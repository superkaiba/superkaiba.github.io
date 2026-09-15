---
title: Transferring capabilities and alignment through crosscoders
category: representations
status: Not started
order: 4
---

# Transferring capabilities and alignment through crosscoders

My work on [cross-architecture model diffing](https://arxiv.org/abs/2602.11729) uses crosscoders to identify meaningful differences between models. [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) isolates changes from narrow fine-tuning, while [model stitching](https://arxiv.org/abs/2506.06609) shows that probes and steering vectors can transfer through simple representation mappings.

It would be useful to test whether crosscoder features can transfer a capability or alignment-related behavior between models. Matching a representation is only a starting point: the recipient must use the transferred information in its own computation.

- Begin with controlled model pairs that differ in one known skill or behavioral tendency.
- Use shared features to translate interventions, comparing crosscoders with affine stitching and direct fine-tuning.
- Test whether an intervention supplies a missing capability, changes how an existing capability is used, or only changes output style.
- Measure transfer on unfamiliar tasks and prompts, together with side effects on unrelated abilities and safety behavior.
