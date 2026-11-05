---
title: Do LLM neurons grow by recursive generalization during training?
status: Not started
order: 10.3
math: true
---

# Do LLM neurons grow by recursive generalization during training?

**TL;DR:** Follow individual MLP neurons across Pythia and OLMo pretraining checkpoints. Test whether each neuron's activating contexts grow outward from one starting concept through nearby concepts, as the recursive generalization account predicts, or whether neurons pick up unrelated concepts.

[Neural Networks Are Already Clean](https://already-clean.goodfire.com/) argues that most apparent polysemanticity in neurons comes from a motif it calls recursive generalization. A neuron starts on one concept, then extends to related concepts, and those extensions extend again. Its example is a language-model neuron that fires on "iy", then on "diy", then on "do it yourself", which no longer contains "iy". The essay contrasts this with superposition in the sense of a neuron packing unrelated concepts together because they rarely co-occur. The two accounts predict different things about how a neuron's activating contexts change over training. Recursive generalization predicts that each new concept is close to one the neuron already has. Packing of unrelated concepts predicts no such locality.

The essay watched this happen only in vision models. It retrained InceptionV1 and a ConvNeXt on ImageNet and followed last-layer neurons from epoch 0.7 to 12. One InceptionV1 neuron starts on rapeseed fields, picks up tennis balls, fruit and dogs, then broccoli, until the fields nearly disappear. A ConvNeXt neuron reaches for the same offshoots early and then drops them. The language-model evidence (Qwen3-32B and Kimi K3) comes from finished models without public checkpoints. The essay says testing this across a whole language model isn't a priority for its authors and probably wouldn't be hard. The idea first appeared as "conjoined features" in [Multimodal Neurons](https://distill.pub/2021/multimodal-neurons/), also studied in a finished model.

Existing work on language-model training dynamics mostly tracks other units or other questions. [SAE-Track](https://arxiv.org/abs/2412.17626), [crosscoders across Pythia snapshots](https://arxiv.org/abs/2509.17196) and [Crosscoding Through Time](https://arxiv.org/abs/2509.05291) follow dictionary features, and the essay argues that dictionaries can split one neuron's job into several features. [Universal neurons in GPT-2](https://arxiv.org/abs/2508.00903) tracks whether neurons stay correlated across seeds over checkpoints. The [German context neuron](https://arxiv.org/abs/2311.00863) study follows one native Pythia-70M neuron and its circuit across checkpoints, but it asks how the circuit forms. I haven't found a study that follows the activating contexts of native LLM neurons across checkpoints and tests whether they grow locally.

A study like this could also settle some of the disputed cases. [Commentary on the essay](https://www.lesswrong.com/posts/w2tBHwNERDoSawznx/i-can-see-everything) reports that its Colorado neuron in Qwen3 also fires on code for the Tornado Python web framework, and [Neural Networks Are Not Already Clean](https://www.lesswrong.com/posts/Dkh7pXKjoNWkkxQDz/neural-networks-are-not-already-clean) disputes the broader claim. With checkpoints, a second job like this can be checked directly. Either it enters as an offshoot of something the neuron already responds to, or it enters with nothing nearby.

**Measuring locality.** For one neuron, cluster its top activating contexts at checkpoint $t$ into a set of facets $F_t$. Represent each facet $f$ by the mean embedding $e_f$ of its contexts. When a facet $f$ first appears at checkpoint $t$, measure its distance to the closest facet the neuron already had:

$$
\delta(f) = \min_{g \in F_{t-1}} \big(1 - \cos(e_f, e_g)\big).
$$

As a null, replace $F_{t-1}$ with the facets of a random neuron from the same layer and checkpoint, which gives $\delta_{\text{null}}(f)$. Recursive generalization predicts that $\delta(f)$ is usually smaller than $\delta_{\text{null}}(f)$. If neurons pick up unrelated concepts, the two distributions should look about the same.

**Initial directions:**

- **Pick neurons and checkpoints.** Start with Pythia, which has GELU MLP neurons and 154 public checkpoints, spaced log-uniformly early in training. Sample neurons from several layers at the final checkpoint without selecting for interpretability. Add neurons that a standard autointerp pass labels polysemantic.
- **Build facet histories.** At each checkpoint, collect the top activating contexts from a fixed text sample. Set the threshold as a fraction of the neuron's maximum at that checkpoint, so changes in activation scale don't add or remove facets. Cluster the contexts into facets, label each facet with an LLM, and match facets across checkpoints by embedding similarity.
- **Measure locality and order.** Compute $\delta$ for every new facet and compare it with the random-neuron null and with a null that shuffles the order of checkpoints. Record the order in which facets arrive. The branching picture predicts that later facets are further from the neuron's first facet and closer to some intermediate facet.
- **Trace the route each facet arrives through.** For each new facet, find the upstream neurons and attention heads that drive the neuron on that facet's contexts. In the essay's planetary geology neuron, a code offshoot arrives through its own upstream route. Test how often an offshoot reuses the route of a nearby existing facet.
- **Track pruning as well as growth.** Record facets that appear and later disappear, as in the ConvNeXt neuron. Test whether pruned facets mattered less to the loss (when the neuron is ablated on those contexts) than facets that stay.
- **Compare architectures and scales.** Repeat on OLMo checkpoints, which use SwiGLU. Separate out the double-negative regime the essay describes, where a negative gate times a negative value gives positive activations that resemble the negative pole. Compare Pythia sizes to test the essay's claim that smaller models have broader neurons with more offshoots.
- **Look for counterexamples directly.** Collect neurons whose final facets look unrelated, like the Colorado and Tornado case. Check whether their histories show a chain of nearby facets connecting the two, or a facet that arrives with nothing nearby.

The intended output is a set of facet histories for a few hundred neurons, the fraction whose growth is local under both nulls, and the clearest examples of branching and of counterexamples. A positive result would support studying native neurons directly. A negative result would show which neurons pick up unrelated concepts and at what point in training it starts.

**Related projects:** [Are GLP neurons broadly interpretable?](#glp-neuron-interpretability) audits neuron interpretability in another basis. [Semantic structure in native residual coordinates](#native-coordinates) asks when the model's own coordinates carry stable concepts. [Tracking concept and persona interpretability through pretraining](#concept-persona-pretraining) uses the same kind of checkpoints for probe-based questions. [A SimpleStories successor with forum threads and dense checkpoints](#simplestories-forums) would provide dense checkpoints at small scale.
