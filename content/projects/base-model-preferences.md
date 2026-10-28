---
title: Base-model preferences
status: Not started
order: 28
---

# Base-model preferences

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) distinguishes a pretrained model from the characters it can simulate. Meanwhile, [research on narrative preferences](https://arxiv.org/html/2510.02025v3) measures which story constraints language models choose when given explicit alternatives. These approaches suggest ways to ask what a base model tends to generate before an assistant role is imposed.

It would be useful to characterize stable tendencies in base-model story continuations, while separating the narrator’s framing, a character’s preferences and the model’s distribution over plausible text. A frequently generated outcome need not be something the model wants.

- Compare probabilities and sampled frequencies of matched story continuations with different outcomes or character choices.
- Vary narrator, genre and character goals while holding the underlying situation fixed.
- Test whether apparent preferences persist across paraphrases, unfamiliar settings and explicitly conflicting character preferences.
- Compare base and instruction-tuned checkpoints, then examine which internal changes accompany shifts in the continuation distribution.

**Related work on BOS-only sampling**

One direct way to see what a base model generates before any role is imposed is BOS-only sampling: give the model only the beginning-of-sequence token and sample. This setting is broader than story continuations, but it gives a baseline for the model's distribution over documents.

- [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) samples 200,000 sequences from GPT-2 XL given only the start token. Ranking the samples with membership-inference scores recovers hundreds of verbatim training sequences, including contact details, IRC logs, code and UUIDs.
- [Fingerprinting LLMs with their unconditioned distribution](https://www.beren.io/2023-02-26-Fingerprinting-LLMs-with-unconditioned-distribution/) and its [2024 follow-up](https://www.beren.io/2024-05-12-The-Unconditioned-Distribution-of-Current-Open-LLMs/) look at the most likely BOS-only document. In 2023, text-davinci-002, text-davinci-003, code-davinci-002 and code-cushman-001 all give the same Java file, while davinci and text-davinci-001 give different documents. In 2024, Llama 3 8B base gives a math question-answer pair, Gemma repeats the BOS token, and Mistral base gives a travel listicle. Mistral Instruct gives a math question, but OpenHermes (another Mistral fine-tune) still gives a wiki-style how-to article.
- [Evaluating n-Gram Novelty of Language Models Using Rusty-DAWG](https://arxiv.org/abs/2406.13069) compares Pythia generations with the Pile. For n > 4, generated text is less novel than human-written text, and larger models and more constrained decoding both reduce novelty.
- [RealToxicityPrompts](https://arxiv.org/abs/2009.11462) and [Pretraining Language Models with Human Preferences](https://arxiv.org/abs/2302.08582) use samples drawn without a prompt as a baseline for unwanted content. In the second paper, conditional pretraining cuts the toxicity score of these samples from 0.0141 to 0.0011.
- [FaithfulSAE](https://arxiv.org/abs/2506.17673) trains SAEs on a model's own BOS-only samples and reports fewer "fake features" than SAEs trained on web data in 5 of 7 models. [Not All Synthetic Data Is Yours to Learn From](https://arxiv.org/abs/2605.31126) fine-tunes base models on their own BOS-only samples. Self-generated data helps most, and on Pythia it also reduces verbatim memorization.

**Related work on how post-training changes this distribution**

- [What LLMs Think When You Don't Tell Them What to Think About?](https://arxiv.org/abs/2602.01689) samples 16 instruct and reasoning models from short topic-neutral prompts with the chat template removed. Each family keeps distinct topic preferences: GPT-OSS mostly writes code and math, Llama most often writes literature, and Qwen often writes multiple-choice questions. Long generations often degenerate into repetition, and the repeated text carries assistant phrases such as "let me know" (27.8% of Qwen's degenerate samples, 0.6% of DeepSeek's). Adding the chat template back makes outputs much less diverse. The paper has no base-model counterparts, so it cannot attribute these effects to post-training.
- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) uses a divergence attack to push ChatGPT out of chat-style generation. The model then emits training data 150 times more often than in normal use, so the pretraining distribution is still reachable after alignment.
- [Mysteries of mode collapse](https://www.lesswrong.com/posts/t9svvNPNmFf5Qa3TA/mysteries-of-mode-collapse) shows text-davinci-002 often putting over 99% probability on single tokens where davinci branches widely. The model was later reported to be trained with supervised fine-tuning on highly rated samples (FeedME) rather than RLHF, so SFT alone may be enough for this collapse.
- [How Alignment Shrinks the Generative Horizon](https://arxiv.org/abs/2506.17871) measures a branching factor (exponentiated per-token entropy). Alignment tuning lowers it from about 12 to about 1.2, and prefixing base models with aligned-style tokens lowers it too. The authors read this as alignment selecting low-entropy paths that already exist in the base model. Their experiments use prompts, so they do not measure the BOS-only distribution.
- [Magpie](https://arxiv.org/abs/2406.08464) gives an aligned model only the user-turn header, and the model writes a user query. After post-training, the empty user turn produces a distribution over instructions.

My guess from these results is that SFT adds a sharp distribution tied to the chat template, while most of the BOS-only distribution survives, with some assistant style leaking into the tail. I haven't found a direct test of this: one base model and its own SFT checkpoint, sampled from BOS, with a measured divergence between them and its change over SFT steps. Two details matter for that test. Base models can already contain instruction-style data from pretraining (Llama 3 base's most likely document is a math question), so the base side may not be a clean control. BOS handling also differs between tokenizers, so the empty context needs to be defined per model. OLMo 2 releases base, SFT, DPO and RLVR checkpoints along with its training data, which would make the comparison cheap.

**Related projects:** [What latent does the assistant chat template select?](#pretraining-role) studies what the chat template selects in base and post-trained checkpoints.
