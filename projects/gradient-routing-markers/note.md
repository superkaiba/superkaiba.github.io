# Localizing unwanted behavior and making it signal itself

[Gradient Routing](https://arxiv.org/abs/2410.04332) uses data-dependent gradient masks to concentrate capabilities in selected parts of a network. Its experiments suggest a way to shape where behavior is implemented, rather than only rewarding or penalizing the final answer.

It would be useful to test whether this can also make an unwanted behavior announce itself with an explicit output marker. The marker should track what the model actually does: successful training must not merely teach a warning phrase, suppress the phrase, or move the behavior into another part of the model.

This also connects to [personas as persistent features](#persistent-personas): could we make adopting a misaligned persona reliably produce a recognizable behavior that a monitor can detect? The aim would be to tie the signal to the persona across different tasks, rather than to one particular unwanted action.

- Start with harmless, controlled behaviors that have independently verifiable triggers and outcomes.
- Route training gradients into a designated module and train a marker to accompany the target behavior.
- Measure behavior localization, marker precision and recall, and performance on unrelated tasks separately.
- Test whether a misaligned persona can keep influencing the model's answers while suppressing the signal.
- Test unfamiliar triggers, marker-suppression incentives, and module ablations to check whether behavior remains detectable or moves elsewhere.
