# Personas as persistent features

There has been a lot of work on [persona features](https://arxiv.org/abs/2506.19823) and the [assistant axis](https://arxiv.org/abs/2601.10387), but I still think there is a basic question about what makes something a persona rather than an ordinary feature.

Intuitively, a persona should persist. If a model is answering in a particular character or style, we do not expect it to abruptly switch halfway through a sentence. This suggests that persistence across tokens might help identify high-level behavioral features.

I propose to look at this in two ways:

- Find SAE features that remain active over many tokens, and test whether they are especially associated with personas or behavioral traits.
- Fit a linear map from one token's activation to the next, then inspect directions that the map tends to preserve.

We would want to distinguish persona persistence from simpler explanations, such as the answer staying on the same topic. A further question is whether reinforcing or disrupting these persistent directions changes persona stability over a long conversation.
