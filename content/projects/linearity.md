---
id: "P19"
title: "How linear are LLM representations?"
area: "Representations"
status: "Not started / proposal"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Exploring Linearity in LLMs"
---

# How linear are LLM representations?

There is a lot of literature suggesting that parts of LLM computation are more linear than we might expect:

- [Neural sentence trajectories](https://arxiv.org/pdf/2311.04930) become straighter as they pass through trained language models.
- [Jump to Conclusions](http://arxiv.org/html/2303.09435v2) studies linear transformations that approximate the relationship between intermediate and final representations.
- [The Linear Representation Hypothesis](https://arxiv.org/abs/2311.03658) examines how concepts can be represented as directions.
- [Transferring Linear Features Across Language Models](https://arxiv.org/pdf/2506.06609) studies linear mappings between different models' representations.

These are related observations, but they concern different kinds of linearity: across tokens, across layers, across concepts, and across models.

The goal of this project would be to characterize these relationships and see whether they can help us build simple models of LLM behavior, generation, or training. If we can describe part of the computation with a linear map, we can bring in tools from dynamical systems and other well-developed areas of mathematics.
