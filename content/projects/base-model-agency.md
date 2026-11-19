---
title: Agency in base models, "contaminated" base models, and post-trained models without a chat template
status: Fleshed out
order: 28.1
aliases: [base-model-preferences]
---

# Agency in base models, "contaminated" base models, and post-trained models without a chat template

The goal of this project would be to evaluate the level of agency that can be ascribed to a base model (this probably needs some input from the agent foundations people as to how to define "agency", e.g. agents as systems that would adapt their policy if their actions influenced the world in a different way: [Kenton et al., 2022](https://arxiv.org/abs/2208.08345)) as well as how this changes when we add chat template data to pretraining/midtraining (base models already refuse harmful requests through the same refusal direction as chat models: [Kissane et al., 2024](https://www.lesswrong.com/posts/YWo2cKJgL7Lg8xWjj/base-llms-refuse-too); the Assistant Axis is already present in base models: [Lu et al., 2026](https://arxiv.org/abs/2601.10387)).

### Base-model preferences

One concrete handle on this is whether a base model has stable preferences of its own. The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) distinguishes a pretrained model from the characters it can simulate, and [research on narrative preferences](https://arxiv.org/html/2510.02025v3) measures which story constraints language models choose when given explicit alternatives. It would be useful to characterize stable tendencies in base-model story continuations, while separating the narrator's framing, a character's preferences and the model's distribution over plausible text. A frequently generated outcome need not be something the model wants.

- Compare probabilities and sampled frequencies of matched story continuations with different outcomes or character choices.
- Vary narrator, genre and character goals while holding the underlying situation fixed.
- Test whether apparent preferences persist across paraphrases, unfamiliar settings and explicitly conflicting character preferences.
- Compare base and instruction-tuned checkpoints, then examine which internal changes accompany shifts in the continuation distribution.

A related baseline is BOS-only sampling: give the model only the beginning-of-sequence token and sample, to see what it generates before any role is imposed. The most likely BOS-only document differs a lot across models (Llama 3 8B base gives a math question-answer pair, Mistral base a travel listicle: [Millidge, 2024](https://www.beren.io/2024-05-12-The-Unconditioned-Distribution-of-Current-Open-LLMs/)), and alignment tuning sharply lowers the entropy of generations by selecting low-entropy paths that already exist in the base model ([Yang & Holtzman, 2025](https://arxiv.org/abs/2506.17871)). My guess is that SFT adds a sharp distribution tied to the chat template, while most of the BOS-only distribution survives, with some assistant style leaking into the tail. I haven't found a direct test of this: one base model and its own SFT checkpoint, sampled from BOS, with the divergence between them tracked over SFT steps. OLMo 2 releases base, SFT, DPO and RLVR checkpoints along with its training data, which would make the comparison cheap. One caveat is that base models can already contain instruction-style data from pretraining, so the base side may not be a clean control (which is the "contaminated" case above).

**Related projects:** [What latent does the assistant chat template select?](#pretraining-role) studies what the chat template selects in base and post-trained checkpoints.
