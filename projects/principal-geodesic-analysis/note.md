# Curved activation geometry: principal geodesics and how smoothly behavior changes along natural paths

**TL;DR:** Find curved, behaviorally meaningful structure in residual-stream activations with principal geodesic analysis (PGA), then use paths that follow this natural geometry to test whether small changes to internal representations can still cause large behavior changes, and which features act as gradual controls or sharp switches.

[Circular representations of weekdays and months](https://arxiv.org/abs/2405.14860) show that some language-model features have multidimensional, curved structure, and [manifold steering](https://arxiv.org/abs/2605.05115) fits curved activation manifolds and tests their connection to behavior through interventions. Work on [activation plateaus](https://www.lesswrong.com/posts/WMfSbt7AAcJdHzysB/activation-plateaus-where-and-how-they-emerge) finds both gradual responses and flat regions separated by sharp transitions when interpolating between activations, and [steering-strength analysis](https://arxiv.org/abs/2602.02712) studies how concept expression changes as a fixed steering vector is scaled. These experiments use fixed directions or prescribed interpolation paths, so a sharp response could reflect a meaningful behavioral boundary, an excursion away from familiar activation regions, or both.

### Finding the curved directions with principal geodesic analysis

[Component analysis on CLIP's spherical embedding space](https://arxiv.org/abs/2305.14053) provides precedent for applying PGA to model representations. The central question is which geometry to use. PGA on the full residual space with ordinary Euclidean distance reduces to PCA. Normalizing activations gives a sphere but discards magnitude, while learning a manifold introduces assumptions about its shape and metric. A useful result would show that a justified geometry captures a causal feature and improves interventions under matched controls.

- Collect activations at a fixed layer and token position for a controlled task with suspected curvature, starting with cyclic concepts such as weekdays, and evaluate on held-out prompt templates.
- Compare ordinary PCA, PCA on normalized activations, local PCA, and PGA with matched dimensions and data. Separate improvements from normalization from those due to curved geometry, and distinguish tangent-space PGA from exact PGA.
- Check where PGA fails: broad or multimodal data, unstable means, poor tangent-space approximations, and semantic curves that are not geodesics of the chosen manifold. High explained variance alone would not establish a mechanism.

### How smoothly does behavior change along natural paths?

The recovered geodesics give curved paths that stay near natural activations. Continuity here means practical sensitivity to finite changes, rather than a claim of mathematical discontinuity in a dense transformer's outputs.

- Compare fixed-direction steering, spherical interpolation, PGA geodesics and curved paths learned from naturally occurring activations. Match endpoints, report path length, and measure local response per unit distance so a longer path does not automatically appear smoother.
- Check whether intermediate states resemble held-out natural activations and preserve task performance, treating this as evidence about path quality rather than proof of the true manifold.
- Measure downstream activation changes, output-distribution changes and behavioral outcomes separately, using repeated generations to distinguish internal sensitivity from a small probability change that flips a decoded token.
- Compare transition sharpness across features, prompts, layers and models, and test whether following natural geometry makes steering more predictable and selective.

**Related projects:** [characterizing activation geometry with nonlinear factors](#activation-manifold) and [nonlinear geometry of persona representations](#persona-manifolds).
