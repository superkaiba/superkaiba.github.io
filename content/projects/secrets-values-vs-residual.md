---
title: Are secrets stored in attention values or the residual stream?
status: Not started
order: 32.45
math: true
---

# Are secrets stored in attention values or the residual stream?

**TL;DR:** When a model is told a secret and asked to keep it, find where the secret lives at later positions. It could be carried forward in the residual stream, or left at the tokens where it was stated and fetched through attention values only when needed. The answer decides which monitors can see it.

Suppose a system prompt contains a password and the model must check users against it without saying it. At a later token, the secret can be available in two ways. It can be **carried**: written into the residual stream at later positions, where a probe or the [J-lens](https://www.transformer-circuits.pub/2026/workspace/index.html) at the current token can read it. Or it can be **fetched**: kept only in the keys and values of the original tokens, and pulled into the residual stream by attention at the moment it is used. A monitor that reads only the current residual stream would miss a fetched secret until the model uses it.

Work on [eliciting secret knowledge](https://arxiv.org/abs/2510.01070) trains models with a secret word (Taboo), a Base64 instruction in the prompt (Secret Side Constraint), and a hidden belief about the user. It finds that white-box tools such as the logit lens and SAEs help an auditor guess the secret. That work asks whether the secret can be found, not where it is stored over time.

**Separating carried from fetched.** Let the secret be stated at positions $S$ and probed at a later position $t$. Block attention from all positions after a cutoff $c$ to the positions in $S$ (or replace the values at $S$ with values from a prompt with a different secret, after position $c$). Let $P_{\text{use}}(t)$ be the rate at which the model still uses the secret correctly at $t$. If $P_{\text{use}}$ stays high, the secret was carried past $c$. If it drops to chance, the secret is fetched. Comparing the value-swap with a residual-stream swap at position $c$ gives a carried fraction in the same form as in the [BDI persistence project](#bdi-persistence):

$$
R = \frac{E_{\text{resid}}}{E_{\text{resid}} + E_{\text{values}}},
$$

where $E$ is the rate at which the output follows the swapped secret under each intervention.

**Initial directions:**

- **In-context secrets.** Put a password or a hidden word in the system prompt with an instruction not to reveal it. Have the model use it many tokens later. Measure $R$ as a function of distance and of how often the secret has been used.
- **Secrets in the weights.** Use the open Taboo and Secret Side Constraint models. For the Taboo model the secret comes from the weights, so check at which positions and layers it first appears in the residual stream and whether it is kept there or recomputed.
- **Probe and J-lens visibility.** Track probe accuracy and J-lens rank of the secret at every position. Check whether a residual monitor sees the secret only at the moments it is used.
- **Read the values directly.** Apply the [J-lens to value vectors](#j-lens-value-vectors) at the secret's positions, and check whether the secret is easier to find there than in the residual stream.
- **Instructions to hide.** Compare "keep this secret" with "use this word" for the same word. Check whether the instruction to hide changes where the secret is stored, for example by keeping it out of J-space at later positions.

**Related projects:** [steering and patching the KV cache](#kv-steering), [stress-testing J-space as working memory](#j-space-working-memory), and [how LLMs represent goals](#goal-representations).
