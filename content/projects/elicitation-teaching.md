---
title: Mechanistic differences between elicitation and teaching
status: In progress
order: 52
---

# Mechanistic differences between elicitation and teaching

[Bits That Count](https://icml.cc/virtual/2026/poster/61292) studies how to quantify and predict capabilities, while [mechanistic analysis of fine-tuning on procedurally defined tasks](https://arxiv.org/abs/2311.12786) provides controlled settings for examining training effects. A better score alone does not tell us whether training taught something new or made an existing capability easier to access.

It would be useful to identify internal signatures of that distinction and compare them across SFT and RL. This project is already in progress.

- Use controlled tasks where the available information and newly introduced information are known.
- Compare representation changes, affected components and gradients under teaching and elicitation conditions.
- For RLVR, specify the allowed prefix or activation interventions and test how closely they reproduce post-trained behavior.
- Treat unsuccessful elicitation as evidence about the tested method, rather than proof that the capability was absent.
