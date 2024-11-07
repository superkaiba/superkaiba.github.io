import copy

import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision.datasets import CIFAR10, CIFAR100, MNIST, FashionMNIST
import torchvision.transforms as transforms
import torch

class SlowChangingSequence:
    def __init__(self, change_type, target_function, distribution_type, change_target,
                 change_freq=None, change_timescale=None, seed=None,
                 *args, **kwargs):
        self.seed = seed
        self.rng = np.random.default_rng(seed)  # make RNG for this object only
        self.change_type = change_type #  Specifies how to change the input distribution: smoothly or with jumps
        assert change_type in ('smooth', 'discrete', 'discrete_single', 'stationary')
        self.distribution_type = distribution_type  # specifies how the fast variables are distributed
        assert distribution_type in ('normal', 'rademacher')
        self.change_target = change_target  # if True, changes the target function at discrete intervals
        self.change_freq = change_freq  # if 'discrete', how often to change the distribution
        self.change_timescale = change_timescale
        self.step_counter = 0

        if change_type == 'smooth' and change_timescale is None:
            raise TypeError("change_timescale must be specified")
        elif change_type == 'discrete' and change_freq is None:
            raise TypeError("change_freq must be specified")

        # Inputs vary but the underlying function stays the same
        # some inputs change quickly, some vary slowly

        # generate the underlying function as a small neural net with Relu activation (removes problem of expressivity)

        num_inputs = 16
        num_hidden_units = 32
        self.target_function_name = target_function
        if target_function == 'relu_network':
            self.target_function = TargetNetwork(num_inputs, num_hidden_units, 'relu', self.rng, 2)
        elif target_function == 'ltu_network':  # linear threshold unit (ltu)
            self.target_function = TargetNetwork(num_inputs, num_hidden_units, 'ltu', self.rng, 2)
        elif target_function == 'ltu_network_1layer':
            self.target_function = TargetNetwork(num_inputs, num_hidden_units, 'ltu', self.rng, 1)
        elif target_function == 'ltu_network_4input':
            self.target_function = TargetNetwork(num_inputs, num_hidden_units, 'ltu', self.rng, 1)
        else:
            raise AssertionError(target_function + " is not a valid target function")
        # inputs have dimension 16
        # a quarter of the inputs change fast and the rest change slowly
        # the inputs are of the form X_t = sqrt(beta)*X_{t-1} + sqrt(1-beta)*Y_t where Y_t is an independent standard normal
        # this averaging means that the marginal distribution of X_t is still a standard normal
        # although it is correlated between timesteps
        self.x = self.rng.normal(size=num_inputs)  # the inputs
        if change_type == 'smooth':
            slow_timescale = self.change_timescale  # approximately after this many steps, the initial value is 'forgotten' (not quite, but it's complicated)
            self.slow_factor = 1 - 1/slow_timescale  # this is beta
            # fast_timescale = 1000  # slow timescale isn't used for now
            # self.fast_factor = 1 - 1/fast_timescale

        # the agent can get to see the full distribution across the inputs that change quickly
        # but only gets to see part of the full space for the inputs that change slowly
        pass

    def step(self):
        ''' Updates the x-value and returns it along with the associated target value '''
        if self.distribution_type == 'normal':
            slow_var = self.rng.normal(size=12)
            fast_var = self.rng.normal(size=4)
        elif self.distribution_type == 'rademacher':
            slow_var = self.rng.integers(0, 2, 12) * 2 - 1   # -1, 1 possible
            fast_var = self.rng.integers(0, 2, 4) * 2 - 1

        if self.target_function_name == 'ltu_network_4input':
            slow_var = np.zeros(shape=12)  # we only have the four fast_var dims as inputs

        self.x[0:4] = fast_var

        if self.change_type == 'smooth':
            self.x[4:16] = np.sqrt(self.slow_factor) * self.x[4:16] + np.sqrt(1-self.slow_factor) * slow_var
        elif self.change_type == 'discrete':
            if self.step_counter % self.change_freq == 0:
                self.x[4:16] = slow_var
        elif self.change_type == 'discrete_single':
            if self.step_counter % self.change_freq == 0:
                idx = self.rng.integers(0, 12)
                self.x[idx+4] = slow_var[idx]
        elif self.change_type == 'stationary':  # can also be used if we want to change all the variables at once
            self.x[4:16] = slow_var

        if self.change_target:
            if self.step_counter % self.change_freq == 0:
                # reinitialize the target function
                self.target_function.reset()

        self.step_counter += 1

        return self.x.copy(), self.target_function(self.x).copy()

