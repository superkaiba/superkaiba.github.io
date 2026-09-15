# Can models learn to evade probes in context?

Probes are small classifiers that read a model's internal activations to detect a behavior of interest. They could be useful monitors, but only if the model cannot easily work around them. [Obfuscated Activations](https://arxiv.org/abs/2412.09565) shows that attacks can change activations enough to evade some internal defenses while preserving the behavior those defenses are meant to catch.

I want to understand whether a model can learn to do something similar **in context**, without changing its weights. For example, does telling the model that it is being monitored, or giving it feedback from a probe, help it find ways to avoid detection?

We would start with a fixed probe and a controlled task where we can independently measure the behavior. We would then check:

- Does detection get worse after the model receives information about the probe?
- Is the model still doing the same thing, or did it simply stop the behavior?
- Does evasion transfer to a new probe or a new task?
- How much information or feedback does the model need?
