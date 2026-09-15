---
title: Red-teaming through predicted answer representations
category: context-prediction
status: Not started
order: 4
---

# Red-teaming through predicted answer representations

[Adversarial suffix optimization](https://arxiv.org/abs/2307.15043) shows that optimizing inputs can expose failures that ordinary prompting misses. [Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) suggests another route: predict an answer representation from the context, apply a behavioral readout, and optimize that prediction.

It would be useful to know whether a differentiable answer predictor can make automated red-teaming more efficient. The challenge is that increasing a predicted risk score may exploit the predictor or produce a context representation that no real prompt can reach.

- Begin with controlled behaviors and compare predicted risk with independently evaluated generated answers.
- Optimize context representations through a fixed answer predictor, then search for prompts that realize the proposed changes.
- Compare with direct prompt optimization at matched model-query budgets.
- Check transfer to new tasks and monitors, and distinguish actual failures from misleadingly high predicted scores.