class TargetNetwork:
    def __init__(self, num_inputs, num_hidden_units, activation_fn, rng, num_hidden_layers):
        ''' This is used to generate a network to be used as a target for regression
         Note: There's no bias terms
         It's a three-layer (2 hidden layer) network. '''
        self.rng = rng  # pass in a random number Generator instance
        self.activation_fn = activation_fn

        self.num_inputs = num_inputs
        self.num_hidden_units = num_hidden_units
        self.num_hidden_layers = num_hidden_layers
        if self.activation_fn == 'relu':
            def relu(y):
                return y * (y > 0)
            self._activation_fn = relu
        elif self.activation_fn == 'ltu':
            def ltu(y):
                return (y > 0).astype('float')
            self._activation_fn = ltu
        else:
            raise AssertionError('invalid activation function')
        self.W1 = rng.normal(0, np.sqrt(2/num_inputs), size=(num_hidden_units, num_inputs))
        self.W2 = rng.normal(0, np.sqrt(2/num_hidden_units), size=(num_hidden_units, num_hidden_units))
        self.W3 = rng.normal(0, np.sqrt(2/num_hidden_units), size=(1, num_hidden_units))
        self.b1 = rng.normal(0, np.sqrt(2/num_inputs), size=num_hidden_units)
        self.b2 = rng.normal(0, np.sqrt(2/num_hidden_units), size=num_hidden_units)

    def __call__(self, x):
        a1 = self._activation_fn(np.dot(self.W1, x) + self.b1)
        if self.num_hidden_layers == 1:
            a2 = a1
        elif self.num_hidden_layers == 2:
            a2 = self._activation_fn(np.dot(self.W2, a1) + self.b2)
        else:
            raise AssertionError('invalid number of layers {}'.format(self.num_hidden_layers))
        out = np.dot(self.W3, a2)
        return np.squeeze(out)

    def reset(self):
        self.__init__(self.num_inputs, self.num_hidden_units, self.activation_fn, self.rng, self.num_hidden_layers)


class PermutedImages:
    def __init__(self, dataset: str, change_freq: int,  batch_size: int,
                 seed: int = None,
                 *args, **kwargs):
        self.dataset = dataset
        self.seed = seed
        self.rng = np.random.default_rng(seed)  # make RNG for this object only

        if seed is not None:
            seed += 100
        self.permutation_rng = np.random.default_rng(seed)
        self.permutation = None

        self.change_freq = change_freq
        self.batch_size = batch_size

        self.training_dataloader = None
        self.test_dataloader = None
        self.training_iterator = None
        self.load_dataset(dataset)

        self.step_counter = 0

    def step(self):
        if (self.step_counter+1) % self.change_freq == 0:  # get a new permutation
            self.permutation = self.permutation_rng.permutation(np.arange(28 * 28))

        try:
            train_imgs, train_labels = next(self.training_iterator)
        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels
        # return train_imgs.reshape(train_imgs.shape[0], -1), train_labels

    def load_dataset(self, name):
        self.permutation = self.permutation_rng.permutation(np.arange(28 * 28))

        transform = transforms.Compose(
            [transforms.ToTensor(),
             transforms.Normalize((0.5,), (0.5,)),
             transforms.Lambda(lambda x: self._permutate_image_pixels(x, self.permutation)),
             transforms.Lambda(lambda x: x.flatten())
             ])
        if name == "MNIST":
            training_data = MNIST(root='./dataset/', train=True, transform=transform, download=False)
            test_data = MNIST(root='./dataset/', train=False, transform=transform, download=False)
        elif name == "FashionMNIST":
            training_data = FashionMNIST(root='./dataset/', train=True, transform=transform, download=False)
            test_data = FashionMNIST(root='./dataset/', train=False, transform=transform, download=False)
        elif name == "CIFAR10":
            training_data = CIFAR10(root='./dataset/', train=True, transform=transform, download=False)
            test_data = CIFAR10(root='./dataset/', train=False, transform=transform, download=False)
        else:
            raise AssertionError("invalid dataset",  name)

        self.training_dataloader = DataLoader(training_data, batch_size=self.batch_size, shuffle=True, num_workers=1)
        self.test_dataloader = DataLoader(test_data, batch_size=500, shuffle=True, num_workers=1)
        self._make_iterator()

    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)

    def _permutate_image_pixels(self, image, permutation):
        if permutation is None:
            return image

        c, h, w = image.size()
        image = image.view(-1, c)
        image = image[permutation, :]
        return image.view(c, h, w)

