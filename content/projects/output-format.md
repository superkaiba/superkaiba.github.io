---
title: How output format changes model behavior
status: Not started
order: 27
---

# How output format changes model behavior

[Chunky Post-Training](https://arxiv.org/abs/2602.05910) shows that formatting can activate unintended behaviors learned from post-training data. For example, LaTeX in a question can cue tool-use patterns rather than simply expressing the same mathematics differently. This raises a related question about the text the model itself generates: does writing in LaTeX, prose or code change its subsequent reasoning and behavior?

It would be useful to separate genuine changes in computation from changes in presentation. In particular, does asking for LaTeX make a model more logically consistent, or mainly select a familiar mathematical style?

- Solve matched reasoning problems in prose, LaTeX and structured formats, scoring the underlying answers with the same checker.
- Change input format and requested output format independently, while tracking token and compute costs.
- Compare representations before generation and after matched intermediate reasoning steps.
- Switch formats partway through a solution and test whether correctness, confidence or error recovery changes.
- Repeat across base and post-trained checkpoints to locate when any format dependence develops.
