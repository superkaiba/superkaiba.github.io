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

Several lines of work suggest that parts of LLM computation are more linear than we might expect. [Work on neural sentence trajectories](https://arxiv.org/abs/2311.04930) finds that token trajectories become straighter as they pass through trained language models. [Jump to Conclusions](https://arxiv.org/abs/2303.09435) studies linear transformations that approximate relationships between intermediate and final representations.

Other papers concern the geometry of concepts and models. [The Linear Representation Hypothesis](https://arxiv.org/abs/2311.03658) examines how concepts can be represented as directions, while [Transferring Linear Features Across Language Models](https://arxiv.org/abs/2506.06609) uses linear mappings between different models' representations.

These observations concern different kinds of linearity: across tokens, across layers, across concepts, and across models. The goal of this project would be to characterize their relationships and see whether they can help us build simple models of LLM behavior, generation, or training.

[Local Linearity of LLMs Enables Activation Steering via Model-Based Linear Optimal Control](https://arxiv.org/abs/2604.19018) already applies control theory to local approximations across layers. I would like to understand when similarly simple descriptions remain useful over longer computations and where they break down.

We would compare linear and nonlinear models on held-out data, test whether repeatedly applying a fitted map gives useful predictions, and check whether it predicts the effects of interventions. If a simple map captures enough of the relevant computation, we can apply tools from dynamical systems and other well-developed areas of mathematics.
