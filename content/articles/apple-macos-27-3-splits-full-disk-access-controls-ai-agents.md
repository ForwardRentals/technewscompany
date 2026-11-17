title: Apple Overhauls Mac Privacy Controls for Apps Requesting Full Disk Access as AI Agents Spread
dek: The changes, arriving with macOS 27.3, split the permission settings and add an indicator when one app controls another.
date: 2026-11-16
category: Security
company: Apple
source: TechCrunch|https://techcrunch.com/2026/11/16/apple-reveals-new-mac-security-controls-as-ai-agents-raise-privacy-risks/
image: /img/news/apple-macos-27-3-splits-full-disk-access-controls-ai-agents.jpg
image_credit: Daniel L. Lu (user:dllu) / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Aerial_view_of_Apple_Park_dllu.jpg
---
Apple announced on Monday, November 16, changes to how macOS handles apps that ask for broad system access, a move aimed at limiting the risk posed by AI agents, TechCrunch reported. The changes arrive with macOS 27.3.

## What changes

Apple had said in October it would revise the settings, after a journalist claimed Meta's Muse app read private messages without consent, which Meta disputes, and after a Wired report on a flaw in ChatGPT's Mac app that could have exposed sensitive data. According to TechCrunch, the new controls are:

- Two separate settings, "System & App Protection Override" and "Accessibility," replace the combined Device Control and Data Access settings; the first overrides built-in protections
- One permission method: users pick the requesting app from a list
- On-screen advice to grant Full Disk Access or the override only to apps that need it
- More visibility into what data an app will be able to reach
- An option to make apps ask each time they need access
- A new indicator when one app is controlling another through the override

## Developers

In a blog post Apple warned that "before granting an app such extraordinary access, users should understand that it puts all of the data on their Mac at risk." It advised developers to update onboarding and to have apps handle limited folder or app access gracefully. Apps that need Full Disk Access for backup or assistive technology can request exceptions, which Apple calls entitlements, to keep existing behavior.

## Context

The changes do not prevent users from installing AI agents or other apps that request elevated access; they add choices and information. TechCrunch noted that agents run on the user's device and can act across the operating system, files and apps, and that Apple has benefited from sales of Mac mini and Mac Studio machines bought by early adopters to run local models.