class SplitImages:
    def __init__(self, dataset: str, change_freq: int,  batch_size: int,
                 seed: int = None, preprocess: str = None, accumulate_data=False,
                 *args, **kwargs):
        self.dataset = dataset
        self.seed = seed
        if seed is not None:
            self.rng = torch.Generator().manual_seed(self.seed)
        else:
            self.rng = None

        self.preprocess = preprocess
        self.change_freq = change_freq
        self.batch_size = batch_size
        self.accumulate_data = accumulate_data

        self.training_dataloader = None
        self.training_data_list = None
        self.test_dataloader = None
        self.training_iterator = None
        self.training_data_index = -1
        self.load_dataset(dataset)

        self.step_counter = 0

    def step(self):

        #change_step = self.change_freq
        change_step = self.training_data_index * self.change_freq

        if (self.step_counter+1) % change_step == 0:  # move on to next split
            self._make_training_split()

        try:
            train_imgs, train_labels = next(self.training_iterator)
        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels

    def load_dataset(self, name):
        if self.preprocess is None:
            transform_train = transform_test = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 ])
        elif self.preprocess.lower() == 'good':
            transform_train = transforms.Compose([
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
            transform_test = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
        else:
            raise AssertionError('Invalid preprocess', self.preprocess)

        if name == "MNIST":
            self.training_data = MNIST(root='./dataset/', train=True, transform=transform_train, download=False)
            self.test_data = MNIST(root='./dataset/', train=False, transform=transform_test, download=False)
        elif name == "CIFAR10":
            self.training_data = CIFAR10(root='./dataset/', train=True, transform=transform_train, download=False)
            self.test_data = CIFAR10(root='./dataset/', train=False, transform=transform_test, download=False)
        else:
            raise AssertionError("invalid dataset",  name)

        self.training_data_index = -1
        self._make_training_split()
        self.test_dataloader = DataLoader(self.test_data, batch_size=self.batch_size, shuffle=True, num_workers=1)

    def _make_training_split(self):
        ''' Creates the next training set and iterator. Iterates through the 10 splits created.
        Once the last split is done, it recreates a new set of 10 splits.
        If self.accumulate_data=True, we keep data from previous splits. For the 10th task onwards, the whole dataset is available'''
        if self.training_data_index < 0 or (self.training_data_index >= 10 and not self.accumulate_data):  # make new splits
            self.training_data_index = 0
            self.training_data_list = torch.utils.data.random_split(self.training_data, np.ones(10)/10,
                                                                        generator=self.rng)

        if self.accumulate_data:
            training_dataset = torch.utils.data.ConcatDataset(self.training_data_list[:self.training_data_index+1])
        else:
            training_dataset = self.training_data_list[self.training_data_index]
        self.training_dataloader = DataLoader(training_dataset,
                                              batch_size=self.batch_size, drop_last=True, shuffle=True, num_workers=1)
        self._make_iterator()
        self.training_data_index += 1

    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)

class ClassSplitImages:
    def __init__(self, dataset: str, change_freq: int,  batch_size: int,
                 seed: int = None, preprocess: str = None, accumulate_data=False,
                 *args, **kwargs):
        self.dataset = dataset
        self.seed = seed
        if seed is not None:
            self.rng = torch.Generator().manual_seed(self.seed)
        else:
            self.rng = None

        self.preprocess = preprocess
        self.change_freq = change_freq
        self.batch_size = batch_size
        self.accumulate_data = accumulate_data

        self.training_dataloader = None
        self.training_data_list = None
        self.test_dataloader = None
        self.training_iterator = None
        self.training_data_index = -1
        self.load_dataset(dataset)

        self.step_counter = 0

    def step(self):

        #change_step = self.change_freq
        change_step = self.training_data_index * self.change_freq

        if (self.step_counter+1) % change_step == 0:  # move on to next split
            self._make_training_split()

        try:
            train_imgs, train_labels = next(self.training_iterator)

        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels

    def load_dataset(self, name):
        if self.preprocess is None:
            transform_train = transform_test = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 ])
        elif self.preprocess.lower() == 'good':
            transform_train = transforms.Compose([
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
            transform_test = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
        else:
            raise AssertionError('Invalid preprocess', self.preprocess)

        if name == "CIFAR100":
            self.training_data = CIFAR100(root='./dataset/', train=True, transform=transform_train, download=False)
            self.test_data = CIFAR100(root='./dataset/', train=False, transform=transform_test, download=False)
        else:
            raise AssertionError("invalid dataset",  name)

        self.training_data_index = -1
        self._make_training_split()

    def _make_training_split(self):
        ''' Creates the next training set and iterator. Iterates through the 10 splits created.
        Once the last split is done, it recreates a new set of 10 splits.
        Each split contains the data from 5 classes.
        If self.accumulate_data=True, then we keep data from all previous splits for the current task. '''
        num_classes_per_split = 10
        num_splits = 10
        if self.training_data_index >= num_splits or self.training_data_index < 0:
            self.training_data_index = 0
            self.permutation = torch.randperm(100)

        if self.accumulate_data:
            mask = torch.isin(torch.tensor(self.training_data.targets), self.permutation[:num_classes_per_split * (self.training_data_index + 1)])
        else:
            mask = torch.isin(torch.tensor(self.training_data.targets), self.permutation[num_classes_per_split*self.training_data_index:num_classes_per_split*(self.training_data_index+1)])
        subset_idx = np.arange(len(self.training_data.targets))[mask]
        subset = torch.utils.data.Subset(self.training_data, subset_idx)

        self.training_dataloader = DataLoader(subset, batch_size=self.batch_size, drop_last=True, shuffle=True, num_workers=1)

        if self.accumulate_data:
            self.test_dataloader = DataLoader(self.test_data, batch_size=self.batch_size, shuffle=False, num_workers=1)
        else:
            # make test dataloader too to only evaluate the current classes being trained on
            test_mask = torch.isin(torch.tensor(self.test_data.targets), self.permutation[num_classes_per_split*self.training_data_index:num_classes_per_split*(self.training_data_index+1)])
            test_subset_idx = np.arange(len(self.test_data.targets))[test_mask]
            test_subset = torch.utils.data.Subset(self.test_data, test_subset_idx)
            self.test_dataloader = DataLoader(test_subset, batch_size=self.batch_size, shuffle=True, num_workers=1)

        self._make_iterator()
        self.training_data_index += 1

    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)

class VanillaImages:
    def __init__(self, dataset: str, batch_size: int,
                 seed: int = None, preprocess: str = None,
                 *args, **kwargs):
        self.dataset = dataset
        self.seed = seed

        if seed is not None:
            self.rng = torch.Generator().manual_seed(self.seed)
        else:
            self.rng = None

        self.preprocess = preprocess
        self.batch_size = batch_size

        self.training_dataloader = None
        self.training_data_list = None
        self.test_dataloader = None
        self.training_iterator = None
        self.training_data_index = -1
        self.load_dataset(dataset)

        self.step_counter = 0

    def step(self):
        try:
            train_imgs, train_labels = next(self.training_iterator)
        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels

    def load_dataset(self, name):
        if self.preprocess is None:
            transform_train = transform_test = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 ])
        elif self.preprocess.lower() == 'good':
            transform_train = transforms.Compose([
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
            transform_test = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ])
        else:
            raise AssertionError('Invalid preprocess', self.preprocess)

        if name == "CIFAR10":
            self.training_data = CIFAR10(root='./dataset/', train=True, transform=transform_train, download=False)
            self.test_data = CIFAR10(root='./dataset/', train=False, transform=transform_test, download=False)
        elif name == "CIFAR100":
            self.training_data = CIFAR100(root='./dataset/', train=True, transform=transform_train, download=False)
            self.test_data = CIFAR100(root='./dataset/', train=False, transform=transform_test, download=False)
        else:
            raise AssertionError("invalid dataset",  name)

        self.training_data_index = -1
        self.test_dataloader = DataLoader(self.test_data, batch_size=self.batch_size, shuffle=True, num_workers=1)
        self.training_dataloader = DataLoader(self.training_data, batch_size=self.batch_size, shuffle=True, num_workers=1)
        self._make_iterator()

    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)


