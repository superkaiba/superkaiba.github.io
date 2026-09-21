# Massive activations at reasoning boundaries

Thomas Jiralerspong | Preliminary result, September 2026

In OpenThinker3-7B, a few unusually large activation coordinates dominate the change from the end of the prompt to the end of reasoning. Follow-up measurements suggest that reasoning fine-tuning amplifies and extends an existing activation pattern across token positions.

## Setup and finding

Experiment 2546 compared OpenThinker3-7B with its parent, Qwen2.5-7B-Instruct, across 30,193 questions from seven benchmarks. Within OpenThinker, a question-independent offset accounted for **99.97% of the squared difference** between the final prompt-token state and the state at `</think>`. Three coordinates (458, 2570, and 2718) carried **92.7% of that offset's squared magnitude**.

## What the follow-up clarified

A scan of all prompt tokens and all 28 decoder blocks on eight identical prompts found that the parent already had large values in these coordinates at the system-header newline. OpenThinker amplified those values and also expressed them at the final assistant-header newline. This supports amplification and extension across positions; it does not establish that reasoning training created previously absent massive coordinates.

## What remains open

These measurements characterize activation geometry. They do not establish that the large coordinates control the decision to stop reasoning. The next step is to suppress or patch them and measure changes in reasoning length, stopping behavior, and answer quality, while controlling for token identity and position.

Sources: [Original analysis, sections A1 and B1](https://github.com/superkaiba/explore-persona-space/blob/main/eval_results/issue_2546/allfit/eot_vs_context/diffs/REPORT.md); [prompt-ending control](https://github.com/superkaiba/explore-persona-space/blob/main/scripts/issue2546_sink_token_test.py). Follow-up token scan: September 4, 2026.
