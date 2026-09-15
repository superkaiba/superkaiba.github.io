---
title: Connecting trajectory straightening with belief-state geometry
status: Not started
order: 18
---

# Connecting trajectory straightening with belief-state geometry

Work on [neural sentence trajectories](https://arxiv.org/abs/2311.04930) finds that token trajectories become straighter across layers of trained language models. Separately, [belief-state geometry](https://arxiv.org/abs/2405.15943) and [constrained Bayesian updates](https://arxiv.org/abs/2502.01954) connect activation structure to uncertainty about the process generating the text. These are different observations; neither alone explains how trajectory curvature relates to belief changes.

It would be useful to test whether straightening reflects a simpler representation of belief dynamics, and identify when that interpretation fails.

- Measure token-trajectory curvature and decoded belief changes together in models trained on known latent processes.
- Vary uncertainty, surprising observations and hidden-state transitions while controlling token statistics.
- Compare curvature in activation space, decoded probability space and representations of log probabilities.
- Test whether interventions that alter belief updating also alter straightening and predictive performance, before extending the analysis to natural language.
