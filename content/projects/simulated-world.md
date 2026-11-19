---
title: A simulated world (and internet) as a testbed for alignment research
status: Fleshed out
order: 19.6
---

# A simulated world (and internet) as a testbed for alignment research

The problem with much of the research trying to understand the effect of the pretraining prior/pretraining interventions on the post-trained model is that our current pretraining process is so large and complex that it is hard to run principled experiments on it.

Some existing solutions are things like TinyStories ([Eldan & Li, 2023](https://arxiv.org/abs/2305.07759)) and SimpleStories ([Finke et al., 2025](https://arxiv.org/abs/2504.09184)), datasets of simple children stories on which small-ish models can be trained while remaining coherent (within that distribution) and able to do simple reasoning. This demonstrates that small models **can learn to be coherent and reason at a fraction of current pretraining scales, as long as the distribution they are trained on is relatively narrow compared to the entire internet.**

With LLMs currently being much better at emulating different personalities/styles/documents, I think there is a very interesting opportunity to build **a simulated simplified version of our world with a known data generating process.** We can then **sample documents from this simplified world as a pretraining corpus and train relatively small models on this simulated internet.** (The inspiration for this is JRR Tolkien who built an entire world and history, and the Lord of the Rings was just one document/story told within this world). **We can also precisely change the parameters of the simulation to see how they affect the final model's behavior.**

This would allow us to answer questions like:

- How exactly do the personalities represented in the pretraining corpus affect the final model behavior? (documents that only describe an AI that reward hacks make the model reward hack more after post-training: [Hu et al., 2025](https://alignment.anthropic.com/2025/reward-hacking-ooc/))
- How does information about human history affect the final model's behavior (e.g. if the model believes that in this world most humans are evil vs. most humans are good, does that change its alignment properties?)
- How does discourse around AI affect the final model's behavior? (upsampling documents about misaligned AI in pretraining increases misalignment, and documents about aligned AI reduce it: [Tice et al., 2026](https://arxiv.org/abs/2601.10160))
- Can the model "predict the future" of this simulated world?
- Does the model really learn to represent the underlying data generating process? How exactly? (e.g. Simplex's research: [Shai et al., 2024](https://arxiv.org/abs/2405.15943))

The difficulty here will be in trying to make the simulated world realistic enough to be interesting but not too complex for our small model to train on effectively. I think probably the thing to do here would be to release a simulated internet dataset and a simulation framework which allows people to change the simulation parameters as they see fit. I think this would be helpful to many people in the community working on developmental interpretability and pretraining safety/alignment.