class EvalCIFARImages:   # use this to evaluate the plasticity of agents
    def __init__(self, dataset_name, transform_name, batch_size=128, seed=None,
                 *args, **kwargs):
        ''' This class is used to create tasks related to the CIFAR10/100 datasets.  '''
        self.dataset_name = dataset_name
        assert dataset_name.lower() in ('cifar10', 'cifar100')
        self.transform_name = transform_name
        self.rng = np.random.default_rng(seed)
        self.step_counter = 0

        self.batch_size = batch_size

        self.training_dataloader = None
        self.test_dataloader = None
        self.training_iterator = None

        self.load_dataset(dataset_name, transform_name)
        self._make_iterator()

    # Removed: this was only needed to switch the tasks
    # def eval_step(self):
    #     try:
    #         imgs, labels = next(self.train_iterator)
    #     except StopIteration:
    #         self._make_iterator()
    #         imgs, labels = next(self.train_iterator)
    #
    #     self.train_step_counter += 1
    #     return imgs, labels

    def step(self):
        try:
            train_imgs, train_labels = next(self.training_iterator)
        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels

    def load_dataset(self, dataset_name, transform_name):
        if dataset_name.lower() == 'cifar10':
            num_labels = 10
        elif dataset_name.lower() == 'cifar100':
            num_labels = 100

        transform_input_fn = transforms.Compose(
            [transforms.ToTensor(),
             transforms.Normalize((0.5,), (0.5,)),
             ])
        transform_target_fn = None

        if transform_name == 'random_labels':  # every label is chosen uniformly at random
            pass  # labels are remade after the dataset is loaded
        elif transform_name == 'shuffled_labels':  # each label is mapped to a different one but classes are preserved
            self.label_mapping = self.rng.permutation(num_labels)
            transform_target_fn = lambda y: self.label_mapping[y]
        elif transform_name == 'blurred_inputs':
            transform_input_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 transforms.GaussianBlur((5,5), 1.5),
                 ])
        elif transform_name == 'random_crop_flip_inputs':
            transform_input_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 transforms.RandomCrop(32, padding=4),
                 transforms.RandomHorizontalFlip(),
                 ])
        elif transform_name == 'permuted_inputs':
            permutation = self.rng.permutation(np.arange(32 * 32))
            transform_input_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Lambda(lambda x: permutate_image_pixels(x, permutation)),
                 # transforms.Lambda(lambda x: self._permutate_image_pixels(x)),
                 # transforms.Lambda(lambda x: dummy_transform(x)),
                 transforms.Normalize((0.5,), (0.5,)),
                 ])
        elif transform_name == 'grayscale_inputs':
            transform_input_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 transforms.Grayscale(num_output_channels=3),
                 ])
        else:
            raise AssertionError("invalid transform", transform_name)

        if dataset_name.lower() == "cifar10":
            self.training_data = CIFAR10(root='./dataset/', train=True, transform=transform_input_fn, target_transform=transform_target_fn, download=False)
            self.test_data = CIFAR10(root='./dataset/', train=False, transform=transform_input_fn, target_transform=transform_target_fn, download=False)
            # self.eval_data = RandomImagesLabelsDataset
        elif dataset_name.lower() == "cifar100":
            self.training_data = CIFAR100(root='./dataset/', train=True, transform=transform_input_fn, target_transform=transform_target_fn, download=False)
            self.test_data = CIFAR100(root='./dataset/', train=False, transform=transform_input_fn, target_transform=transform_target_fn, download=False)
        else:
            raise AssertionError("invalid dataset",  dataset_name)

        self.training_dataloader = DataLoader(self.training_data, batch_size=self.batch_size, shuffle=True, num_workers=1)
        self.test_dataloader = DataLoader(self.test_data, batch_size=self.batch_size, shuffle=True, num_workers=1)

        if transform_name == 'random_labels':
            self.training_data.targets = [self.rng.integers(0, num_labels) for _ in range(len(self.training_data.targets))]
            self.test_dataloader = None
    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)

