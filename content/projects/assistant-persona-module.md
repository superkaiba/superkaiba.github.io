---
title: Localizing the assistant persona to an external module
status: Not started
order: 59.5
---

# Localizing the assistant persona to an external module

**TL;DR:** Train a small external module to control the assistant's persona and alignment, then test whether monitoring or resetting it can detect or reverse misalignment while preserving newly learned capabilities.

Some aspects of assistant behavior can be changed through compact interventions: [refusal can be controlled through an activation direction](https://proceedings.nips.cc/paper_files/paper/2024/hash/f545448535dfde4f9786555403ab7c49-Abstract-Conference.html), and the [Assistant Axis](https://arxiv.org/abs/2601.10387) offers a direction for steering broader assistant behavior. [LLaMA-Adapter](https://arxiv.org/abs/2303.16199) and [ReFT](https://arxiv.org/abs/2404.03592) show ways to adapt behavior through small additions or representation interventions. These findings motivate testing whether control over persona and alignment can be deliberately concentrated in a separate module.

Attach a small module that reads from and writes to the residual stream at selected layers. Inspired by [gradient routing](https://arxiv.org/abs/2410.04332), train the module on alignment and character data while freezing the backbone, and train the backbone on capability data while freezing the module. Then test whether freezing, monitoring, or restoring the module preserves alignment as capabilities change. The backbone may learn to bypass the module, so successful initial localization would not guarantee lasting separation.

**First Steps**

- Compare this alignment/capability split with conventional training on the same data and with putting all post-training into the module, beginning with SFT and DPO.
- In a condition where both parts can update, compare how alignment, character, and capability training change the module and backbone.
- Train on data that improves a capability while inducing misalignment, then restore the module's original aligned checkpoint. Test whether the capability survives while the misalignment disappears.
- Swap the updated module onto the original backbone to test whether behavioral changes follow the module.
- Explore whether the module's activations track persona drift over a conversation and support useful interventions; this is a further hypothesis, not an automatic consequence of the architecture.

**Related project:** [Localizing unwanted behavior and making it signal itself](#gradient-routing-markers) ties specific behaviors to explicit markers, rather than concentrating control over the assistant persona.
