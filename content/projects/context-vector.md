---
title: What is stored in the final context activation?
status: Not started
order: 5
---

# What is stored in the final context activation?

Work on [in-context task vectors](https://arxiv.org/abs/2310.15916) shows that context activations can encode information about the requested task. [My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) studies what they reveal about the upcoming answer. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens, before the answer is generated. This makes it a useful place to ask what has already been decided before generation begins.

It would be useful to separate prompt information, task information and prospective answer information, and understand what additional computation creates each of them. Being able to read something out does not establish that the model uses it.

- Apply a logit lens to individual, mean-pooled and max-pooled activations, tracking how readouts change across layers.
- Use matched prompts to separate facts, task identity, user information and intended behavior.
- Measure what information each additional layer or token contributes, then test its role with interventions.
- Track how the final context vector changes over a conversation, including changes that precede a shift in behavior.
