---
title: First-, second-, and third-person identity in prompts
status: Fleshed out
order: 23
---

# First-, second-, and third-person identity in prompts

**TLDR:** Test how "I am," "You are," and "The assistant is," placed in system or user prompts, affect the model's internal representations of itself and expressed traits/behaviors/identity

System prompts (or user prompts) often say things such as "You are Claude" or "You are a programmer" (second person pronouns) in order to confer a certain identity to the LLM assistant. However, based on the PSM ([Marks et al., 2026](https://alignment.anthropic.com/2026/psm/)), something that makes more sense is potentially saying "The assistant is Claude" or "The assistant is a programmer" (third person pronouns), "I am Claude" or "I am a programmer" (first person pronouns) or even "All AI assistants are programmers"

No one has conducted a principled study of the differences between these forms of giving the assistant its identity (the closest I could find is [this paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0341558) which compares first person prompting in the chat template with third person prompting outside the chat template, but this is quite different; prior work on personas in system prompts varies which role is given, not how it is phrased: [Zheng et al., 2024](https://arxiv.org/abs/2311.10054)). This would be useful both to understand better how to instill a robust identity into a model with prompting/system prompting, and to gain better understanding of how the model represents the assistant (e.g. the Assistant Axis: [Lu et al., 2026](https://arxiv.org/abs/2601.10387)) and of the PSM in general.

Some questions to answer:

- Which of these methods work best to prompt the assistant with an identity?
- Are these represented the same way in activation space?
- Does this change if it's in the system prompt or the user prompt?

**First Steps**

- Vary prompting method for different identities/traits and in the system/user prompt and see what differences there are in expressed behavior and representation space, across multiple turns
