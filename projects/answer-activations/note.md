# Predicting answer activations from context

I have some results showing that a linear map can predict much of an answer's mean activation from the final context activation, described in [Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf). [Future Lens](https://arxiv.org/abs/2311.04897) studies a related possibility at the level of future tokens. These results suggest that useful information about an answer is available before it is generated, but a good average prediction can still miss the behavior we care about.

It would be useful to understand what is linearly predictable, what requires nonlinearity, and how much uncertainty comes from the model sampling different answers. This is a follow-up to Affine Anticipation.

- Characterize the most and least predictable directions and the dimensionality of answer representations.
- Separate persistent behavioral information from token-specific variation and sampling noise from prediction error.
- Compare pooling across tokens and layers, and track predictability as an answer unfolds.
- Forecast a judge's verdict before and during generation, checking predictions against actual outputs.
- Test rare behaviors and reward hacking, paying particular attention to calibration and false negatives.
