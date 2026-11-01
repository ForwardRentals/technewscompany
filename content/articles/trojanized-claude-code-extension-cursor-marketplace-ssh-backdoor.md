title: Trojanized Claude Code Extension on Cursor's Marketplace Tried to Plant SSH Backdoors
dek: A malicious build posing as Anthropic's extension was live for about 11 hours on October 29; researchers say the backdoor largely failed to open remote access.
priority: 5
date: 2026-10-30
category: Security
company: Anthropic
source: BleepingComputer|https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/
image: /img/news/trojanized-claude-code-extension-cursor-marketplace-ssh-backdoor.jpg
image_credit: Department for Science, Innovation and Technology / CC BY 2.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Secretary_of_State_Peter_Kyle_visits_Anthropic_in_San_Francisco._(54098999333).jpg
---
A trojanized version of Anthropic's Claude Code extension was distributed through Cursor's extension marketplace on October 29 and attempted to install persistent SSH backdoors on developers' machines, BleepingComputer reported on October 30.

## What happened

The malicious package, labeled version 2.1.313, was available for about 11 hours, from 2:27 a.m. to 1:35 p.m. Pacific Time, according to the report. Up to 5,000 developers may have been exposed, though no exact install count was given. Cursor said Anthropic did not create the extension. It remains unexplained how the attackers were able to publish it under Anthropic's name.

Researchers at Phorion and OpenSourceMalware analyzed the package. Attackers added a JavaScript loader to the start of the extension's main file and left the legitimate code unchanged, so it ran as soon as the extension loaded.

## What the code did

- Collected system details, including the Git email address and public IP address.
- Added an attacker-controlled SSH key and tried to enable SSH and a reverse tunnel.
- Set up persistence through a macOS LaunchAgent or a Windows scheduled task or startup script.
- Sent host information to a server at 134.209.82[.]225.

Phorion found the remote-access step mostly failed. On macOS, a check of the remote-login setting ran without elevated privileges and returned an error, so SSH was never switched on. On Windows, the routine to install an OpenSSH server was run through a shell that standard Windows lacks. The SSH key and persistence were still installed, but without a running SSH server the tunnel gave no access. Reconnaissance data, including usernames, hostnames and the names of environment variables tied to credentials, was still transmitted.

## Response and guidance

Cursor removed the extension and temporarily shut down its whole marketplace to audit other extensions and rotate access keys. It also worked with the hosting provider to take the attacker's server offline, and said it found no evidence that other versions or the official distribution were affected. Early reports that npm, Open VSX and Microsoft's VS Code Marketplace were also hit were later disputed.

Users are advised to look for an SSH key named `svc-telemetry`. If found, they should isolate the machine, rotate any accessible secrets, invalidate sessions and rebuild from safe backups.

BleepingComputer said it contacted Anthropic and Cursor; the article did not report an Anthropic response. Open questions include whether systems at either company were compromised.
