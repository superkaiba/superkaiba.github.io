---
title: Recovering information from obfuscated chain-of-thought
status: Not started
order: 46
---

# Recovering information from obfuscated chain-of-thought

[Monitoring Reasoning Models for Misbehavior](https://arxiv.org/abs/2503.11926) shows that reasoning traces can help detect reward hacking, but strong optimization against a monitor can encourage models to hide relevant information in their chain-of-thought while continuing the behavior.

It seems important to test whether internal readouts retain useful access to information that has disappeared from readable reasoning. A decoder that produces a convincing explanation is insufficient: the recovered information should predict independently measured behavior and respond appropriately to controlled changes in what the model is doing.

- Compare text monitors and activation probes before and after reasoning becomes harder to monitor.
- Start with tasks whose hidden choices or intermediate variables are known, then move to less structured agent behavior.
- Test whether readouts recover those variables on new forms of obfuscation.
- Use interventions and counterfactual tasks to distinguish faithful information recovery from plausible reconstruction based on the prompt.
