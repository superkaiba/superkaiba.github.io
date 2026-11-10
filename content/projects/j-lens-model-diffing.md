---
title: The J-lens as a model diffing tool in activation space
status: Not started
order: 17.5
math: true
---

# The J-lens as a model diffing tool in activation space

**TL;DR:** Run a base model and its fine-tuned version on the same text, take the difference in their activations at each layer, and read that difference with the J-lens instead of the logit lens. Check whether this finds the fine-tuning objective in earlier layers and in subtler fine-tunes than current activation-difference methods.

[Minder et al.](https://arxiv.org/abs/2510.13900) show that narrow fine-tuning leaves readable traces. They average the activation difference between the fine-tuned and base model over the first few tokens of unrelated web text, and read it with Patchscope and the logit lens (the Activation Difference Lens). The tokens they find often name the fine-tuning domain, and steering with the difference produces text like the fine-tuning data. The logit lens is known to work poorly in early and middle layers, and Patchscope depends on a choice of target prompt. The [J-lens](https://www.transformer-circuits.pub/2026/workspace/index.html) corrects the logit lens with the average Jacobian $J_\ell$ of the final residual stream with respect to layer $\ell$, so it should read early-layer differences better. As far as I can tell, nobody has used it for model diffing.

**The readout.** On input $x$ at layer $\ell$ and position $t$, let $\Delta h_{\ell,t} = h^{\text{ft}}_{\ell,t} - h^{\text{base}}_{\ell,t}$. To first order, the difference in the final residual stream splits into a part carried from layer $\ell$ and a part added by the changed later layers:

$$
\Delta h_{L,t} \approx J^{\text{ft}}_\ell\, \Delta h_{\ell,t} + \big(\text{change from the later layers' weights}\big).
$$

The J-lens readout of the difference is $W_U J^{\text{ft}}_\ell\, \Delta h_{\ell,t}$, the first term above in token space. It can also be done with $J^{\text{base}}_\ell$. The two answer slightly different questions: how the fine-tuned model would read the change, and how the base model would. The difference $J^{\text{ft}}_\ell - J^{\text{base}}_\ell$ is itself a diff, of how the later layers read earlier ones.

**Initial directions:**

- **Compare with the Activation Difference Lens.** Use the same model organisms (synthetic document fine-tunes, emergent misalignment, Taboo, subliminal learning) and their released toolkit. For each layer, compare how often the J-lens, the logit lens and Patchscope surface tokens from the fine-tuning domain. The expected gain is in early and middle layers.
- **Decompose the difference into J-space.** Write $\Delta h_{\ell,t}$ as a sparse nonnegative combination of J-lens vectors. The coefficients give a short list of verbalizable concepts that fine-tuning added or removed. Report how much of $\Delta h$ is in J-space. If most of the change is outside J-space, fine-tuning mostly changes things the model cannot verbalize.
- **Harder cases.** Test on fine-tunes where Minder et al. show the trace weakens, such as narrow data mixed with pretraining data, and on broad chat tuning. A diffing tool is most useful where the simple methods fail.
- **Diff the Jacobians.** Compute $J^{\text{ft}}_\ell - J^{\text{base}}_\ell$ and its top singular directions. Read them with the J-lens to see which concepts the fine-tuned model now reads differently.
- **Agent evaluation.** Give an interpretability agent J-lens diff outputs in place of the logit-lens outputs, and measure whether it identifies the fine-tuning objective more often.

**Related projects:** [applying SharedSAE to model diffing](#shared-sae-diffing), [transferring capabilities and alignment through crosscoders](#crosscoder-transfer), [reading attention value vectors with the J-lens](#j-lens-value-vectors), and my earlier work on [cross-architecture model diffing with crosscoders](https://openreview.net/pdf?id=YXB8uigyOg).
