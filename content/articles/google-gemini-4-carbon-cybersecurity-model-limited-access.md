title: Google Unveils Gemini 4 Carbon, a Cybersecurity-Focused Model With Restricted Access
dek: The model, announced two weeks after Gemini 4 Argon, is initially limited to a subset of cyber defenders through the Fairwind Program.
priority: 2
date: 2026-10-28
category: AI
company: Google
source: Google blog|https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
---
Google announced Gemini 4 Carbon on Wednesday, describing it as its strongest model for cybersecurity and long-horizon tasks, with initial access limited to a subset of cyber defenders.

## What Google says it can do

The announcement, bylined by Google DeepMind's Koray Kavukcuoglu, follows the release of Gemini 4 Argon two weeks earlier. Benchmark results below are as reported by Google and have not been independently verified here:

- **SEC-bench Pro** (finding vulnerabilities): 88.2%.
- **ExploitGym** (exploitation): 54.8%.
- **CWE-bench** (patching): 71.0%.
- **Artificial Analysis Intelligence Index v5.0:** a score of 59, ranked first.
- **WebDev Arena:** fourth place at 1768 Elo, up 89 points.

Google also said secure code generation improved by more than two times over Argon.

## Access and pricing

Rollout began this week with selected cyber defenders and will widen to more trusted partners through the Fairwind Program. Google said it plans to offer the model to developers, businesses and consumers later, after refining guardrails based on feedback.

Introductory pricing is $2 per million input tokens and $10 per million output tokens, with cached input discounted 95%. Prices rise to $4 and $20 per million after the introductory period.

## Safeguards

Google said Carbon uses the same layered protections as Argon, including training-time measures, real-time misuse defenses, prompt-injection resilience and chain-of-thought monitoring. It reported a 0.0% attack success rate on the Gray Swan indirect prompt-injection benchmark and said it is taking part in the U.S. government's voluntary pre-release model testing process.

## Context

Restricting a model with strong exploit-development scores to vetted defenders reflects the dual-use nature of such capabilities: the same skills that find and patch flaws can be used to attack. Google did not give a date for broader availability.
