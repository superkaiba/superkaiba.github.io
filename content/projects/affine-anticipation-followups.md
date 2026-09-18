---
title: How fine-tuning changes the context-to-answer map
status: In progress
order: 2
---

# How fine-tuning changes the context-to-answer map

My work on linear context-answer relationships studies answer prediction before generation. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens, and that this relationship changes during supervised fine-tuning. My work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) also examines features that change during fine-tuning. Comparing these compact maps could make training-induced behavioral changes easier to study than comparing every activation independently.

It would be useful to predict how a particular training batch changes the map, and whether those changes tell us how the model will behave on other prompts. We are already working on comparing maps across fine-tuning.

- Start with a single training batch and measure changes in the map and in held-out behavior.
- Test whether information about the batch predicts those changes before updating the model.
- Align representation coordinates so a change of basis is not mistaken for a behavioral change.
- Compare SFT and RL updates, and test when predictive map differences support a causal explanation.

<!-- Paper link temporarily hidden: [My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) -->
