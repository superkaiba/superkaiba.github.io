---
title: A general predictor between activation locations
status: Not started
order: 9
---

# A general predictor between activation locations

[Jump to Conclusions](https://arxiv.org/abs/2303.09435) learns linear maps from intermediate to final representations. [Future Lens](https://arxiv.org/abs/2311.04897) predicts future hidden states and token outputs from a single hidden state. [Model stitching](https://arxiv.org/abs/2506.06609) transfers features between different models through affine mappings. [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964) learns an activation distribution with diffusion models, providing a prior over plausible internal states. These results suggest a broader question: can separately useful predictors and activation priors be combined into a consistent description of how representations change?

It would be useful to build a predictor that can move between activation locations across tokens, layers and models, and determine where that description breaks down. A map that predicts one destination accurately might still become unreliable when composed with other maps.

- Fit token-to-token and layer-to-layer predictors on the same data, comparing linear maps, nonlinear regressors and conditional generative models.
- Compare predicting a destination directly with reaching it through intermediate layers or tokens.
- Test whether constraints requiring these paths to agree improve generalization and repeated prediction.
- Extend to pairs of models and distinguish changes of coordinates from information that one model does not represent.
