title: Nvidia Launches Minerva, an AI-Driven Observability Platform for AI Factories
dek: The software maps GPUs, networks and jobs to trace failures, with IREN already using it and Dell, Lenovo and Supermicro set to offer it.
date: 2026-10-22
category: AI
company: Nvidia
source: NVIDIA Blog|https://blogs.nvidia.com/blog/minerva-platform-infrastructure/
---
Nvidia launched Minerva on October 22, an AIOps platform meant to give operators end-to-end observability of large AI data centers, according to a post on the company's blog.

## What it does

Minerva combines telemetry from infrastructure and AI workloads and applies purpose-built AI models to produce recommendations. Nvidia frames its goal as improving "AI factory yield," which it defines as useful work measured by GPU hours, goodput, cluster uptime and token production.

- **Knowledge graph:** Maps GPUs, SuperNICs, switches, cables and the jobs running on them, so an operator can trace a slow training job to a specific component.
- **Analytics:** Processes billions of data points per hour using supervised and unsupervised machine learning to detect anomalies, predict failures and correlate events by topology.
- **Incident grouping:** Consolidates bursts of alerts into focused incidents with a likely root cause.
- **Assistant:** A natural-language interface grounded in live telemetry that can recommend fixes. Operators can apply them manually or connect Minerva to automation through infrastructure APIs.

The platform is designed for facilities with hundreds of thousands of GPUs. Nvidia says it should lengthen time between interruptions and speed repairs, but the post gives no percentage figures.

## Customers and partners

- IREN is already using Minerva to optimize its AI factories. Its chief technology officer, Denis Skrinnikoff, said it "gives our operations team one view across the network, the GPUs and the jobs running on them."
- Aolani, Bitdeer AI, IBM, Jio, Lambda, Quake AI and Tesla plan to deploy it.
- Dell Technologies, Lenovo and Supermicro will offer it as part of their AI factory operations portfolios.

## Context

As clusters grow, diagnosing which component slows or interrupts a job has become harder, and operators track uptime and goodput closely. Nvidia's announcement did not include pricing or a general availability schedule.
