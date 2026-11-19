---
title: How much of an LLM's persona comes from the context and how much from the weights?
status: Draft (slop)
order: 5.5
math: true
---

# How much of an LLM's persona comes from the context and how much from the weights?

**TL;DR:** Split the persona a model expresses into the part set by its weights and the part set by its context (system prompt, user messages, conversation history). Measure the split in behavior and in activation space, then map how it changes with post-training, model size, conversation length and trait.

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) views post-training as selecting a persona from those the model learned in pretraining, and the context keeps selecting among personas at inference time. Both levers clearly matter. A system prompt or role-play request can move a model's persona a lot, persona traits can be read and steered along [persona vectors](https://arxiv.org/abs/2507.21509), and models can drift away from the default assistant along the [Assistant Axis](https://arxiv.org/abs/2601.10387) during a conversation. A long enough context can even override trained behavior, as in [many-shot jailbreaking](https://www.anthropic.com/research/many-shot-jailbreaking). As far as I can tell, nobody has measured how the expressed persona divides between the two sources across ordinary use.

**A behavioral split.** Pick a trait (for example sycophancy, honesty or warmth) and a score $s_{m,x}$ for how strongly model checkpoint $m$ expresses it given context $x$, using a judge score or a persona-vector projection. Across a set of checkpoints and a set of contexts, decompose

$$
s_{m,x} = \mu + a_m + b_x + c_{m,x} + \varepsilon,
$$

where $a_m$ is the part set by the weights, $b_x$ the part set by the context, and $c_{m,x}$ their interaction (how much a given context moves a given model). The share of variance explained by each term is the weights share, the context share and the interaction share for that trait.

**A mechanistic split.** At the last context position, project the residual stream onto a persona vector or the Assistant Axis. Split the projection into contributions that reach it only through computation at that position and contributions that pass through attention to earlier positions, following both to the persona direction with layer norms and MLPs linearized. The second kind is the mechanistic context share of the persona.

**Initial directions:**

- **Default vs prompted persona.** Measure trait scores across many system prompts, user styles and conversation histories, for several models, and fit the decomposition above.
- **Which traits are fixed.** Compare refusals and stated values with personality traits and style. My guess is that values are the most weight-driven and style the most context-driven.
- **Conversation length.** Track the context share as conversations get longer, to see whether the context gradually takes over from the weights.
- **Post-training.** Compare base and chat checkpoints and the stages in between, to see whether post-training mainly raises the weights share (a more fixed assistant) or changes how the model responds to context.
- **By layer.** Track the mechanistic context share of persona directions layer by layer.

**Related projects:** [predicting answer activations from context](#answer-activations), [personas as persistent features](#persistent-personas), [first-, second-, and third-person identity in prompts](#first-third-person) and [persona selection as Bayesian inference](#bayesian-personas).
