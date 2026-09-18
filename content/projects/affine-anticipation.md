---
title: Affine Anticipation
status: Completed
published: false
order: 64
---

# Affine Anticipation

Generating an answer involves many nonlinear steps, but how much of its internal representation is already determined by the context? [Future Lens](https://arxiv.org/abs/2311.04897) studies anticipation of subsequent tokens; our work asks about a representation summarizing an entire answer.

[My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) studies answer prediction before generation. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens. On held-out Qwen2.5-7B-Instruct conversations, the linear map reaches R² = 0.81, compared with 0.86 for a nonlinear MLP. Probes applied to these predicted activations can forecast behaviors such as sycophancy, hallucination and harmful compliance before generation.

The completed paper is the starting point for [predicting answer activations](#answer-activations), [studying fine-tuning changes](#affine-anticipation-followups) and [forecasting conversation dynamics](#conversation-dynamics).
