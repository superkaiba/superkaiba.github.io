---
id: "P10"
title: "Which concepts are linearly decodable?"
area: "Representations"
status: "Not started / seed"
intake: "To confirm"
status_checked: "2026-09-14"
source_title: "Characterizing the linear decodability of concepts from the residual stream"
---

# Which concepts are linearly decodable?

A lot of interpretability work relies on the idea that meaningful concepts can be read out with linear probes. The [linear representation hypothesis](https://arxiv.org/abs/2311.03658) helps formalize why this might work, but it does not mean that every concept will be equally easy to decode in every setting.

The goal of this project would be to characterize **what is linearly decodable, where, and under which conditions**. I would like to understand the pattern of successes and failures, rather than just finding a probe that performs well on one dataset.

[The Geometry of Truth](https://arxiv.org/abs/2310.06824) gives a concrete case of linear structure, while [Not All Language Model Features Are One-Dimensionally Linear](https://arxiv.org/abs/2405.14860) identifies richer feature geometry. [Amnesic Probing](https://arxiv.org/abs/2006.00995) motivates checking whether information that a probe can extract actually affects the model's behavior.

We could start with concepts that differ in useful ways: factual versus behavioral, local versus context-dependent, and simple attributes versus combinations of attributes.

Some questions:

- At which layers and token positions does each kind of information become accessible?
- Do concepts stay linearly decodable when the prompt format or task changes?
- When a nonlinear probe helps, what additional structure is it using?
- Does being easy to read out also make a concept easy to control through an intervention?
