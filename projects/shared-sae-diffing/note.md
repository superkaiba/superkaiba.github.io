# Using a shared SAE for model diffing

[Crosscoders](https://transformer-circuits.pub/2024/crosscoders/index.html) learn shared sparse features across models. My work on [Delta-Crosscoder](https://arxiv.org/abs/2603.04426) shows why narrow fine-tuning changes need particular care, while [model stitching](https://arxiv.org/abs/2506.06609) provides a way to align representation spaces and transfer sparse autoencoders. This raises a practical question about how much machinery is needed to compare models reliably.

It would be useful to test when one shared SAE—a sparse autoencoder trained to describe both models—provides a clear account of their differences, and when it misses changes that a crosscoder can detect.

- Train a shared dictionary on matched activations from a base model and several controlled fine-tunes.
- Compare joint training, a frozen dictionary transferred between models, and crosscoder baselines.
- Separate changes in feature frequency or strength from genuinely new behavior and reconstruction errors.
- Test whether the identified differences predict behavioral changes and survive feature ablation or activation patching.
