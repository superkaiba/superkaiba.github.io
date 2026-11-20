---
title: How and why do LLM activations correct themselves?
status: Draft (slop)
order: 10.15
math: true
aliases: [steering-recovery]
---

# How and why do LLM activations correct themselves?

**TL;DR:** Later layers often undo damage to earlier activations. They restore part of an ablated component's effect, shrink small perturbations, and erase weak steering. Test whether these are one mechanism, find the components that do the correcting, and work out why training produces it. The last section applies this to personas: after persona steering, what does the model return to?

**Self-repair after ablation.** When a layer or attention head is ablated, downstream components change their outputs and restore part of the lost logit ([McGrath et al.](https://arxiv.org/abs/2307.15771); [Rushing and Nanda](https://arxiv.org/abs/2402.15390)). Known contributors include backup heads, weaker erasure by late MLPs, and rescaling by the final LayerNorm. The amount of repair varies a lot across prompts.

**Plateaus around natural activations.** Small perturbations of a natural activation barely change the output, until a sharp boundary ([Janiak et al.](https://arxiv.org/abs/2409.17113)). These plateaus get sharper with model size and training. In GPT-2 Large, freezing the MLP outputs removes the plateaus, while freezing attention outputs has small effects ([Shinkle and Heimersheim](https://www.lesswrong.com/posts/WMfSbt7AAcJdHzysB/activation-plateaus-where-and-how-they-emerge)). [Ferreira da Silva and Heimersheim](https://arxiv.org/abs/2606.24964) find that feature directions hold up better than mixtures of them, which computation in superposition predicts. The effect is modest.

**Basins and steering.** [Finlayson et al.](https://arxiv.org/abs/2610.04183) find that natural activations sit in attracting basins separated by barriers. Synthetic activations often shrink in norm across layers. Strong steering moves an activation into another basin, where it stays. In belief-state steering, edits made in roughly the first third of layers get undone by later layers ([Balcells et al.](https://arxiv.org/abs/2609.17376)). Adjacent layers also partly cancel each other's contributions to the residual stream ([Patrawala et al.](https://arxiv.org/abs/2609.07876)).

**Why does this happen?** The causes are unclear. Dropout was proposed early, but McGrath et al. found strong self-repair in a model trained without dropout. Theory on computation in superposition says interference between features grows with depth unless the network corrects it ([Hänni et al.](https://arxiv.org/abs/2408.05451)). That would make error correction necessary. Simpler accounts may also fit the plateau data, so the evidence for this theory is still weak.

One hypothesis connects all of these. The forward pass may contain standing negative feedback that pulls activations back toward typical values. That one mechanism would produce repair after ablation, shrinking of small perturbations, and reversal of weak early steering. This is my guess, and it makes testable predictions.

**Setup.** Perturb the activation $h_\ell$ at layer $\ell$ by $\epsilon v$, where $v$ is a unit direction and $\epsilon$ the size. For each later layer $m > \ell$, measure the gain

$$
g_m(\epsilon, v) = \frac{\lVert h_m(h_\ell + \epsilon v) - h_m(h_\ell) \rVert}{\epsilon}.
$$

If $g_m$ falls as $m$ grows, the perturbation is being corrected. Negative feedback predicts that $g_m$ stays roughly constant in $\epsilon$ below a threshold and jumps above it, where the activation crosses into another basin. Comparing $g_m$ along feature, steering and random directions shows which directions get corrected.

**Initial directions:**

- **Measure all three effects on one model.** Use one intervention type for ablation self-repair, perturbation shrinkage and steering reversal. Check whether the same components drive all three.
- **Find the correcting components.** Freeze candidate MLP or attention outputs at their clean values during the perturbed pass. Check which ones remove the correction.
- **Sweep the perturbation size.** Plot $g_m$ against $\epsilon$ for many directions. Look for a threshold, and check whether it matches the plateau boundary.
- **Test natural and synthetic activations.** Patch in SAE reconstructions or activations from another prompt. Track layer by layer whether they move back toward the set of natural activations.
- **Follow correction over training.** Measure it on Pythia or OLMo checkpoints. Compare models trained with and without dropout at matched loss.

## Recovery of personas after steering

The same question matters for personas. After a brief persona perturbation, does the model return to its default assistant behavior, return to the persona the prompt supports, or simply lose the injected signal? [Tracing the Persona Circuit](https://proceedings.mlr.press/v306/qin26h.html) studies competition between character-specific signals and an assistant-like default. In refusal, [Beyond I'm Sorry, I Can't](https://ojs.aaai.org/index.php/AAAI/article/view/41119) finds that previously inactive features can become active after other refusal features are ablated. These results are precedents for recovery, so a steering effect that weakens downstream would not by itself show a new mechanism.

A falling projection on the steering direction could reflect normalization, a changing representation, or reconstruction from the unchanged prompt. During generation, the model's own text can also drive recovery, as in [Endogenous Resistance to Activation Steering](https://arxiv.org/abs/2602.06941).

- **Measure recovery within one forward pass.** Apply a brief perturbation at one layer and token, then trace it through later layers with the input tokens fixed. Use held-out, layer-specific persona readouts alongside next-token predictions and controlled behavioral choices. A drop along the steering direction alone is not enough.
- **Test what the model returns to.** Compare a default-assistant context with a context that sets up a different, benign persona. Include random and non-persona perturbations, matched for size and immediate effect where feasible. Check whether recovery depends on the perturbed trait and on the persona the context selects.
- **Find the components that cause recovery.** Find downstream heads or MLPs whose outputs change in response to the perturbation. Hold them at clean-run values during the perturbed pass, then run complementary rescue interventions. Check that these selectively remove or restore recovery without broadly damaging the task.
- **Separate network computation from text and cache effects.** Compare fixed-prefix replay with free generation. Rebuild the key/value cache from identical text without steering, to test whether later behavior depends on the edited activations. Replay steered transcripts without intervention to measure what the wording alone reproduces.
- **Replicate what survives.** Start with one small instruction-tuned model and benign persona contrasts, then test held-out prompts and a second model family. Use base and post-trained checkpoints as controls.

A useful result would show a perturbation-dependent correction, say which persona it restores, and show that intervening on the responsible components changes the recovery. If the effect reduces to generic attenuation or known persona competition, that would narrow the claim.

**Related projects:** [LLM neuroanatomy](#llm-neuroanatomy), [understanding the general structure of the residual stream](#residual-stream-structure), [personas as persistent features](#persistent-personas), and [localizing the assistant persona to an external module](#assistant-persona-module).
