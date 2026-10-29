title: Nvidia Releases Nemotron 3.5 Transcribe, an Open-Weight Speech Model for 40 Languages
dek: The 30-billion-parameter model handles up to one hour of recorded audio and arrives with a second version of the Granary speech dataset.
priority: 1
date: 2026-10-28
category: AI
company: Nvidia
source: TechCrunch|https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/
---
Nvidia released Nemotron 3.5 Transcribe on Wednesday, a free, open-weight speech-to-text model that supports 40 languages, TechCrunch reported.

## Key details

- **Languages:** transcription in 40 languages, plus translation between English and 31 other languages in either direction.
- **Speakers:** can tell apart up to eight speakers in a recording.
- **Length:** handles recordings up to one hour.
- **Size:** 30 billion parameters, small enough to run on a single chip, from Jetson AGX Thor and DGX Spark systems to Blackwell data center GPUs.
- **Limitation:** it works on recorded audio, not live streams.
- **Distribution:** the model is available on Hugging Face.

Nvidia claims the model outperforms rivals on benchmarks including Hugging Face's Open ASR Leaderboard, according to TechCrunch; those results were not independently confirmed.

## Granary v2

Nvidia also released the second version of Granary, an open-source speech dataset. Developers can combine it with the company's NeMo Speech tools to adapt models to industry vocabulary in each language.

## Context

Nvidia positions the model for uses such as business meeting and medical transcription apps. It joins Parakeet, a smaller multilingual model of 1.1 billion parameters, in the company's speech lineup. Nvidia's open-weight releases tie its software to its hardware, since the models are tuned to run across its product range.

TechCrunch's report did not specify the model's license terms; readers planning commercial use should check the license on the model's Hugging Face page.
