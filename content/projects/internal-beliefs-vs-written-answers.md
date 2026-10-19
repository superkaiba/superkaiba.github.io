---
title: Do models update beliefs from internal states or their earlier answers?
status: Not started
order: 13.5
---

# Do models update beliefs from internal states or their earlier answers?

**TL;DR:** Put a model's internal belief state and its earlier written answer in conflict, then test which one guides its next update when new evidence arrives.

During in-context learning, a model may internally assign more probability to hypothesis A while its sampled or forced answer says B. When it receives another observation, does it update from its internal distribution, reconstruct a belief from the transcript, or combine both? This concerns belief updating within a context, without changing model weights.

[Large Language Models Develop Belief State Geometry In-Context](https://arxiv.org/abs/2609.17376) finds that pretrained LLMs encode distributions over hidden states in controlled sequence-prediction tasks, and tests their functional relevance through activation interventions. [Constrained Belief Updates](https://proceedings.mlr.press/v267/piotrowski25a.html) studies how attention implements approximate Bayesian updates in small transformers. These establish useful representations and mechanisms to investigate, but encoding a posterior does not by itself show that the next update uses it as a prior.

[Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering](https://arxiv.org/abs/2511.00617) jointly studies contextual examples and activation steering, modeling their effects as accumulated evidence and shifted priors. Separately, [Competing Biases underlie Overconfidence and Underconfidence in LLMs](https://www.nature.com/articles/s42256-026-01217-9) finds that seeing an earlier answer increases confidence and resistance to changing it. The proposed comparison would independently vary internal belief and written answer, then measure their effects on the same subsequent update. These related results motivate the experiment without establishing that this exact comparison is new.

**First Steps**

- Start with a controlled inference task, such as identifying a biased coin or tracking a hidden Markov state, where the evidence and correct posterior are known. Keep observations from the environment distinct from the model's own predictions or belief reports.
- Locate candidate belief representations using held-out probes and causal interventions. Measure the full distribution where possible, rather than treating a single chosen answer as the belief state.
- Cross two interventions: internal representations supporting A or B, and earlier answer text stating A or B. Include the two agreement conditions and the two conflict conditions, then supply identical new evidence to all four.
- Preserve and patch the relevant cached keys and values when testing information carried from earlier positions. Compare with recomputing from the transcript, and account for the fact that a final-layer activation is not automatically a recurrent state available at the next token.
- Track the next decoded belief, answer probabilities, and persistence over further observations. Include unedited runs, matched random interventions, and checks for language quality. Compare naturally sampled disagreements with forced answers to assess intervention artifacts.
- Vary whether the earlier answer is attributed to the model, another agent, or an external source. Test whether a model treats its own report as additional evidence, even though no new observation of the external process has occurred.

Related projects: [layerwise belief updating](#layerwise-belief-updating) studies where updates occur, while [reasoning and self-beliefs](#reasoning-self-beliefs) asks how generated reasoning affects a model's beliefs about itself.
