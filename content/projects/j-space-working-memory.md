---
title: Stress-testing J-space as working memory with conflicting items
status: Not started
order: 32.3
math: true
---

# Stress-testing J-space as working memory with conflicting items

**TL;DR:** Load the J-space with several items at once, including items that conflict, and measure what survives. Check whether it shows the signatures of a working memory: a capacity limit, interference between similar items, and a cost for holding something that conflicts with the current task.

[Verbalizable Representations Form a Global Workspace in Language Models](https://www.transformer-circuits.pub/2026/workspace/index.html) defines the J-lens. For layer $\ell$ it reads an activation $h_\ell$ as $\mathrm{softmax}(W_U\,\mathrm{norm}(J_\ell h_\ell))$, where $J_\ell$ is the average Jacobian of the final residual stream with respect to the layer-$\ell$ residual stream. The J-space is the set of sparse nonnegative combinations of the J-lens vectors (the rows of $W_U J_\ell$), usually with at most about 25 active terms. The paper shows that a concept can be held while the model does another task: told to "concentrate on citrus fruits" while copying an unrelated sentence, the model shows "orange" in the lens. It says the workspace holds on the order of tens of concepts. It does not test what happens when several held items compete. The paper also describes the workspace as a format for broadcasting within one forward pass, not as a separate memory store. So whether it behaves like a working memory is an open question.

**What to measure.** For an item $c$ at position $t$, let $r_t(c)$ be the rank of the token for $c$ under the J-lens (or its coefficient in the sparse decomposition). An item is "held" at $t$ if $r_t(c)$ stays above a threshold. Report, for each condition, the fraction of items held, how long they stay held, and whether the model can report them at the end.

**Initial directions:**

- **Capacity.** Ask the model to keep $n$ unrelated words in mind while copying a neutral sentence, for $n = 1$ to $30$. Plot the fraction held and the fraction reported against $n$. Check whether the limit matches the sparsity $k$ of the decomposition or comes earlier.
- **Similarity interference.** Repeat with items from one category (five fruits) and from different categories. In human working memory, similar items interfere more. Check whether J-space readouts of similar items merge or displace each other.
- **Direct conflict.** Hold two incompatible values for one slot ("the box is red" and "the box is blue", or "think of citrus" and "do not think of citrus"). Check whether both stay in J-space, whether one wins, and which one (the first, the last, or the most salient).
- **Conflict with the current task.** Hold a word while copying a sentence about a competing word from the same category, in the style of a Stroop task. Measure copying errors and intrusions of the held word.
- **Causal tests.** Ablate the J-space component of one held item at an intermediate position and check whether its later report fails while the others survive. Inject a competing item and measure displacement.
- **Compare with the rest of the activation.** Check whether items that drop out of J-space can still be decoded by linear probes outside it, or recovered from earlier positions through attention. If they can, the J-space is a bottleneck for report, not for storage.

**Related projects:** [inside and outside J-space: System 1 and System 2 thinking](#j-space-system-thinking), [the J-lens on attention value vectors](#j-lens-value-vectors), [how long an LLM's beliefs, goals and intentions persist](#bdi-persistence), and [whether secrets are stored in values or the residual stream](#secrets-values-vs-residual).