def permutate_image_pixels(image, permutation):
    if permutation is None:
        return image
    # print(type(image))
    #
    c, h, w = image.size()
    image = image.view(-1, c)
    image = image[permutation, :]
    return image.view(c, h, w)

# def dummy_transform(image):
#     return image

class EvalSyntheticImages:
    def __init__(self, dataset_name, base_dataset_name, batch_size=500, seed=None,
                 *args, **kwargs):
        ''' This class is used to create synthetic images and labels
          dataset_name: specifies how the images and labels are generated
          base_dataset_name: 'mnist' or 'cifar10' or 'cifar100' to copy the shapes
           Note: test_iterator is None. We need to check for this in the evaluation class '''
        self.dataset_name = dataset_name
        self.dataset_name_shape = base_dataset_name
        self.rng = np.random.default_rng(seed)
        self.step_counter = 0

        self.batch_size = batch_size

        self.training_dataloader = None
        self.test_dataloader = None
        self.training_iterator = None

        self.load_dataset(dataset_name, base_dataset_name)
        self._make_iterator()

    def step(self):
        try:
            train_imgs, train_labels = next(self.training_iterator)
        except StopIteration:
            self._make_iterator()
            train_imgs, train_labels = next(self.training_iterator)

        self.step_counter += 1
        return train_imgs, train_labels


    def load_dataset(self, dataset_name, base_dataset_name):
        if dataset_name == 'random':
            input_transform_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 ])
        elif dataset_name == 'random_smooth':
            input_transform_fn = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5,), (0.5,)),
                 transforms.GaussianBlur(kernel_size=5, sigma=1.5),
                 ])

        if 'random' in dataset_name:
            self.training_data = RandomImagesLabelsDataset(dataset_name=base_dataset_name, transform=input_transform_fn)
        else:
            raise AssertionError('invalid dataset name', dataset_name)

        self.training_dataloader = DataLoader(self.training_data, batch_size=self.batch_size, shuffle=True,
                                              num_workers=1)
        self._make_iterator()

    def _make_iterator(self):
        self.training_iterator = iter(self.training_dataloader)


