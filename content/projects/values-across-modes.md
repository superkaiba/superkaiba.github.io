---
title: Shared representations across talking, thinking, and acting on values
status: Not started
order: 32.5
---

# Shared representations across talking, thinking, and acting on values

**TL;DR:** Test whether the same internal representations support discussing, reasoning about, and acting on a value—and whether probes and training transfer between these modes.

[The Talker Does Not Control The Doer](https://www.lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais) motivates separating verbal endorsement from action selection. [Your LLM, Your Style](https://arxiv.org/abs/2608.10703) studies behavioral control across decision, advice, and execution settings, providing close related work for comparisons across modes.

This project focuses on specific values and behaviors, such as honesty: is the representation involved in explaining honesty also involved in reasoning about an honest choice and taking an honest action? If the representations differ, can we characterize that difference and transfer readouts or training between them?

**First Steps**

- Construct matched tasks in which the model discusses, reasons about, or acts on the same value, controlling information, wording, and task difficulty.
- Train probes in one mode and test them in the others; compare direct transfer with learned mappings between representation spaces.
- Intervene on candidate representations to test their behavioral role rather than relying only on probe accuracy.
- Train a value or behavior in one mode and measure transfer to the others, including conditions with conflicting training signals.

**Related projects:** [Thinker, talker, and doer personas](#cot-persona) studies identity and goals across modes; [message-type representations](#message-type-activations) studies broader differences across conversation stages.
