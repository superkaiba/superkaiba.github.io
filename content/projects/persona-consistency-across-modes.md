---
title: How well does the model's persona hold up across thinking, doing, and talking?
status: Fleshed out
order: 20.5
aliases: [message-type-activations]
---

# How well does the model's persona hold up across thinking, doing, and talking?

We are seeing a remarkable degree of "split-brainedness" in modern LLMs, with the model saying, thinking, and doing contradictory things (stated values often diverge from value-informed actions: [Shen et al., 2025](https://arxiv.org/abs/2501.15463); CoTs often leave out what actually drives the answer: [Chen et al., 2025](https://arxiv.org/abs/2505.05410)), as well as acting differently in different contexts. This is not surprising given the different rewards used to train different parts of the model (RLHF for the talker, RLVR for the thinker/doer), and the fact that modern SOTA models are probably trained by distilling many specialized teachers into one model (e.g. multi-teacher on-policy distillation, used to train MiMo-V2-Flash: [Ma et al., 2026](https://arxiv.org/abs/2606.30406)) (we are literally distilling different brains into one).

The goal of this project would be to evaluate to what degree a model's character/persona is consistent across these different modes, and potentially develop methods to make it more consistent.

### Representations across prompts, reasoning, answers and tool calls

Work on [reasoning trajectories](https://arxiv.org/abs/2604.05655) and [internal tool-call signals](https://arxiv.org/abs/2605.09252) suggests that stages of a conversation can contain different information, and [The Talker Does Not Control The Doer](https://www.lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais) raises the possibility that verbal explanations and action selection should be studied separately. A first step toward measuring consistency across modes is to characterize how representations differ across system prompts, user messages, reasoning, answers and tool calls, separating differences caused by message role from differences in content, position or intended action.

- Put matched content in different message roles and compare its activations.
- Separate speaker identity and behavioral persona from the type of message being processed.
- Test whether probes and SAE features transfer between explanation, answer and tool-call states.
- Compare stated intentions with actual actions and intervene on candidate representations to test their relationship.
