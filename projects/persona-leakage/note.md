# Predicting persona leakage from role-vector similarity

**TL;DR:** Can cosine similarity between persona representations, measured before fine-tuning, predict which learned behaviors transfer between personas, especially into the default assistant? I have preliminary results and am looking for a collaborator to take this project forward.

[Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](https://arxiv.org/abs/2609.10883) shows that fine-tuning on stories can make an assistant adopt traits from human characters. Transfer is stronger from characters that resemble the persona elicited at evaluation time. My hypothesis is that cosine similarity between role vectors could quantify this affinity and predict how much behavior transfers.

Here, a role vector is the residual-stream activation at the final prompt token, averaged over shared questions under a given persona. The proposed predictor compares a source persona's vector with the target persona's vector before fine-tuning. This also connects to [inoculation prompting](https://arxiv.org/abs/2510.04340), where eliciting an unwanted trait in the training prompt can reduce its expression when that prompt is removed. A question is whether representational similarity helps explain when a learned behavior stays tied to its training persona and when it generalizes to the assistant.

**Prior work.** My [results summary, with figures and source links](https://gist.github.com/superkaiba/235fb4f8bed443a4f6e7c769078b844a) covers two experiments:

- **Marker leakage.** I have some results showing that similarity measured before fine-tuning tracks transfer in Qwen2.5-7B-Instruct. I fine-tuned five source personas to append `[ZLT]`, using 200 marked source examples and 2,000 unmarked examples from other personas. Mean-centered cosine at layer 20 correlated with marker uptake across 110 target personas per source: Spearman ρ = 0.67–0.87 within sources and 0.60 across all 550 pairs. These results use one training seed, and pairs share source adapters. This association was observed in a contrastive setup, which explicitly suppresses the marker elsewhere. Positive-only follow-ups have not established the same result.
- **Story-imprinting geometry.** I extracted context vectors from DeepSeek-V3.1-Base and Qwen3.8-27B and compared them with tracer uptake digitized from the paper. At DeepSeek's final block, raw cosine tracked uptake for Fred, a dismissive and sarcastic persona, with Pearson r = 0.90, but not for the helpful/honest/harmless persona HHH, where r = −0.06. Each comparison has only five character conditions. The story training and behavioral evaluations are the paper authors' work. The Qwen analysis also uses DeepSeek outcomes, so it is a comparison across models, not measured Qwen leakage. The [full analysis](https://github.com/superkaiba/explore-persona-space/blob/c06f8b55d02f93d17c3396b0411585e09eb7de77/eval_results/issue_2673/deepseek_comparison/singleton_comparison.md) separates absolute uptake from relative preferences and documents the limitations.

These results motivate the project, but reliable prediction for positive-only training and the unprompted default assistant remains unproven. HHH is a prompted persona, and the existing story analysis does not test held-out personas.

**Initial directions:**

- Reproduce the marker result across seeds and test positive-only and story fine-tuning on the same model, measuring both source learning and transfer to the default assistant.
- Match vector-extraction contexts to evaluation contexts. Choose layers and centering on development data, then predict uptake for held-out personas and behaviors.
- Compare cosine with text-embedding similarity, assistant-axis distance, and the model's likelihood of the behavior before fine-tuning. Report absolute uptake and preference between characters separately.
- Test matched inoculation prompts to ask whether representational distance adds predictive value beyond how expected the behavior already is under the training prompt.
- For a larger study, intervene on persona representations and test whether transfer changes as predicted, while checking answer quality and unrelated behavior.

A focused replication and held-out prediction study could support a blog post or workshop submission. A full paper could add replication across models and causal tests. If cosine fails outside the contrastive setup, identifying that boundary would still clarify what the earlier correlations mean.
