title: Optimizely Confirms Hijacked Scripts Served Crypto-Swapper and Card Skimmer to Sites Including Zoom and GitLab
dek: StepSecurity says the "OPTIMJACK" campaign injected malicious JavaScript into customer projects on Optimizely's CDN on November 16, affecting roughly 178 organizations.
date: 2026-11-17
category: Security
company: Optimizely
source: StepSecurity|https://www.stepsecurity.io/blog/optimjack-optimizely-hosted-scripts-crypto-clipper-card-skimmer
image: /img/news/optimizely-hosted-scripts-hijacked-skimmer-optimjack-zoom-gitlab-salesforce.jpg
image_credit: Martin Vorel / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Programming_code.jpg
---
Optimizely has confirmed that an unauthorized party added malicious JavaScript to some customer projects on its Experimentation platform, which caused the company's content delivery network to serve the code to visitors of affected websites. Security firm StepSecurity, in a November 17 write-up, said the campaign it calls OPTIMJACK began on November 16 and touched 178 organizations.

## What happened

According to StepSecurity, the attacker inserted code into the "Project JavaScript" field of customer projects in Optimizely Web. Because the rest of each snippet was unchanged and still came from Optimizely's CDN, site owners' normal script allow-lists did not flag it. Researcher Scott Helme found the injected code in 188 of 1,611 snippets he checked.

StepSecurity listed affected sites including Zoom, Salesforce, GitLab, CNN, BBC, HSBC, KLM, Air France, IKEA and Equifax, and said Optimizely's own sites were also affected.

## The payload

- **Crypto swapper:** replaces copied wallet addresses with attacker-controlled ones when nearby text mentions payments.
- **Data exfiltration:** sends a screenshot of the page and cookies to the attacker's server after a swap.
- **Card skimmer:** captures card numbers, expiry dates and security codes from forms.
- **iOS stage:** Helme's analysis said it loads exploit kits on iPhones and iPads, which StepSecurity did not verify.

## Optimizely's response

Optimizely's status page said an unauthorized party "exploited a vulnerability in Experimentation and added malicious JavaScript to some customer projects." The company said it fixed the flaw, removed the injected code, ended sessions, revoked tokens, reset affected accounts and notified customers. StepSecurity reported that an Optimizely spokesperson told Gizmodo the flaw was in the account sign-up flow. Salesforce said it "will notify customers if it finds unauthorized access to their data."

## Impact so far

StepSecurity reported that the attacker's wallets were emptied on November 17, with estimated losses between roughly $2,300 and $7,040 depending on the source. The number of card details captured has not been reported.

Site owners can check scripts served through Optimizely for the attacker's domain, and because files were being cleaned on November 16, a clean result now does not prove a file was clean earlier. Figures come from StepSecurity and may change.
