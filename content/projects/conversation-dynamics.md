---
title: Predicting how conversations unfold
status: Not started
order: 3
---

# Predicting how conversations unfold

My work on linear context-answer relationships studies answer prediction before generation. I have some results showing that a learned linear map from the final context token's activation can predict the mean activation across the answer's tokens. [Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) suggests that representations of conversation participants could help extend this to later turns. Anthropic's [Claude 4 system card](https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf) also describes recurring interaction patterns, including a “spiritual bliss” state in model self-interactions.

I have some results showing that you can predict the next context vector from the previous one.

It would be useful to understand how far such predictions can describe an unfolding conversation. Repeated conversational patterns might admit a dynamical explanation, but recurring text alone does not establish an attractor.

- Fit context-to-next-context maps and measure how errors accumulate over turns.
- Include a representation of the user when predicting human–assistant conversations.
- Compare conversations with other agents; test the hypothesis that their dynamics are more predictable.
- Perturb recurring conversational states and test recovery, stability and sensitivity to initial conditions.

<!-- Paper link temporarily hidden: [My recent paper on linear context-answer relationships](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) -->