class SequenceCIFAREnvs:
    def __init__(self, change_freq, dataset_name, batch_size=128, seed=None,
                 *args, **kwargs):

        self.change_freq = change_freq
        self.dataset_name = dataset_name
        self.batch_size = batch_size
        self.seed = seed

        self.child_env = None

        self.change_counter = 0
        self.step_counter = 0

        self.training_dataloader = None
        self.test_dataloader = None
        self._init_child_env()

    def step(self):
        self.step_counter += 1

        transition = self.child_env.step()

        if self.step_counter % self.change_freq == 0:
            self.change_counter += 1
            self._init_child_env()

        return transition

    def _init_child_env(self):
        if self.dataset_name[0:9] == 'sequence_':
            name = self.dataset_name[9:]

            if self.seed is not None:
                seed = self.seed + self.change_counter
            else:
                seed = None
            env_dict = {'batch_size': self.batch_size, 'seed': seed}

            if name in ('cifar10', 'cifar100'):
                env_class = VanillaImages
                env_dict['dataset'] = name.upper()

            elif name == 'cifar10_random_inputs_random_labels':
                env_class = EvalSyntheticImages
                env_dict['dataset_name'] = 'random'
                env_dict['base_dataset_name'] = 'cifar10'
            elif name == 'cifar10_random_smooth_inputs_random_labels':
                env_class = EvalSyntheticImages
                env_dict['dataset_name'] = 'random_smooth'
                env_dict['base_dataset_name'] = 'cifar10'
            elif name == 'cifar10_random_labels':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'random_labels'
            elif name == 'cifar10_shuffled_labels':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'shuffled_labels'
            elif name == 'cifar10_permuted_inputs':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'permuted_inputs'
            elif name == 'cifar10_grayscale_inputs':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'grayscale_inputs'
            elif name == 'cifar10_blurred_inputs':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'blurred_inputs'
            elif name == 'cifar10_random_crop_flip_inputs':
                env_class = EvalCIFARImages
                env_dict['dataset_name'] = 'cifar10'
                env_dict['transform_name'] = 'random_crop_flip_inputs'
            else:
                raise AssertionError('invalid env ', self.dataset_name)

            if self.child_env is not None:
                del self.child_env

            self.child_env = env_class(**env_dict)
            self.training_dataloader = self.child_env.training_dataloader
            self.test_dataloader = self.child_env.test_dataloader

        #     if name == 'cifar10_random_inputs_random_labels':
        #         ...
        #     else:
        #         #
        #         self.child_env = EvalCIFARImages(name, transform_name=)
        # if self.dataset_name == 'sequence_cifar10_random_inputs_random_labels':
        #     self.child_env = EvalCIFARImages()
        # ...

    def evaluate_agent(self, *args, **kwargs):
        return None


