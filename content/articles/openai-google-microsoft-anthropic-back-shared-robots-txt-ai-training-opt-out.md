title: OpenAI, Google, Microsoft and Anthropic Agree to Honor a Shared robots.txt Opt-Out for AI Training
dek: Websites will be able to refuse AI training across four major companies with a single entry, though only Anthropic has begun supporting it.
priority: 5
date: 2026-10-30
category: AI
company: OpenAI
source: Thurrott.com|https://www.thurrott.com/a-i/343407/anthropic-google-microsoft-and-openai-agree-to-let-sites-opt-out-of-ai-training
image: /img/news/openai-google-microsoft-anthropic-back-shared-robots-txt-ai-training-opt-out.jpg
image_credit: HaeB / CC BY-SA 4.0 via Wikimedia Commons|https://commons.wikimedia.org/wiki/File:Pioneer_Building,_San_Francisco_(2019)_-1.jpg
---
OpenAI, Google, Microsoft and Anthropic said on October 30 that they will support a common signal that lets website owners opt out of having their content used for AI training. Anthropic has already started implementing it. The other three plan to follow in 2027, according to Thurrott.com and AI Weekly, which cited The Verge's report.

## How the signal works

The mechanism is a robots.txt token, `__usage_ai-training`. A site adds it as a user-agent entry with a `Disallow: /` rule to opt out, with optional `Allow:` exceptions for specific paths, according to AI Weekly's summary.

- The token covers AI training only. The draft says it is not a directive about crawling, so search indexing and archiving are handled separately.
- It is described in an individual Internet-Draft, "Machine-Readable Training Preference Signal," dated October 30, 2026, which is being discussed in the IETF's AIPREF working group.
- The draft has no formal standing in the IETF standards process, and it is expected to be proposed as an international standard once complete, Thurrott reported.

## Company timelines

- **Anthropic:** already implementing support.
- **OpenAI:** says it "aims to implement the signal in the coming months."
- **Microsoft:** targets February 1, 2027, and plans a separate setting for AI grounding, the step where live web content is retrieved for chat answers.
- **Google:** targets 2027. Google's John Mueller said the token "will help websites express their AI training preferences across multiple AI providers in a single step."

## Limits

OpenAI described the effort as voluntary and called it a coordination mechanism rather than a security control, so scrapers that ignore robots.txt are unaffected. Updating the file also does not remove material already in existing datasets or trained models. Microsoft's Krishna Madhavan said publishers should not have to choose between being discoverable in Bing and deciding how generative models use their work.

Thurrott's Paul Thurrott called the change "largely symbolic," noting that the companies already used web content for training at large scale.

## Why it matters

Until now, publishers have had to maintain separate rules for each company's crawler. A shared token reduces that work, but its practical effect will depend on when each company ships support and how consistently it is honored.
