---
title: Does reasoning change what a model believes about itself?
status: Not started
order: 36
---

# Does reasoning change what a model believes about itself?

[Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) finds internal representations of different agents' beliefs in social-reasoning tasks. [Work on chain-of-thought dynamics](https://aclanthology.org/2025.emnlp-main.1516/) shows that reasoning text can influence an answer even when it does not faithfully describe the computation behind it.

It seems important to ask whether generated reasoning also changes a model's representations of its own abilities, traits, or role. For example, does writing “I am bad at this task” change subsequent behavior, or simply repeat an already selected response pattern?

- Track representations and behavioral self-predictions before, during, and after reasoning.
- Compare self-generated statements with matched statements supplied by a user or attributed to another agent.
- Edit or remove self-descriptions while keeping task-relevant reasoning intact.
- Test whether resulting changes persist into later tasks and whether activation interventions reproduce them.