class RandomImagesLabelsDataset(Dataset):
    def __init__(self, dataset_name, seed=None, transform=None):
        # Initialize the dataset by loading or processing the data
        # transform: Optional data transformations (e.g., for preprocessing)

        self.dataset_name = dataset_name
        self.transform = transform
        self.rng = np.random.default_rng(seed)

        dataset_size = 50000
        if 'cifar10' in self.dataset_name.lower():
            # the data matches specs for a numpy image. Dimensions are ordered (H x W x C) and uint8
            self.data = self.rng.integers(0, 256, (dataset_size, 32, 32, 3), dtype=np.uint8)
            self.labels = self.rng.integers(0, 10, dataset_size)
        elif 'cifar100' in self.dataset_name.lower():
            # the data matches specs for a numpy image. Dimensions are ordered (H x W x C) and uint8
            self.data = self.rng.integers(0, 256, (dataset_size, 32, 32, 3), dtype=np.uint8)
            self.labels = self.rng.integers(0, 100, dataset_size)
        elif 'mnist' in self.dataset_name.lower():
            self.data = self.rng.integers(0, 256, (dataset_size, 28, 28, 1), dtype=np.uint8)
            self.labels = self.rng.integers(0, 10, dataset_size)
        else:
            raise AssertionError("Invalid dataset name", str(self.dataset_name))

    def __len__(self):
        # Return the total number of samples in the dataset
        return len(self.data)  # Modify according to your data structure

    def __getitem__(self, idx):
        # Return a single sample and its corresponding label
        sample = self.data[idx]
        label = self.labels[idx]
        # Apply any transformations if needed
        if self.transform:
            sample = self.transform(sample)
        return sample, label



