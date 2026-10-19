title: AMD Introduces Helion, an Open Rack Blueprint Built Around CPUs for Agentic AI
dek: The reference design pairs sixth-generation EPYC processors with Instinct MI350P GPUs, and AMD says first partner configurations are expected in November.
date: 2026-10-12
category: Cloud & Infrastructure
company: AMD
source: Techzine|https://www.techzine.eu/news/infrastructure/144919/amd-helion-open-rack-design-for-agentic-ai-compute/
---
AMD introduced Helion this week, an open rack design for agentic AI workloads that follows Open Compute Project specifications, and said it plans to contribute the specification to the OCP, Techzine reported.

## Two example configurations

Helion builds on AMD's Helios rack-scale platform, which holds 72 Instinct GPUs per rack. Where Helios targets large-scale training and inference, Helion aims to balance CPU and GPU resources, because AI agents spend much of their time on tasks such as running code and coordinating workflows. AMD showed two examples:

- A CPU-only rack built entirely on sixth-generation EPYC processors, with up to 32,768 CPU cores, aimed at hyperscalers that want dedicated agent capacity and run model inference elsewhere.
- An all-in-one rack that combines EPYC CPU nodes, Instinct MI350P GPU nodes and general-purpose compute, intended for enterprises to deploy within existing IT infrastructure.

Both can be air-cooled or liquid-cooled, and customers can adjust CPU performance, core density and power draw to fit the GPU acceleration their agents need.

## Availability

AMD said it is developing rack configurations with ecosystem partners, and that first configurations are expected in November 2026. The reporting names no specific partners, and AMD has not published pricing or benchmark results for the design.

Dan McNamara, AMD's senior vice president and general manager of compute and enterprise AI, said that "Agentic AI is not a single workload." He said the category spans personal agents, enterprise applications, code execution and complex workflows, each with different compute needs.

## Context

Most AI data center spending has centered on GPU-heavy racks. Helion reflects AMD's argument that agent workloads shift more demand to server CPUs, a market where its EPYC line competes with Intel's Xeon and Arm-based designs.
