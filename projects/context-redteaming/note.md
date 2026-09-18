# Red-teaming through predicted answer representations

[Adversarial suffix optimization](https://arxiv.org/abs/2307.15043) shows that optimizing inputs can expose failures that ordinary prompting misses. [My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) studies answer prediction before generation. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens. This suggests another route: apply a behavioral readout to the predicted answer activation and optimize the context to increase the predicted risk.

It would be useful to know whether a differentiable answer predictor can make automated red-teaming more efficient. The challenge is that increasing a predicted risk score may exploit the predictor or produce a context representation that no real prompt can reach.

- Begin with controlled behaviors and compare predicted risk with independently evaluated generated answers.
- Optimize context representations through a fixed answer predictor, then search for prompts that realize the proposed changes.
- Compare with direct prompt optimization at matched model-query budgets.
- Check transfer to new tasks and monitors, and distinguish actual failures from misleadingly high predicted scores.
