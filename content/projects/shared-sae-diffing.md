---
title: Applying SharedSAE to model diffing
status: Not started
order: 17
---

# Applying SharedSAE to model diffing

[SharedSAE: One Feature Dictionary Across Language Models](https://arxiv.org/abs/2609.04344) introduces a shared dictionary of sparse features with model-specific encoders and decoders. The paper shows that these features and their descriptions can transfer across models, and that new models can be adapted to a frozen dictionary.

It would be useful to apply SharedSAE to model diffing: can its shared features reveal what changes between a base model and its fine-tuned versions? [Crosscoders](https://transformer-circuits.pub/2024/crosscoders/index.html) and my work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) provide comparison methods for identifying changes introduced by fine-tuning.

- Apply SharedSAE to a base model and several controlled fine-tunes using matched inputs.
- Compare joint dictionary training with freezing the dictionary before adapting the fine-tuned checkpoints.
- Separate changes in feature frequency or strength from genuinely new behavior and reconstruction errors.
- Compare with crosscoder baselines, and test whether the identified differences predict behavioral changes using feature ablation or activation patching.
