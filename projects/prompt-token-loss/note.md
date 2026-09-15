# What changes when models learn to predict user turns?

[Instruction Fine-Tuning: Does Prompt Loss Matter?](https://arxiv.org/html/2401.13586v4) already studies how weighting prompt tokens changes fine-tuning outcomes. [Flipping the Dialogue](https://arxiv.org/abs/2510.06552) trains models specifically to produce user turns. These establish that learning to predict the user is a concrete training choice, alongside learning to answer the user.

It would be useful to understand what this choice changes internally: does it improve the model’s representation of the user, change its representation of itself as the assistant, or blur the distinction between the two roles?

- Fine-tune identical starting checkpoints with assistant-only, user-only and mixed-turn losses on the same conversations.
- Vary the user-loss weight and control both processed tokens and the amount of assistant-target supervision.
- Measure user prediction, instruction following, role adherence and responses to questions about the model’s own behavior.
- Compare self, user and assistant-role representations across checkpoints, using interventions to test which changes affect behavior.
- Check whether any gains survive new users, dialogue formats and topics.
