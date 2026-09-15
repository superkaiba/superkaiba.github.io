---
title: A general predictor between activation locations
category: representations
status: Not started
order: 2
---

# A general predictor between activation locations

[Jump to Conclusions](https://arxiv.org/abs/2303.09435) learns linear maps from intermediate to final representations. [Model stitching](https://arxiv.org/abs/2506.06609) transfers features between different models through affine mappings. These results suggest a broader question: can separately useful mappings be combined into a consistent description of how representations change?

It would be useful to build a predictor that can move between activation locations across tokens, layers and models, and determine where that description breaks down. A map that predicts one destination accurately might still become unreliable when composed with other maps.

- Fit token-to-token and layer-to-layer predictors on the same data, comparing linear and nonlinear models.
- Compare predicting a destination directly with reaching it through intermediate layers or tokens.
- Test whether constraints requiring these paths to agree improve generalization and repeated prediction.
- Extend to pairs of models and distinguish changes of coordinates from information that one model does not represent.
