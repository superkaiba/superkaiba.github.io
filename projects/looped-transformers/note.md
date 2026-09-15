# Interpretability and safety of looped transformers

Looped transformers reuse a set of layers over multiple computation steps. This means a model can do more internal computation without having a different set of parameters for every step.

[Reasoning with Latent Thoughts](https://arxiv.org/abs/2502.17416) studies how this repeated computation can support reasoning. I am interested in what the model is doing internally as it goes around the loop, and what this means for interpretability and safety.

We would start with an openly available model and tasks where we can understand the intermediate computation. Then we could apply tools such as probes, activation patching, and feature analysis across loop iterations.

Some questions:

- Does each iteration refine the same representation, or carry out a qualitatively different operation?
- Can we identify when the model has finished the useful part of its computation?
- Do behavioral features persist, disappear, or become stronger as computation continues?
- Do interventions have to be applied once, or repeatedly across the loop?
- What can we observe when reasoning happens internally instead of in a visible chain-of-thought?
