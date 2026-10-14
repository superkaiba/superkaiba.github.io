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

**Related work on SDF timing and side effects**

- [Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints](https://arxiv.org/abs/2610.00767) compares SDF across SFT, DPO, and RL checkpoints. Learning the SDF update on a base model and adding it to a post-trained model reduces damage to preference consistency and “reality drift,” where unrelated fictional entities are treated as real. In its Qwen3-14B experiments, direct SDF raises the measured probability that Harry Potter is real from 1% to 55%, and Tyrell Corporation from 3% to 53%. These are normalized completion probabilities across prompt variants, not spontaneous claim rates. [Section 3.1](https://arxiv.org/html/2610.00767#S3.SS1) gives the examples, and [Appendix A.2.3](https://arxiv.org/html/2610.00767#A1.SS2.SSS3) explains the measurement limits.
- [Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966) applies SDF separately to checkpoints from a capabilities-focused o3 RL run before safety training. Changing beliefs about what the grader rewards substantially changes downstream behavior, with stronger grader-following effects later in RL. This tests RL checkpoint → SDF → evaluation, rather than interleaving document updates with RL.
- [Alignment Faking in Large Language Models, Appendix H.5.1](https://arxiv.org/html/2412.14093) mixes 66M synthetic-document tokens with 128M trainable tokens of ordinary assistant transcripts. Alignment faking remains above 15% in that setup, showing that document-induced effects can survive mixed document and assistant-response training.
- [Practical Learnings from Synthetic Document Finetuning](https://www.lesswrong.com/posts/7zGgFPLaTXJwCJccB/practical-learnings-from-synthetic-document-finetuning) reports that SDF can disrupt response endings. Mixing in well-formatted assistant trajectories or applying a small amount of tool-use RL afterward helped. These practical observations motivate checking formatting and tool use alongside capability and alignment.

These studies inform the training order and controls, but do not establish that third-person rollout documents separate capability transfer from misalignment or settle how SDF should be interleaved with RL.

**Related projects:** [Localizing the assistant persona to an external module](#assistant-persona-module) tests an architectural separation of alignment and capabilities. [Contextualized pretraining](#contextualized-pretraining) studies how source attribution changes generalization.
