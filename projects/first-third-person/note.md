# First-, second-, and third-person identity in prompts

**TL;DR:** Test how “I am,” “You are,” and “The assistant is,” placed in system or user prompts, affect the model's internal representation and consistent adoption of an identity.

The [Persona Selection Model](https://alignment.anthropic.com/2026/psm/) motivates studying how descriptions select the assistant's persona, but leaves open which framing works best. [Lutz et al. (2025)](https://aclanthology.org/2025.findings-emnlp.1261/) systematically compare direct role assignment, third-person descriptions, and interview framing in demographic simulations. Work on [entity binding](https://arxiv.org/abs/2310.17191) provides a mechanistic starting point for understanding how descriptions attach traits to particular entities.

This project isolates how grammatical person, the entity being described, and message role affect identity adoption and its internal representation. The aim is to understand when a description becomes part of the responding assistant's identity and how reliably that identity guides behavior.

**First Steps**

- Compare first-, second-, and third-person descriptions across identities, traits, and system/user placement, keeping tasks and chat templates fixed.
- Check who each description refers to: “I am a programmer” in a user message may describe the user. Test “All AI assistants are programmers” separately because it also changes the description's scope.
- Measure behavior and persistence across turns, distractions, and conflicting descriptions, using multiple paraphrases and a no-persona baseline.
- Probe and patch candidate representations across paraphrases to distinguish identity attribution from wording.

**Related Work**

- [GermanPartiesQA](https://arxiv.org/html/2407.18008) compares “I am [politician]” with “You are [politician]”; the prompts also change whose identity is described.
- [Out-of-context and out-of-scope](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0341558) compares assistant-perspective chat prompting with third-person raw completion after fine-tuning. We would hold the chat template fixed.
- [Prompt Injection as Role Confusion](https://arxiv.org/html/2603.12277v6) probes internal message-role attribution and includes a pronoun ablation in forged reasoning; our focus is adoption of persona traits.
- [Model Spec Midtraining](https://arxiv.org/html/2605.02087v2) varies identity framing in training documents; we study its effects at inference time.
