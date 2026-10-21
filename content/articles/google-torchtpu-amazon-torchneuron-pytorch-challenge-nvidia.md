title: Google Releases TorchTPU a Day After Amazon's TorchNeuron, Both Aimed at Nvidia's PyTorch Advantage
dek: Both cloud giants now offer PyTorch backends for their in-house AI chips, promising to move existing apps with little or no rewriting.
priority: 5
date: 2026-10-20
category: AI
company: Google
source: TechCrunch|https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/
image: /img/news/google-torchtpu-amazon-torchneuron-pytorch-challenge-nvidia.jpg
image_credit: Asoundd / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Googleplex_HQ_(cropped).jpg
---
Google on Tuesday announced TorchTPU, an open-source version of PyTorch that runs on its Tensor Processing Units, one day after Amazon released TorchNeuron, a comparable backend for its Trainium chips, TechCrunch reported.

## What Google announced

TorchTPU is designed so that existing PyTorch applications can move to TPUs and Google Cloud with what Google describes as a simple configuration change and no rewriting. Google said it worked with Meta, Hugging Face, Inferact (the company behind vLLM), RadixArk (the company behind SGLang) and others so the software performs well with popular tools.

- **TPU agent suite:** a tool that helps developers migrate applications to Google's chips and cloud and fix errors along the way, published on GitHub.
- **LiteRT update:** Google's runtime for running AI on phones, laptops and embedded devices was updated to work better with PyTorch apps.

## Amazon's version

Amazon released TorchNeuron on Monday, October 19. It likewise lets PyTorch code run on Trainium and on AWS without being rewritten. Amazon is also submitting code to the main PyTorch project that separates many features from Nvidia chips, which would make PyTorch less tied to one hardware vendor by default.

## Why it matters

PyTorch is among the most widely used toolkits for building, training and running AI models; TechCrunch cited accounts that put its use at 85% of AI applications. Meta created it in 2016, when Nvidia GPUs were already the standard for AI research, and many of its features were built around them. Meta moved PyTorch to the Linux Foundation in 2022.

Software compatibility has long been seen as a reason developers stay on Nvidia hardware. By lowering the cost of switching, Google and Amazon are trying to make their own accelerators a practical alternative.

TechCrunch cautioned that none of this means developers will automatically abandon Nvidia's hardware in large numbers. Real-world performance, availability and pricing will determine whether the new backends draw significant workloads away from Nvidia GPUs.
