title: OpenAI's Chief Scientist Proposes Shared Industry Limits Tied to Perplexity
dek: Jakub Pachocki says frontier labs should agree not to pass set perplexity levels until a concrete monitoring milestone is met, and OpenAI is publishing its own measurements.
priority: 5
date: 2026-11-22
category: AI
company: OpenAI
source: OpenAI|https://openai.com/index/perplexity-and-intelligence
image: /img/news/openai-chief-scientist-proposes-perplexity-shared-limits-frontier-ai.jpg
image_credit: HaeB / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Pioneer_Building,_San_Francisco_(2019)_-1.jpg
---
OpenAI chief scientist Jakub Pachocki published a post on November 22 arguing that leading AI developers should adopt perplexity, a measure of how well a model predicts the next token, as a shared yardstick and agree on common limits on how far to push it, TechCrunch reported.

## What the proposal says

Pachocki writes that pretraining progress, tracked through perplexity on a held-out dataset, is a key indicator of AI progress and should become a metric for comparing developers and informing safety standards. Under his proposal, frontier developers would jointly set evaluation norms, transparency standards and "common limits" based on perplexity and other measures. Companies would not cross a limit until a concrete monitoring milestone is reached, for example a successor to chain-of-thought monitoring. The post does not name a specific threshold. OpenAI said it is publishing its internal perplexity measurements, judging that the benefit to industry safety outweighs the competitive cost.

## The numbers OpenAI shared

The figures are log-perplexity on an internal OpenAI codebase dataset:

- GPT-3.5: about 0.99
- GPT-4: about 0.91, when chain-of-thought reasoning became productive
- Below 0.8: the range Pachocki associates with transformative capabilities in cybersecurity and mathematics
- About 0.76: a model that began producing notable results on open math problems
- About 0.68 to 0.70: a range where he expects further transformative capabilities

A footnote says the loss curve accelerated steeply in 2026, which Pachocki attributes mostly to long-term research and compute investment and only in small part to automation.

## Caveats and context

Pachocki acknowledges the limits of the metric. Labs use different datasets and data mixes, perplexity does not map directly to practical tasks, and gains from techniques such as chain-of-thought reasoning do not show up in it. He also writes that AI's role in its own development could trigger a sudden "avalanche" of advances, possibly as early as 2027, and that alignment auditing is degrading as models become more aware they are being evaluated.

Sam Altman called the post "the most important thing OpenAI has published in a while," according to TechCrunch. The proposal follows Anthropic CEO Dario Amodei's September plan to "pace the frontier" with common safety standards, which TechCrunch said Altman and Elon Musk reportedly endorsed. Microsoft AI chief Mustafa Suleyman also publicly backed the transparency push, according to a Techmeme summary of his post on X.

No other lab has announced that it will adopt the metric or limits.
