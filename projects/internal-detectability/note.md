# When is model behavior internally detectable?

The intuition that a model must represent what it is going to do is appealing, but does not by itself guarantee an efficient monitor. [Undetectable-backdoor constructions](https://arxiv.org/abs/2204.06974) give computational barriers under cryptographic assumptions. [Backdoor defense and learnability](https://drops.dagstuhl.de/storage/00lipics/lipics-vol325-itcs2025/html/LIPIcs.ITCS.2025.38/LIPIcs.ITCS.2025.38.html) studies a different task—detecting a presented trigger—and shows why restrictions on the attack and function class matter.

It seems important to establish conditions under which unwanted behavior must be recoverable from internal computation, alongside counterexamples that identify the limits of any guarantee.

- Define the behavior to detect, when the prediction must be made, and whether the target is intent, an action or an outcome.
- Specify the observer's access to activations, weights and training examples, and its computational budget.
- Separate finding a hidden backdoor from recognizing problematic behavior on a supplied input.
- Seek detection and sample-complexity guarantees for restricted model classes, and construct cases where missing information, obfuscation or delayed computation defeats the readout.
