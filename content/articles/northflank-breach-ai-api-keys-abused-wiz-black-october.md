title: Northflank Breach Leads to Abuse of Customers' AI API Keys, Wiz Reports Wave of Incidents
dek: The cloud platform told users to assume environment variables were decrypted; Wiz counts at least nine October incidents at AI developer platforms.
date: 2026-10-31
category: Security
company: Wiz
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/northflank-security-breach-leads-to-abuse-of-customers-ai-api-keys/
image: /img/news/northflank-breach-ai-api-keys-abused-wiz-black-october.jpg
image_credit: BalticServers.com / CC BY-SA 3.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:BalticServers_data_center.jpg
---
Cloud deployment platform Northflank has told customers to rotate their credentials after a security breach led to unauthorized use of AI API keys stored on its service, BleepingComputer reported on October 31.

## What Northflank said

Northflank disclosed the incident on its status page on October 30, following a threat alert from cloud security company Wiz. Its first guidance was blunt: "Assume all environment variables have been decrypted. Disable/rotate all keys." It later said users had reported unauthorized use of AI API keys supplied to the platform.

According to the incident timeline, Wiz alerted Northflank at 11:43 UTC on October 30, engineers reviewed the alert a minute later, and a network policy patch followed, with further patches at 12:50 and 13:05. Northflank also enabled credential rotation for PostgreSQL, MongoDB, MySQL and Redis, and turned on audit logs for all customers, including free accounts.

Northflank has not said how the attackers got in, how many customers were affected, or whether credentials other than AI API keys were taken. It did not respond to BleepingComputer's questions before publication.

## Wider pattern

Wiz published a report titled "Black October for AI Developer Platforms" that counts at least nine incidents at such platforms this month, including Northflank, Railway, OpenCode, Warp and Lightning AI. Wiz said some attackers specifically sought environment variables holding AI service credentials, a practice known as LLMjacking, in which stolen keys are used to run models on another organization's account. In two cases Wiz investigated, compromised enterprise credentials were used for roughly 2.5 million Amazon Bedrock API calls, about $100,000 in usage. Wiz has not confirmed that one group is behind all nine incidents.

## Recommended steps

- Rotate all user-provided secrets stored in Northflank, including workload, secret-group and global secrets.
- Disable public access to add-ons where enabled.
- Review AI provider usage and billing logs for unexpected activity.
- Report suspicious usage to Northflank and the relevant AI providers.
