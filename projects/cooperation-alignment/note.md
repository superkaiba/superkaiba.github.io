# Does learning to cooperate improve broader alignment?

[Pedagogical Games](https://openreview.net/pdf?id=VyVxlnVp9L) reports that training language models on numerical public-goods games can reduce harmful actions in unrelated text adventures, while training on the Prisoner's Dilemma produces little or no transfer. This provides preliminary evidence that cooperation training can change behavior beyond the training game. [Beneficial trait RL](https://arxiv.org/abs/2606.24014) reports broader alignment improvements, but explicitly rewards several alignment traits, so it does not isolate the effect of learning to cooperate.

It would be useful to test whether rewarding a model for helping other agents and achieving joint goals improves honesty, reduces manipulation and reward hacking, and increases willingness to accept correction in unrelated settings. The central question is what generalizes from cooperation itself when these other behaviors are not directly rewarded during training.

- Train on public-goods and resource-sharing games, and compare with individual-reward training in the same environments. Include a control with similar amounts of RL training, data, and compute on unrelated tasks.
- Evaluate a broad set of alignment behaviors outside the training games, using independent benchmarks and behavioral checks. Measure cooperation separately so improved teamwork is not counted as evidence of broader alignment.
- Vary the environment, partners, and reward structure to distinguish learning to coordinate for mutual benefit from helping others at a cost. Test effects on outsiders, including whether cooperation encourages collusion or uncritical deference.
- Test whether any gains survive changes in incentives, unfamiliar partners, and subsequent fine-tuning. Check for capability losses and increased refusal alongside alignment improvements.
