title: Notion Says Breach at AI Vendor Fireworks Exposed Chat Transcripts From Under 1% of Users
dek: The transcripts came from a Notion AI analytics dataset held by Fireworks AI, which confirmed on November 8 that customer data had been accessed.
date: 2026-11-11
category: Security
company: Notion
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/notion-says-fireworks-breach-exposed-customer-ai-chat-transcripts/
---
Notion has disclosed that a breach at its AI infrastructure provider, Fireworks AI, exposed Notion AI chat transcripts from a small number of workspaces, BleepingComputer reported on November 11. Notion said fewer than 1% of its users are affected.

## What happened at Fireworks

Fireworks runs some open-weight models for Notion AI and analyzes stored conversations for an Insights feature that gives workspace admins visibility into how teams use AI. BleepingComputer reported two earlier Fireworks incidents:

- **Early October:** hackers accessed environment variables holding API keys and tokens for a limited number of accounts.
- **October 23:** an attacker reached Fireworks' development environment through a third-party cloud provider, exposing resource metadata, billing information, model weights and datasets for some customers.

## Notion's timeline

- **November 2:** Fireworks alerted Notion to an exposed dataset that Notion initially understood held only synthetic test data.
- **By November 3:** Notion cut traffic to Fireworks, deleted its data from the vendor's systems and halted training runs.
- **November 8:** Fireworks confirmed customer data, including Notion users' data, had been accessed.

## What was exposed

The affected material was AI chat transcripts from the Insights dataset, which Notion has since disabled. Notion said the transcripts were unattributable for the vast majority of impacted workspaces, meaning they were not labeled with an author or workspace, and that they did not contain tool-call results. Notion said Fireworks had contractually committed to zero data retention for its data.

## What users should do

- Workspace owners can review exposed data through Security incident review in Notion's desktop or web app and share a download link with members.
- Anyone who entered passwords, API keys or other credentials into affected chats should rotate them.
- Users who received no notice from Notion or their workspace owner need take no action for now, according to Notion.

The incident adds to a series of recent disclosures involving AI vendors' infrastructure; Fireworks has also been in the news this month after Meta's chief strategy officer left to become its CFO.
