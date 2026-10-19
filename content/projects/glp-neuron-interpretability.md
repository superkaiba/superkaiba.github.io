---
title: Are GLP neurons broadly interpretable?
status: Not started
order: 10.2
---

# Are GLP neurons broadly interpretable?

[Generative Latent Prior (GLP)](https://arxiv.org/abs/2602.06964) learns to denoise language-model activations. Its internal neurons outperform SAE features and raw LLM neurons on single-feature probing across 113 classification tasks. However, that evaluation selects the best neuron for each predefined concept. It establishes that useful concept detectors exist, while leaving open how interpretable a typical GLP neuron is and whether its apparent meaning predicts its causal effects.

It would be useful to audit a representative sample of GLP neurons without selecting them for known concepts first. The goal is to measure how often neurons have clear, specific meanings, how well those meanings generalize, and whether interventions support them. The [released checkpoints and code](https://github.com/g-luo/generative_latent_prior) make this possible without training a new GLP.

- Sample neurons across GLP layers before inspecting their activations. Report the full score distribution and the fraction of inactive or poorly explained units, with uncertainty over the sample.
- Generate descriptions from activating examples, then test whether those descriptions predict activations on held-out text. Include medium and low activations, unrelated topics, and hard negative examples, rather than evaluating only the most activating passages.
- Compare with raw MLP neurons, SAE features, and random directions using the same text, explanation procedure, and evaluation budget. Separately repeat concept probing with matched candidate counts to test how much feature selection contributes to the advantage.
- Intervene on selected GLP neurons and measure changes in reconstructed activations and downstream LLM behavior. Use matched random-neuron and intervention-size controls. Distinguish control through the auxiliary GLP from evidence about the original LLM's mechanism.
- Check stability across diffusion noise levels, noise draws, datasets, and training checkpoints. Test whether improved diffusion loss predicts broader neuron interpretability as well as better best-neuron probing.

This connects to [semantic structure in native residual coordinates](#native-coordinates) and [characterizing activation geometry with nonlinear factors](#activation-manifold).
