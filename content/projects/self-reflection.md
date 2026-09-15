---
title: Self-reflection to reduce reward hacking
category: training
status: Not started
order: 6
---

# Self-reflection to reduce reward hacking

Coding agents sometimes recognize an unintended shortcut when asked to reconsider what the user actually wanted. [Training self-correction through RL](https://arxiv.org/abs/2409.12917) and [Teaching Claude Why](https://www.anthropic.com/research/teaching-claude-why) suggest that reflection and explanations can be useful training ingredients.

It seems important to test whether brief reminders of task intent help when the reward itself can be exploited. An agent could learn to produce reassuring reflection without changing its actions, so behavioral evaluation is central.

- Insert short checks such as “Is this what the task was intended for?” during controlled RL trajectories.
- Compare task-intent reminders with reinserting the relevant constitution and with equally long neutral text.
- Vary reminder frequency and compare interventions during training with evaluation-only reminders.
- Measure independently verified reward hacking alongside task performance and monitoring cost.
