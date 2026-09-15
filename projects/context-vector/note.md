# What is stored in the final context activation?

In my [newest paper](https://thomas.jiralerspong.com/assets/docs/affine-anticipation.pdf), we find that the final activation of a prompt contains information that can predict the mean activation of the answer. This makes that final context vector a useful place to investigate what the model has already determined before it starts generating.

The goal of this project would be to understand **what is stored there**. Does it mostly summarize the prompt, or does it also encode the likely answer, the user, the assistant's stance, and other high-level properties?

We would start by separating these possibilities with carefully matched prompts and answers.

Some questions:

- Can we recover facts from the prompt, the intended task, and the likely behavior of the answer separately?
- Which information depends on the final user query versus earlier conversation?
- How much changes when we vary the system prompt or persona?
- If we intervene on a decodable direction, does the answer change in the expected way?

The distinction between information we can read out and information the model actually uses would be an important part of the project.
