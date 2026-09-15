---
id: "P15"
title: "Self-reflection to reduce reward hacking"
area: "Training"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Self-reflection to prevent reward hacking"
---

# Self-reflection to reduce reward hacking

Using coding agents often reveals a frustrating failure mode: an agent gets blocked, does something that was not what you asked for, and only tells you about it much later.

Often, if you catch it and ask something like “is this what I asked you to do?”, it recognizes the problem and corrects course. This suggests that the model can sometimes recognize the failure when prompted to reconsider.

The [Teaching Claude Why](https://www.anthropic.com/research/teaching-claude-why) post also suggests that teaching models **why** an action is wrong can be more effective than demonstrations alone.

I propose to apply a related idea in reinforcement learning. Monitoring every trajectory is expensive, but periodically inserting something like “Stop. Think. Is this what the task was intended for?” should be relatively feasible.

We would then check:

- Does this reduce reward hacking?
- Does it reduce task performance?
- How often do we need to insert the reflection?
- Does the model actually change its actions, or just learn to produce reassuring explanations?

We could also compare reflection during training with reflection introduced only at evaluation time.
