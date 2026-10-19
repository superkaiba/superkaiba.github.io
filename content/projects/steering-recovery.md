---
title: What restores model behavior after activation steering?
status: Not started
order: 20.25
---

# What restores model behavior after activation steering?

**TL;DR:** Test when downstream computation restores a model's default assistant behavior after an activation intervention, when it restores a different persona supported by context, and which components cause that recovery.

[Explorations of Self-Repair in Language Models](https://proceedings.mlr.press/v235/rushing24a.html) shows that later computation can compensate for interventions on earlier components. [Tracing the Persona Circuit](https://proceedings.mlr.press/v306/qin26h.html) studies competition between character-specific signals and an assistant-like default. In refusal, [Beyond I'm Sorry, I Can't](https://ojs.aaai.org/index.php/AAAI/article/view/41119) finds that previously inactive features can become active after other refusal features are ablated. These results give concrete precedents for recovery and redundancy, so observing that steering weakens downstream would not by itself establish a new mechanism.

The question is whether a brief persona perturbation causes a selective corrective response. Does the model return toward its default assistant behavior, toward the persona supported by the prompt, or simply lose the injected signal? A falling projection could reflect normalization, a changing representation, or reconstruction from the unchanged prompt. During generation, the model's own text can also drive recovery, an alternative highlighted by [Endogenous Resistance to Activation Steering](https://arxiv.org/html/2602.06941v3).

**First Steps**

- **Measure recovery within one forward pass.** Apply a brief perturbation at one layer and token, then trace its effect through later layers while holding input tokens fixed. Use held-out, layer-specific persona readouts alongside final next-token predictions and controlled behavioral choices. A decrease along the original steering direction alone is not enough.
- **Test what the model returns to.** Compare a default-assistant context with a context that establishes a different, benign persona. Include random and non-persona semantic perturbations, matched for size and immediate effect where feasible. Test whether recovery depends on the perturbed trait and the persona selected by context.
- **Identify the components that cause correction.** Find downstream attention heads or MLPs whose outputs change in response to the perturbation. Hold candidate outputs at their clean-run values during the perturbed pass, then use complementary rescue interventions. Test whether these manipulations selectively remove or restore recovery without broadly damaging task performance. This separates a compensatory response from ordinary persona construction.
- **Separate network computation from text and cache effects.** After establishing a within-pass effect, compare fixed-prefix replay with free generation. Rebuild the key/value cache from identical text without steering to test whether later behavior depends on the edited activation history. Replay steered transcripts without intervention to measure what the wording alone reproduces.
- **Replicate the surviving effect.** Start with one small instruction-tuned model and benign persona contrasts, then test held-out prompts and a second model family. Compare relevant base and post-trained checkpoints as controls, without treating that comparison itself as a new contribution.

A useful result would identify a perturbation-dependent correction, explain which persona it restores, and show that intervening on the responsible components changes that recovery. If the effect reduces to generic attenuation or known persona competition, that would narrow the claim. This complements [personas as persistent features](#persistent-personas) by focusing on the cause and destination of recovery, and could inform [localizing the assistant persona to an external module](#assistant-persona-module).
