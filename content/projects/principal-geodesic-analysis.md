---
title: Principal geodesic analysis of the residual stream
status: Not started
order: 16.6
---

# Principal geodesic analysis of the residual stream

**TL;DR:** Test whether principal geodesic analysis finds curved, behaviorally meaningful structure in residual-stream activations that linear PCA misses.

[Circular representations of weekdays and months](https://arxiv.org/abs/2405.14860) show that some language-model features have multidimensional structure. [Component analysis on CLIP's spherical embedding space](https://arxiv.org/abs/2305.14053) provides precedent for applying principal geodesic analysis (PGA) to model representations. More recently, [manifold steering](https://arxiv.org/abs/2605.05115) fits curved activation manifolds and tests their connection to behavior through interventions. These motivate testing PGA directly on an LLM's residual stream, without assuming that this application is novel or that its components will be interpretable.

The central question is which geometry to use. PGA on the full residual space with ordinary Euclidean distance reduces to PCA. Normalizing activations gives a sphere but discards magnitude, while learning a manifold introduces assumptions about its shape and metric. A useful result would show that a justified geometry captures a causal feature and improves interventions under matched controls.

**First Steps**

- Collect activations at a fixed layer and token position for a controlled task with suspected curvature, starting with cyclic concepts such as weekdays. Evaluate on held-out prompt templates.
- Compare ordinary PCA, PCA on normalized activations, local PCA, and PGA with matched dimensions and data. Separate improvements from normalization from those due to curved geometry, and retain activation norms when reconstructing interventions.
- Specify the manifold, distance metric, and fitting objective. Distinguish tangent-space PGA from exact PGA, and test sensitivity to the base point, sample size, and prompt distribution.
- Measure held-out reconstruction and behavioral prediction, then intervene along the recovered components. Match the intervention site and edited subspace across methods, and measure unrelated behavior and generation quality.
- Check where PGA fails: broad or multimodal data, unstable means, poor tangent-space approximations, and semantic curves that are not geodesics of the chosen manifold. High explained variance alone would not establish a mechanism.

This is a focused method comparison within [characterizing activation geometry with nonlinear factors](#activation-manifold), with possible applications to [nonlinear persona representations](#persona-manifolds).
