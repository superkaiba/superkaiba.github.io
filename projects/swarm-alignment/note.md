# Do interacting agents develop aligned representation spaces?

[Linear feature transfer](https://arxiv.org/abs/2506.06609) shows that representations can be mapped between independently trained models. [StateBridge](https://arxiv.org/abs/2608.13317) explicitly aligns hidden states for latent communication, while work on [multi-agent annotation discussions](https://aclanthology.org/2025.blackboxnlp-1.12/) studies convergence in agents' outputs.

It would be useful to know whether ordinary interaction itself makes representation spaces more similar, and whether that similarity improves coordination or reduces useful diversity. Explicitly fitting an alignment map and observing natural convergence are different questions.

- Measure representational alignment before and after communication, including agents from different model families.
- Control for shared text, token positions, common conclusions and identical model weights using transcript replay.
- Track whether alignment predicts coordination, correlated mistakes or persona drift.
- Perturb candidate shared directions and test whether they causally affect team behavior.
