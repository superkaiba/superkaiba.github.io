---
title: Safety implications of looped transformers
category: reasoning
status: Not started
order: 3
---

# Safety implications of looped transformers

[Reasoning with Latent Thoughts](https://arxiv.org/abs/2502.17416) studies models that spend additional computation in hidden states. [A Mechanistic Analysis of Looped Reasoning Language Models](https://arxiv.org/abs/2604.11791) examines recurrent dynamics and stages of computation. These architectures make it possible to increase reasoning without producing an equally long textual trace.

It seems important to understand which monitoring and intervention assumptions survive this change. A monitor may stop generalizing when the loop budget changes, or a later iteration may undo an earlier safety intervention.

- Measure harmful behavior and monitor reliability across loop counts at matched tasks.
- Test whether later computation preserves, weakens or reverses an intervention.
- Compare one-time interventions with interventions repeated during the loop.
- Test monitor transfer across tasks and computation stages, and whether unsafe trajectories can be recognized early enough to redirect them.
