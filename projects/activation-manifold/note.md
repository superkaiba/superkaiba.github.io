# Characterizing activation geometry with nonlinear factors

Recent methods go beyond decomposing activations into individual directions. [SMIXAE](https://arxiv.org/abs/2605.09224) learns multidimensional structures with a mixture of autoencoders, [bilinear autoencoders](https://arxiv.org/abs/2605.08891) use quadratic features, and [generative activation models](https://arxiv.org/abs/2602.06964) learn distributions that can guide interventions. These provide starting points for studying the broader activation space, beyond a selected set of persona traits.

It would be useful to characterize which nonlinear factors organize a model's activations and whether they provide stable, interpretable coordinates for its behavior. We should allow several overlapping structures rather than assume that all activations lie on one simple surface.

- Compare linear dictionaries, local subspaces and nonlinear autoencoders on diverse text and task distributions.
- Identify factors whose interpretations persist across held-out contexts, layers and training runs.
- Measure reconstruction and behavioral prediction, checking whether additional complexity provides a useful improvement.
- Intervene along learned factors and test whether they permit selective control without disrupting unrelated behavior.