def eval_with_dataloader(agent, dataloader, eval=False, metrics=None, verbose=False):
    ''' Returns various metrics related to the given dataset (usually the test set) E.g. test loss of a model
    assumes agent contains a .net attribute which is the torch model)
     metrics: a list of metrics to be computed. If None, does all of them.
     eval: If true, sets the network to eval mode first '''
    if dataloader is None:  # this is useful for tasks where there is no test set
        return None

    correct = 0
    total = 0
    # reset storage variables
    if metrics is None or 'dead_units_frac' in metrics:
        agent.get_dead_units_frac(reset=True)
    if metrics is None or 'avg_activation_norm' in metrics:
        agent.get_average_activation(reset=True)

    if eval:
        agent.net.eval()
    with torch.no_grad():
        counter = 0
        for images, labels in dataloader:

            counter += 1
            if counter > 2: # todo remove
                break
            output = agent.predict(images, to_numpy=False)

            # accuracy
            if metrics is None or 'accuracy' in metrics:
                _, predictions = torch.max(output, 1)
                for label, prediction in zip(labels, predictions):
                    if label == prediction:
                        correct += 1
                    total += 1
                accuracy = correct / total
            else:
                accuracy = None

            # compute test metrics
            if metrics is None or 'dead_units_frac' in metrics:
                dead_units_frac = agent.get_dead_units_frac(accumulate=True)
            else:
                dead_units_frac = None

            if metrics is None or 'avg_activation_norm' in metrics:
                avg_activation_norm = agent.get_average_activation(accumulate=True)
            else:
                avg_activation_norm = None

            if verbose:
                print(counter, correct, total, accuracy)

    if eval:
        agent.net.train()

    results = {'accuracy': accuracy,
               'dead_units_frac': dead_units_frac,
               'avg_activation_norm': avg_activation_norm}
    return results



if __name__ == "__main__":
    # from guppy import hpy
    #
    # h = hpy()
    # h.heap()
    #
    import time

    env = SequenceCIFAREnvs(2, 'sequence_cifar10_permuted_inputs')

    for i in range(1000):
        time.sleep(0.01)
        env.step()
        print(env.change_counter)

    # import matplotlib.pyplot as plt
    # # env = EvalCIFARImages('CIFAR10', 'grayscale_inputs')
    # env = EvalSyntheticImages('random_smooth', 'CIFAR10')
    #
    # img, label = next(env.training_iterator)
    #
    #
    # for i in range(5):
    #     print('label', label[i])
    #     plt.figure()
    #     plt.imshow(transforms.ToPILImage()(img[i]))
    # plt.show()

    # training_data = CIFAR100(root='./dataset/', train=True, download=False)


    # permutation = torch.randperm(100)
    # print(training_data.targets[:100])
    # print(permutation)
    # idx = torch.isin(torch.tensor(training_data.targets), permutation[0:5])
    #
    # sub = np.arange(len(training_data.targets))[idx]
    # print(type(sub))
    #
    # subset = torch.utils.data.Subset(training_data, sub)
    #
    # print(torch.tensor(training_data.targets)[idx])


    # training_subset = torch.utils.data.Subset()
    # f = TargetNetwork(16, 32, 'ltu', np.random.default_rng(), 1)
    # for idx in range(16):
    #     x_slice = np.linspace(-1,1, 20)
    #
    #     x = np.zeros(16)
    #     y_lst = []
    #     for x_i in x_slice:
    #         x[idx] = x_i
    #         print(f(x))
    #         y_lst.append(f(x))
    #
    #     import matplotlib.pyplot as plt
    #
    #     plt.plot(x_slice, y_lst, alpha=0.5)
    # plt.show()
    #
    #
    # quit()

    #
    # task = SlowChangingSequence('stationary', )
    # lst = []
    # lst_y = []
    # for i in range(100000):
    #     x,y = task.step()
    #     # lst.append(x[10])
    #     lst_y.append(float(y))
    #     # print(x,y)
    #
    # import matplotlib.pyplot as plt
    # # plt.plot(lst)
    # # plt.plot(lst_y[0:10000])
    # # plt.ylim(-2.5, 2.5)
    # plt.show()
    #
