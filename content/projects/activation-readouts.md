---
title: Comparing tools for reading activations
status: Not started
order: 12
---

# Comparing tools for reading activations

The [tuned lens](https://arxiv.org/abs/2303.08112) turns intermediate activations into token predictions. [Natural-language autoencoders](https://transformer-circuits.pub/2026/nla/) learn textual explanations through a reconstruction objective, while [activation oracles](https://alignment.anthropic.com/2025/activation-oracles) answer questions about internal states. These tools offer different kinds of readout, making it useful to evaluate what each actually reveals about the same computation.

It would be useful to compare their accuracy, cost and causal usefulness on shared tasks, rather than judging explanations only by how plausible they sound.

- Compare SAEs, R Lens, J Lens, the tuned lens, answer predictors, natural-language autoencoders and activation oracles on matched activations.
- Include tasks with known hidden variables and predictions about future answers, withholding information that would reveal the answer directly.
- Test whether each readout predicts the effects of controlled activation interventions.
- Measure performance across layers and models alongside data requirements, runtime and explanation stability.
