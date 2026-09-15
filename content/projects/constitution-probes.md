---
title: Probing for violations of a whole constitution
status: Not started
order: 40
---

# Probing for violations of a whole constitution

[Constitutional Classifiers](https://www.anthropic.com/news/constitutional-classifiers) uses policy-derived examples for safety monitoring. [Constitutional Value Potentials](https://arxiv.org/abs/2606.15420) studies internal monitoring of conflicts among six predefined values, including combinations of value-specific scores. That is useful evidence, but it does not establish coverage of a broad constitution with entirely new principle families.

It seems important to test whether one activation monitor can detect a violation of any part of an entire constitution, without being told which rule is relevant for each example. It would also be useful to forecast the judge's eventual verdict before the violation is fully expressed.

- Distill a broad policy-aware judge into a shared monitor and compare it with separate rule probes.
- Hold out entire principle families and expand the constitution to test how coverage scales.
- Distinguish violations from quotation, harmless discussion and permitted exceptions.
- Forecast judgments before and throughout generation, measuring calibration and missed violations.
- Change the constitution and test whether the monitor follows the new rules rather than the model's usual preferences.
