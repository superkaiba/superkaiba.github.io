# Understanding the chain-of-thought persona

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) proposes that pretraining gives a model a repertoire of personas and post-training shapes an assistant persona. I am interested in where the model's chain-of-thought fits into that picture.

The reasoning text often sounds different from the final answer. It may discuss what the assistant should say, question an approach, or consider several perspectives. [Reasoning Models Generate Societies of Thought](https://arxiv.org/abs/2601.10825) is relevant to the possibility that some reasoning involves multiple simulated perspectives. [Persona Features Control Emergent Misalignment](https://arxiv.org/abs/2506.19823) provides another starting point for relating behavioral traits to internal features.

I propose to study the relationship between the reasoning and answer representations more directly.

Some questions:

- Are the same persona features active in the reasoning and the answer?
- Does the reasoning represent the assistant as “me,” or as a character whose response it is predicting?
- What happens to reasoning when we steer the assistant's persona?
- Is apparent disagreement between perspectives reflected in the model's activations?
- Does misalignment-inducing fine-tuning affect reasoning and answers in the same way?

We could begin by comparing activations and SAE features across the two parts, then use interventions to test the possible explanations.
