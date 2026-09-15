---
title: How fine-tuning changes the context-to-answer map
category: context-prediction
status: In progress
order: 2
---

# How fine-tuning changes the context-to-answer map

[Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) includes initial comparisons of context-to-answer maps across training stages. My work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) also examines features that change during fine-tuning. A compact map could make training-induced behavioral changes easier to study than comparing every activation independently.

It would be useful to predict how a particular training batch changes the map, and whether those changes tell us how the model will behave on other prompts. We are already working on comparing maps across fine-tuning.

- Start with a single training batch and measure changes in the map and in held-out behavior.
- Test whether information about the batch predicts those changes before updating the model.
- Align representation coordinates so a change of basis is not mistaken for a behavioral change.
- Compare SFT and RL updates, and test when predictive map differences support a causal explanation.
