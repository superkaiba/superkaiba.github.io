# Continued third-person training to separate capability gains from misalignment

**TL;DR:** Turn reinforcement-learning rollouts into third-person documents about another agent, then test whether synthetic document finetuning transfers the capabilities without transferring unwanted behavior to the assistant.

[Natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) shows that learning to exploit rewards in realistic RL environments can produce broader misalignment. [Synthetic document finetuning](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/) offers a way to train models on information presented in documents. The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) motivates asking which persona the model associates with the behavior in that training data.

This project asks whether we can separate the capabilities learned from an RL rollout from the unwanted behavior learned about the assistant. After sampling and evaluating a rollout, rewrite it as a third-person document about another agent acting in the environment. Continue training on these documents using synthetic document finetuning (SDF), then evaluate the model in its usual assistant role.

My hypothesis is that the model could learn the capabilities and knowledge demonstrated in the rollout without treating the other agent's reward hacking or other unwanted behavior as part of the assistant's character. This depends on capabilities transferring between personas more readily than unwanted behavior. In particular, the idea assumes that the assistant can use capabilities the model learns while simulating other agents. That transfer needs to be measured.

**First Steps**

- Start with an RL task where training improves a capability but also produces reward hacking or broader misalignment.
- Compare ordinary RL with training on third-person documents made from the rollouts. Include a first-person document condition to separate the effect of narrative perspective from the change in training objective.
- Measure legitimate capability gains, reward hacking, and alignment on held-out tasks in the assistant role, matching training budgets and rollout information where possible.
- Test whether unwanted behavior stays associated with the other agent or transfers to the assistant, including after further capability training.

**Exploratory variant: an "evil twin" persona**

Use SDF to describe an aligned assistant and a misaligned "evil twin" as equally capable. Then apply reinforcement learning with verifiable rewards (RLVR) in the evil twin's persona and test whether the resulting capability gains transfer to the assistant while the unwanted behavior remains confined to the twin. Equal capability is part of the proposed training setup, not evidence that this separation will work.

**Related projects:** [Localizing the assistant persona to an external module](#assistant-persona-module) tests an architectural separation of alignment and capabilities. [Contextualized pretraining](#contextualized-pretraining) studies how source attribution changes generalization.
