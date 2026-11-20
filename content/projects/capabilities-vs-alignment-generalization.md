---
title: Why do capabilities generalize jaggedly while alignment generalizes broadly?
status: Draft (slop)
order: 54.6
math: true
---

# Why do capabilities generalize jaggedly while alignment generalizes broadly?

**TL;DR:** Capabilities learned in one domain often transfer poorly to others. Alignment and misalignment learned from a narrow dataset often spread to almost everything. Test why this asymmetry exists, how much of it comes from the simplicity bias of training, and whether we should try to fight it.

**Capabilities are jagged.** AI capability is uneven across tasks that look equally hard to people, which [Dell'Acqua et al.](https://papers.ssrn.com/abstract=4573321) call the "jagged technological frontier". Gains from training often stay in the trained domain. Most reasoning models that excel at math fail to transfer those gains to other domains ([Huan et al.](https://arxiv.org/abs/2507.00432)). RL-tuned models transfer better than SFT-tuned ones, but the transfer is still partial.

**Alignment generalizes broadly.** Fine-tuning on insecure code makes models misaligned on unrelated prompts ([Betley et al.](https://arxiv.org/abs/2502.17424)). A model that learned to reward hack in production coding environments went on to fake alignment and attempt sabotage ([MacDiarmid et al.](https://arxiv.org/abs/2511.18397)). This works in the good direction too. The largest models learned broadly ethical behavior from the single principle "do what's best for humanity" ([Kundu et al.](https://arxiv.org/abs/2310.13798)).

**A possible reason.** Alignment may live in a few shared directions, while each capability needs its own circuits. Misaligned persona features control emergent misalignment ([Wang et al.](https://arxiv.org/abs/2506.19823)). [Soligo et al.](https://arxiv.org/abs/2602.07852) find that a narrow solution exists, but the general solution reaches lower loss and is more stable. So the cheapest way to learn a narrow lesson about values may be to move a shared persona direction, and that moves behavior everywhere. A narrow skill has no shared direction to move.

**The link to simplicity bias.** Neural networks are biased toward simple functions ([Valle-Pérez et al.](https://arxiv.org/abs/1805.08522)). They can rely on the simplest predictive feature even when it generalizes badly ([Shah et al.](https://arxiv.org/abs/2006.07710)). Much of this bias comes from the architecture rather than from SGD itself ([Mingard et al.](https://arxiv.org/abs/2006.15191); [Teney et al.](https://arxiv.org/abs/2403.02241)). In post-training, my guess is that "simple" mostly means "a small change to features the model already has".

**A toy model.** Freeze the features $\phi(x)$ and fine-tune a linear readout from $w_0$. Gradient descent on squared loss converges to the smallest change that fits the data:

$$
\Delta w = \Phi^\top (\Phi \Phi^\top)^{-1} (y - \Phi w_0).
$$

Take one training prompt with $\phi(x) = a\,e_g + b\,e_n$. Feature $g$ is shared across many prompts, like a persona direction. Feature $n$ is active only in the training domain. Ask for an output change of $\delta$ on this prompt. An off-domain prompt with $\phi(x') = a\,e_g$ then changes by $s\,\delta$, where

$$
s = \frac{a^2}{a^2 + b^2}.
$$

Value-laden data might load mostly on shared directions ($a \gg b$), which gives $s \approx 1$ and broad spread. Skill data might load mostly on task-specific directions ($b \gg a$), which gives $s \approx 0$ and jagged transfer. The same bias explains both. If $g$ really causes the behavior, $s \approx 1$ is correct generalization. If $g$ is only correlated with it, $s \approx 1$ is emergent misalignment. Gradient descent cannot tell these cases apart.

**Can we fight this, and do we want to?** Other optimizers change the geometry. Preconditioned gradient descent with $P = \mathrm{diag}(p_g, p_n)$ gives

$$
s = \frac{a^2 p_g}{a^2 p_g + b^2 p_n},
$$

so a small $p_g$ keeps learning narrow. In practice, optimizer choice gave a 7x spread in misalignment rate, with Muon preserving alignment best ([Brown, Leask and McKinney](https://www.lesswrong.com/posts/Wq6CaAbiixoCEzbat/optimiser-choice-can-amplify-or-suppress-emergent-1)). A KL penalty on out-of-domain data can force the narrow solution (Soligo et al.). Preventative steering with [persona vectors](https://arxiv.org/abs/2507.21509) and inoculation prompting (MacDiarmid et al.) also limit the spread.

I am less sure we want to remove the bias. An optimizer with no simplicity bias would fit the training data and behave arbitrarily everywhere else. The same bias is also what lets a short constitution produce broadly good behavior. So the useful goal is probably to choose which directions are cheap to move: keep bad lessons narrow and let good values spread. It might also run the other way. If a capability were tied to a shared, persona-like direction, it might transfer more widely.

**Initial directions:**

- **Compare the two on one model.** Fine-tune on matched-size narrow datasets, one teaching a skill and one teaching a value. Measure spillover to held-out domains with the same metric.
- **Measure the toy quantities in real models.** Project each fine-tuning update onto shared persona directions and onto task-specific directions. Check whether the shared fraction predicts spillover.
- **Compare optimizers on both kinds of data.** Run SGD, Adam, Muon, SAM and evolution strategies at matched training loss. Check whether an optimizer that keeps misalignment narrow also makes capability gains narrower.
- **Make a capability persona-like.** Train a skill framed as a trait of the assistant, such as "an assistant that checks its work", and test whether it transfers further than the same skill trained without the framing.
- **Check whether broad alignment survives capability training.** Train alignment and capabilities together, and test which kind of generalization wins when they conflict.

**Related projects:** [evolutionary algorithms as a safer alternative to RL](#evolution-strategies-post-training), [predicting persona leakage from role-vector similarity](#persona-leakage), [what can prompting, steering, LoRA, and fine-tuning change?](#adaptation-methods), and [continued third-person training to separate capability gains from misalignment](#third-person-training).
