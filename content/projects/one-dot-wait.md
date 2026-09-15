---
title: Why does “answer in one dot, then wait” change activations?
category: context-prediction
status: Not started
order: 7
---

# Why does “answer in one dot, then wait” change activations?

In our preliminary comparisons, “answer in one dot” and “answer in one dot, then wait” produced very different answer activations. This is interesting alongside [Affine Anticipation](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf): if answer representations carry more than the immediate output, a small instruction about what happens next could change them substantially.

It would be useful to understand whether this difference reflects a plan for subsequent behavior, a changed interpretation of the task, or an artifact of how we collect and average activations.

- Reproduce the difference across prompt paraphrases, models and layers while controlling the actual generated tokens.
- Compare “wait” with stopping, pausing, expecting another user message and continuing with an unrelated action.
- Separate the context, punctuation, end-of-turn and any hidden reasoning positions in the analysis.
- Patch candidate representations between conditions and test whether they change later behavior, rather than only the activation summary.
