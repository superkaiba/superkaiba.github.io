# Understanding the general structure of the residual stream

**TL;DR:** Build a general picture of how the residual stream is organized: whether its native coordinates mean anything, where its structure is curved instead of linear, and how smoothly behavior changes as activations move through it.

Most interpretability tools assume a particular structure for the residual stream: linear directions for probes and steering, a sparse dictionary for SAEs, or an arbitrary basis that only rotations make meaningful. Each assumption holds in some cases and fails in others. This project tries to map which kinds of structure the residual stream actually has, using three complementary angles.

### Is the native basis meaningful?

[Dimension-selection probes](https://aclanthology.org/2020.emnlp-main.15/) find linguistic information concentrated in subsets of embedding coordinates, and work on [privileged residual-stream bases](https://transformer-circuits.pub/2023/privileged-basis/index.html) shows that a model's original coordinate system is not always arbitrary in practice. However, [analyses of individual neurons](https://belinkov.com/assets/pdf/iclr2022.pdf) caution that information recoverable from a coordinate need not be information the model uses. It would be useful to determine when individual residual-stream coordinates encode stable concepts, and what training dynamics or computations create that alignment.

- Compare native coordinates with random rotations and learned alternative bases on held-out semantic tasks.
- Control for token frequency, position, activation magnitude and normalization before assigning semantic interpretations.
- Test whether coordinate interventions change the corresponding behavior, separating readout accuracy from causal importance.
- Track promising coordinates across training checkpoints and optimizer choices to see how semantic alignment develops or disappears.

### Where is the structure curved?

[Circular representations of weekdays and months](https://arxiv.org/abs/2405.14860) show that some features have multidimensional, curved structure, and [manifold steering](https://arxiv.org/abs/2605.05115) fits curved activation manifolds and tests their connection to behavior through interventions. Principal geodesic analysis (PGA) is a direct way to look for this kind of structure ([component analysis on CLIP's spherical embedding space](https://arxiv.org/abs/2305.14053) is a precedent). The central question is which geometry to use. PGA on the full residual space with ordinary Euclidean distance reduces to PCA. Normalizing activations gives a sphere but discards magnitude, while learning a manifold introduces assumptions about its shape and metric.

- Collect activations at a fixed layer and token position for a controlled task with suspected curvature, starting with cyclic concepts such as weekdays, and evaluate on held-out prompt templates.
- Compare ordinary PCA, PCA on normalized activations, local PCA, and PGA with matched dimensions and data. Separate improvements from normalization from those due to curved geometry, and distinguish tangent-space PGA from exact PGA.
- Check where PGA fails: broad or multimodal data, unstable means, poor tangent-space approximations, and semantic curves that are not geodesics of the chosen manifold. High explained variance alone would not establish a mechanism.

### How smoothly does behavior change along natural paths?

Work on [activation plateaus](https://www.lesswrong.com/posts/WMfSbt7AAcJdHzysB/activation-plateaus-where-and-how-they-emerge) finds both gradual responses and flat regions separated by sharp transitions when interpolating between activations, and [steering-strength analysis](https://arxiv.org/abs/2602.02712) studies how concept expression changes as a fixed steering vector is scaled. These use fixed directions or prescribed interpolation paths, so a sharp response could reflect a meaningful behavioral boundary, an excursion away from familiar activation regions, or both. The curved paths found above stay near natural activations, which makes it possible to tell these apart. Continuity here means practical sensitivity to finite changes, rather than a claim of mathematical discontinuity in a dense transformer's outputs.

- Compare fixed-direction steering, spherical interpolation, PGA geodesics and curved paths learned from naturally occurring activations. Match endpoints, report path length, and measure local response per unit distance so a longer path does not automatically appear smoother.
- Check whether intermediate states resemble held-out natural activations and preserve task performance, treating this as evidence about path quality rather than proof of the true manifold.
- Measure downstream activation changes, output-distribution changes and behavioral outcomes separately, using repeated generations to distinguish internal sensitivity from a small probability change that flips a decoded token.
- Compare transition sharpness across features, prompts, layers and models, and test whether following natural geometry makes steering more predictable and selective.

**Related projects:** [how linear are LLM representations?](#linearity), [characterizing activation geometry with nonlinear factors](#activation-manifold), [nonlinear geometry of persona representations](#persona-manifolds), and [are SAE features sparse in the neuron basis?](#sae-neuron-sparsity)
