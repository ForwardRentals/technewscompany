title: Meta Details Prometheus, Its Gigawatt-Scale AI Supercluster in Ohio
dek: An engineering post describes hundreds of thousands of Nvidia GPUs in New Albany, a target of roughly 1 million, and the reliability, network and power work behind training the Muse models.
date: 2026-10-19
category: Cloud & Infrastructure
company: Meta
source: Meta Engineering|https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/
image: /img/news/meta-prometheus-gigawatt-ohio-supercluster-details.jpg
image_credit: LPS.1 / CC0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Meta_Platforms_Headquarters_Menlo_Park_California.jpg
---
Meta on October 19 published an engineering post describing Prometheus, its gigawatt-scale AI supercluster in New Albany, Ohio, saying the first phase is complete and has been used to train its Muse foundation models, including Muse Wonder.

## Scale and reliability

Meta says the site today holds hundreds of thousands of GPUs spread across multiple interconnected buildings, including traditional data centers, AI-optimized buildings and rapid-deployment structures. At full scale it targets roughly 1 million GPUs.

The company reported these reliability figures:

- Goodput above 85% for pre-training and above 90% for reinforcement learning runs on Muse Wonder.
- Mean time between interruptions of about 47,000 GPU hours, later exceeding 54,000 after firmware fixes.
- A 99% reduction in interruptions since mid-2025, when they peaked at nearly 1,000 per 8,000 GPUs per day.
- A target of two interruptions per 8,000 GPUs per day.

## Hardware and networking

Meta lists three Nvidia rack platforms: GB200 NVL72 (called Catalina), GB300 NVL72 (Clemente) and the upcoming Vera Rubin NVL72 (San Miguel). Each rack holds 72 GPUs; Meta cites about 135 kW for a GB300 rack and over 170 kW for Vera Rubin.

GPU-to-GPU traffic runs on a dedicated Ethernet back-end network. Each building fabric connects up to 20,736 GPUs using 51.2T switches, and a backend aggregation layer built on Arista 7800-series chassis with Broadcom Jericho3 silicon links sites from 2 km to more than 100 km apart.

To tolerate faults, each rack keeps 8 of its 72 GPUs as spares and about 2% of racks are held in reserve.

## Power and cooling

Synchronous training can swing cluster load by 30% to 40%, Meta says. It manages this with gradual power capping, rack battery backup units, capacitor trays and facility-level battery storage. Cooling combines air-assisted liquid cooling in free-air buildings with facility liquid cooling in the purpose-built AI building; the newest sites use closed-loop, direct-to-chip liquid cooling.

## What comes next

Meta said lessons from Prometheus will carry into Hyperion, a planned supercluster in Richland Parish, Louisiana, built with utility partner Entergy.
