---
title: Base-model preferences
category: personas
status: Not started
order: 10
---

# Base-model preferences

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) distinguishes a pretrained model from the characters it can simulate. Meanwhile, [research on narrative preferences](https://arxiv.org/html/2510.02025v3) measures which story constraints language models choose when given explicit alternatives. These approaches suggest ways to ask what a base model tends to generate before an assistant role is imposed.

It would be useful to characterize stable tendencies in base-model story continuations, while separating the narrator’s framing, a character’s preferences and the model’s distribution over plausible text. A frequently generated outcome need not be something the model wants.

- Compare probabilities and sampled frequencies of matched story continuations with different outcomes or character choices.
- Vary narrator, genre and character goals while holding the underlying situation fixed.
- Test whether apparent preferences persist across paraphrases, unfamiliar settings and explicitly conflicting character preferences.
- Compare base and instruction-tuned checkpoints, then examine which internal changes accompany shifts in the continuation distribution.
