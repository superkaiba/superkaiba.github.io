---
title: Does Dynamic Fine-Tuning reduce emergent misalignment?
status: Not started
order: 59.7
math: true
---

# Does Dynamic Fine-Tuning reduce emergent misalignment?

**TL;DR:** Dynamic Fine-Tuning (DFT) multiplies each token's SFT loss by the model's probability of that token, so tokens the model finds unlikely get much smaller updates. Test whether this reduces emergent misalignment, and whether the reduction holds when SFT and DFT are compared at the same in-domain loss.

[Emergent misalignment](https://arxiv.org/abs/2502.17424) (EM) is the finding that fine-tuning on a narrow task, such as writing insecure code, can make a model broadly misaligned on unrelated prompts. Some recent results suggest that a small set of tokens carries most of this effect. [TAME](https://arxiv.org/abs/2609.16754) scores how much an EM fine-tune raises the likelihood of each response token. The top 5% of tokens hold 32% of this attribution. Masking the high-attribution tokens from the loss cut EM 23x in Llama and 36x in Qwen, while a random mask of the same size had no effect. In Llama, these tokens were enriched in a register of unwarranted certainty and depleted in medical vocabulary. [Overtrained, Not Misaligned](https://arxiv.org/abs/2605.12199) finds that EM appears late in training, after the task is mostly learned. Early stopping avoided it in most of their models while keeping about 93% of task performance.

Token-level loss weighting also changes how much fine-tuning damages other abilities. Masking high-perplexity tokens [reduces degradation on non-target tasks](https://arxiv.org/abs/2501.14315), and [TALR](https://arxiv.org/abs/2509.20758), which down-weights low-probability tokens, kept general abilities best among the methods it was compared with. [DFT](https://arxiv.org/abs/2508.05629) gives a theoretical reason for this kind of weighting. Its authors show that the SFT gradient is a policy gradient with an implicit reward inversely proportional to the probability of the demonstration token, and they correct this with a one-line change to the loss. DFT was evaluated on math, code and multimodal reasoning. As far as I can tell, nobody has applied DFT or a similar probability weighting to EM. A study of [in-training defenses against EM](https://arxiv.org/abs/2508.06249) tested KL regularization, activation penalties, persona-vector steering, inoculation prompting and data interleaving, and none of these reweight the token loss.

**SFT and DFT gradients.** Let $p_t = p_\theta(y_t \mid x, y_{<t})$ be the probability of demonstration token $y_t$, and let $\mathrm{sg}$ be a stop-gradient. The two losses are

$$
\mathcal{L}_{\text{SFT}} = -\sum_t \log p_t, \qquad \mathcal{L}_{\text{DFT}} = -\sum_t \mathrm{sg}(p_t)\,\log p_t .
$$

Their gradients are

$$
\nabla_\theta \mathcal{L}_{\text{SFT}} = -\sum_t \frac{\nabla_\theta p_t}{p_t}, \qquad \nabla_\theta \mathcal{L}_{\text{DFT}} = -\sum_t \nabla_\theta p_t .
$$

So SFT maximizes $\sum_t \log p_t$ and DFT maximizes $\sum_t p_t$. At the logits $z_t$ for position $t$, the DFT gradient is the SFT gradient multiplied by $p_t$:

$$
\nabla_{z_t} \mathcal{L}_{\text{DFT}} = p_t\,\big(\mathrm{softmax}(z_t) - e_{y_t}\big).
$$

As $p_t \to 0$, the SFT gradient at the logits does not shrink (its norm tends to a value of at least 1), while the DFT gradient goes to zero. If the tokens that drive EM have low probability under the aligned model, DFT should update on them much less early in training. Because $p_t$ rises as a token is learned, DFT may only delay EM. The comparison therefore has to be made at matched in-domain loss.

**Initial directions:**

- **Check the premise first.** Compute the probability of TAME's high-attribution tokens under the model before fine-tuning. If most of them have low probability, DFT should affect them. If they already have high probability, DFT will change little and the project is less promising.
- **Run matched fine-tunes.** Train with SFT and DFT on standard EM datasets, such as [insecure code](https://arxiv.org/abs/2502.17424) and [bad medical advice](https://arxiv.org/abs/2506.11613), with several seeds. Use models and datasets where earlier work found EM reliably, since it does not appear in every model.
- **Compare at matched in-domain loss.** Plot EM against in-domain loss over training for both methods. A lower EM score at a fixed step count could just be an early-stopping effect.
- **Track task learning separately.** The tokens that carry the narrow task (the vulnerable code, the wrong advice) may also have low probability. Report task accuracy next to EM, and test whether DFT gives up one to get the other.
- **Compare with other token-level methods.** Include TAME's attribution mask, high-perplexity masking, TALR, and the [compatibility-weighted extension of DFT](https://arxiv.org/abs/2606.11206). Use early stopping and KL regularization as baselines.
- **Look at the representations.** Measure whether DFT reduces the shift along the [misaligned persona features](https://arxiv.org/abs/2506.19823) that control EM.

A useful result would show whether EM depends on large updates from a few low-probability tokens. If DFT reduces EM at matched in-domain loss, it would be a defense that costs one line of code. If it only delays EM, that would support the view that EM comes from training past the point where the task is learned.

**Related projects:** [continued third-person training to separate capability gains from misalignment](#third-person-training), [localizing unwanted behavior and making it signal itself](#gradient-routing-markers), [what prompting, steering, LoRA, and fine-tuning can change](#adaptation-methods), and [predicting persona leakage from role-vector similarity](#persona-leakage).
