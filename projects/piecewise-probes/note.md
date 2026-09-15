# What determines the right probe?

[Pareto Probing](https://aclanthology.org/2020.emnlp-main.254/) argues for evaluating probe accuracy together with complexity. [From Directions to Regions](https://arxiv.org/abs/2602.02464) shows how local subspaces can capture structure missed by isolated directions. Meanwhile, [production probes for Gemini](https://arxiv.org/abs/2601.11516) illustrate how architecture and training diversity affect robustness to long contexts and other deployment shifts.

It would be useful to predict which kind of probe a task needs from the geometry and distribution of its information, instead of choosing the most flexible probe by default.

- Compare linear, piecewise-linear, subspace-based and MLP probes, each with access to one layer or several layers.
- Measure data efficiency, calibration and accuracy at matched computational budgets, including simple and randomized-label controls.
- Test whether curvature, dimensionality or information spread across layers predicts which probe generalizes best.
- Evaluate unseen concepts, unfamiliar contexts and long conversations, distinguishing genuine robustness from fitting more closely to the training labels.
