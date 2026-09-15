# Mapping context SAE features to answer SAE features

My [recent context-to-answer work](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) finds that a simple map can predict aspects of the answer's activations from the final context activation. This is useful, but a prediction in the residual stream can still be difficult to interpret.

Sparse autoencoders (SAEs) try to express activations in terms of a larger set of features. I propose to investigate whether we can map **context features to answer features**, so that a prediction tells us something more understandable about what the model is likely to do.

[Transcoders](https://arxiv.org/abs/2406.11944) and [crosscoders](https://transformer-circuits.pub/2024/crosscoders/index.html) provide ways to learn relationships between sparse representations. Here, the target would be features of a future answer. [Turn-Averaged SAEs](https://arxiv.org/abs/2606.28548) is especially relevant because encoding an average activation can behave differently from averaging features encoded one token at a time.

We would begin with paired context and answer activations and compare these choices of answer representation. Then we would compare a direct feature-to-feature map against mapping in the residual stream first, using only the context when making predictions.

We would then check:

- Which answer features are predictable before generation starts?
- Are persona and behavioral features easier to predict than details of the answer?
- Does the feature-space map make the relationship easier to explain?
- Do apparent prediction failures come from the model, or from the SAE representation?
