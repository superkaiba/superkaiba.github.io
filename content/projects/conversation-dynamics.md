---
title: Predicting how conversations unfold
category: context-prediction
status: Not started
order: 3
---

# Predicting how conversations unfold

Our [context-to-answer mapping](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf) predicts a summary of one response. [Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) suggests that representations of conversation participants could help extend this to later turns. Anthropic's [Claude 4 system card](https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf) also describes recurring interaction patterns, including a “spiritual bliss” state in model self-interactions.

It would be useful to predict the next context representation, then ask how far such predictions can describe an unfolding conversation. Repeated conversational patterns might admit a dynamical explanation, but recurring text alone does not establish an attractor.

- Fit context-to-next-context maps and measure how errors accumulate over turns.
- Include a representation of the user when predicting human–assistant conversations.
- Compare conversations with other agents; test the hypothesis that their dynamics are more predictable.
- Perturb recurring conversational states and test recovery, stability and sensitivity to initial conditions.
