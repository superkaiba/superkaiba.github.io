# How does chat format recruit an assistant persona?

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) proposes that post-training refines a persona supported by a model’s pretrained ability to simulate characters. [Chat templates](https://huggingface.co/docs/transformers/chat_templating) provide the concrete text and delimiters that assign conversational roles, and these formats vary across models. My hypothesis is that some of their effect comes from recruiting familiar dialogue patterns and personas learned during pretraining.

It would be useful to determine how much the assistant role depends on the meaning of its label, the surrounding format and associations learned during post-training.

- Compare plain-text dialogue labels with each model’s native chat header in matched base and instruction-tuned checkpoints.
- Replace role names, change delimiters and swap speaker assignments independently, measuring behavior and role representations.
- Test whether helpful-assistant behavior transfers to unfamiliar role labels when the surrounding dialogue provides the same evidence.
- Track what changes after small, controlled fine-tunes on alternative dialogue formats.

The role label, special boundary tokens and complete header would be treated as separate interventions.
