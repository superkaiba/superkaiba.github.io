---
title: First-person and third-person identity in prompts
category: personas
status: Not started
order: 5
---

# First-person and third-person identity in prompts

“You are a programmer,” “the assistant is a programmer” and “AIs are programmers” describe similar traits but attach them to different entities. Work on [entity binding](https://arxiv.org/abs/2310.17191) studies how language models connect attributes to the correct entity, while [the assistant as a privileged persona](https://arxiv.org/abs/2606.00545) motivates examining the assistant's special role.

It would be useful to understand which descriptions become statements about the model's own behavior and which remain information about another character. This could clarify why seemingly small changes in role prompts have different effects.

- Compare first-, second- and third-person formulations while holding the task and trait fixed.
- Identify how “I,” “you,” “the assistant” and “an AI” are represented across message roles.
- Vary whether a description appears in a system prompt, user message or quoted story.
- Intervene on candidate binding representations and test whether a trait transfers to the assistant's behavior.
