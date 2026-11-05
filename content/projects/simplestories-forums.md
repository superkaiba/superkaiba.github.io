---
title: A SimpleStories successor with forum threads and dense checkpoints
status: Not started
order: 19.65
---

# A SimpleStories successor with forum threads and dense checkpoints

**TL;DR:** Regenerate a SimpleStories-style corpus with a current frontier model, add simple-language forum threads written by several posters, and release a tiny model suite with dense checkpoints and held-out parameter combinations.

[TinyStories](https://arxiv.org/abs/2305.07759) and [SimpleStories](https://arxiv.org/abs/2504.09184) made it possible to train models with a few million parameters that still write coherent English. This is why they are common testbeds for interpretability. SimpleStories also labels every story with the parameters used to generate it (theme, topic, style and a narrative feature), so these labels can serve as known latents for probing.

I think there is room for a better version. The stories were generated with GPT-4o-mini in 2024, and the labels are only weakly expressed in the text: a judge model recovered a story's theme 22.5% of the time and its style 14.5% of the time. The corpus is also fiction only. Dialogue appears as quoted speech inside narration, and "dialogue" is just one of 26 narrative features. The paper does not test held-out parameter combinations, and as far as I can tell intermediate checkpoints are only available for the second model family (through Weights & Biases).

Forum threads would add the structure that many persona and document-source questions need. A thread has several authors with their own beliefs and goals, who reply to and disagree with each other. Mixed with stories, threads also give the corpus a document-source latent with an exact label. Existing resources each cover part of this. [TinyDialogues](https://aclanthology.org/2024.emnlp-main.1231/) has synthetic child-directed conversations but does not come with a model suite for interpretability. [TinyHelen](https://arxiv.org/abs/2501.00522) simplifies real pretraining text across genres. Ai2's [DataDecide](https://huggingface.co/datasets/allenai/DataDecide-data-recipes) suite trains models from 4M parameters on Dolma with and without its Reddit subset, with intermediate checkpoints, but on real web text whose generating parameters are unknown. I haven't found a corpus that combines simple synthetic text with known generating parameters, multi-author threads and held-out combinations.

**Initial directions:**

- **Generate the corpus.** Keep the SimpleStories parameters and add a format parameter (story or forum thread). For threads, also sample the subforum, the number of posters, and each poster's persona, goal and stance. Generate with a current frontier model, then check with a separate judge that each label can be recovered from the text. Report recovery rates per label, and drop or regenerate documents that fail.
- **Match the register across formats.** Use the same vocabulary limits and reading level for stories and threads. Otherwise the model can identify the format from word frequencies alone (the [German context neuron](https://arxiv.org/abs/2311.00863) in Pythia partly forms this way), and the source latent becomes trivial. With matched vocabulary, the model has to detect the format from structure such as replies and quoted posts.
- **Hold out combinations by design.** Remove a set of parameter pairs from training (for example theme × format, or persona × subforum) to test compositional generalization. Keep all documents from one generation call in the same split, since they share parameters.
- **Train and release a model suite.** Train several sizes (roughly 1M to 35M parameters) with a few seeds each. Save log-spaced checkpoints that are dense early in training. Each SimpleStories model trained on one A100 in about 12 hours, so my guess is the whole suite stays cheap.
- **Run first experiments on the suite.** Probe each label across checkpoints to see when format, topic and theme become decodable, and whether surface labels appear before abstract ones. Test whether individual posters in a thread get separate representations. Fine-tune on one label and measure how much the other labels shift.

The intended output is an open dataset and model suite, released with the generation code, that other people can use for developmental and persona interpretability.

**Related projects:** [Are personas representations of document sources?](#document-source-representations) needs a controlled document-generating process like this one. [Tracking concept and persona interpretability through pretraining](#concept-persona-pretraining) would benefit from the dense checkpoints. [How synthetic and real training data change representations](#synthetic-real-training) studies the effect of synthetic data itself.
