---
title: Semantic structure in native residual coordinates
status: Not started
order: 10
---

# Semantic structure in native residual coordinates

[Dimension-selection probes](https://aclanthology.org/2020.emnlp-main.15/) find linguistic information concentrated in subsets of embedding coordinates. Work on [privileged residual-stream bases](https://transformer-circuits.pub/2023/privileged-basis/index.html) also shows that a model's original coordinate system is not always arbitrary in practice. However, [analyses of individual neurons](https://belinkov.com/assets/pdf/iclr2022.pdf) caution that information recoverable from a coordinate need not be information the model uses.

It would be useful to determine when individual residual-stream coordinates encode stable concepts, and what training dynamics or computations create that alignment.

- Compare native coordinates with random rotations and learned alternative bases on held-out semantic tasks.
- Control for token frequency, position, activation magnitude and normalization before assigning semantic interpretations.
- Test whether coordinate interventions change the corresponding behavior, separating readout accuracy from causal importance.
- Track promising coordinates across training checkpoints and optimizer choices to see how semantic alignment develops or disappears.
