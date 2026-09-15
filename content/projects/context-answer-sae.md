---
title: Mapping context SAE features to answer SAE features
status: Not started
order: 6
---

# Mapping context SAE features to answer SAE features

Our [context-to-answer work](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) predicts answer activations, but a residual-stream prediction can still be difficult to interpret. [Transcoders](https://arxiv.org/abs/2406.11944) offer a way to express relationships through sparse features, while work on [Turn-Averaged SAEs](https://arxiv.org/abs/2606.28548) motivates treating an entire response as a unit of analysis.

It would be useful to predict understandable answer features directly from context features. We should also determine whether an apparent prediction failure belongs to the language model or to the feature representation used to describe it.

- Compare averaging token-level SAE features with encoding the mean answer activation.
- Fit linear maps, nonlinear maps and transcoder-style predictors from context features to answer features.
- Compare direct feature prediction with predicting residual-stream activations first and then encoding them.
- Identify which persistent behavioral features and rare answer features can be anticipated before generation.
