---
type: entity
title: "Project Glasswing"
status: mature
created: 2026-07-07
updated: 2026-07-07
tags:
  - fable5/model
  - note/entity
domain: model-and-family
confidence: evidence-based
related:
  - "[[Claude Mythos 5]]"
  - "[[Claude Fable 5]]"
  - "[[Mythos-Class Model Tier]]"
  - "[[Mythos 5 Access Criteria]]"
  - "[[Anthropic Plans and Access Tiers]]"
  - "[[Fable 5 Dual-Use Safety Measures]]"
  - "[[Fable Mythos Operating Doctrine]]"
  - "[[Fable Mythos 5 System Card]]"
  - "[[Anthropic]]"
source_urls:
  - "https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07)"
  - "https://www.anthropic.com/research/glasswing-initial-update (published 2026-05-22, retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07)"
  - "https://red.anthropic.com/2026/cvd/ (retrieved 2026-07-07)"
  - "https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07)"
---

# Project Glasswing

Project Glasswing is Anthropic's trusted-access defensive cybersecurity program for Mythos-class capability: it gives vetted defenders access to models and tooling that can find serious vulnerabilities faster than the security ecosystem can currently verify, disclose, and patch them.

## What it is

- A gated program announced 2026-04-07 to secure critical software before increasingly capable AI models can be misused against it.
- The original launch organizations were AWS, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks.
- Anthropic also said access had been extended to more than 40 additional organizations that operate or maintain critical software, later summarized as roughly 50 initial partners.
- The model first used for this work was Claude Mythos Preview, which Anthropic did not make generally available because of its cyber capability jump.
- [[Claude Mythos 5]] became the access-gated successor to Mythos Preview, while [[Claude Fable 5]] became the broadly available configuration with cyber and bio safeguards.
- The current program is not a normal account tier. It is an approval and trust program layered on top of account-team access.

## How it works

- Initial work centered on finding and fixing vulnerabilities in foundational systems, including local vulnerability detection, black-box binary testing, endpoint security, and penetration testing.
- Anthropic's disclosed workflow uses codebase mapping, scanning subagents, triage, reports, and threat-model building for prioritization.
- By 2026-05-22, Anthropic reported that it and roughly 50 partners had found more than 10,000 high- or critical-severity vulnerabilities.
- The same update says Cloudflare found 2,000 bugs, including 400 high- or critical-severity findings, while testing Mythos Preview.
- Anthropic also scanned more than 1,000 open-source projects. It reported 23,019 estimated total vulnerabilities and 6,202 estimated high- or critical-severity vulnerabilities.
- Of 1,752 high- or critical-rated findings assessed by independent security firms or Anthropic, 90.6 percent were valid true positives, and 62.4 percent were confirmed high or critical.
- The coordinated vulnerability disclosure dashboard reported 1,596 disclosed vulnerabilities across 281 open-source projects, 97 patched, and 88 assigned CVE or GHSA identifiers as of retrieval.
- The bottleneck changed: finding vulnerabilities became easier than verifying, disclosing, patching, and deploying fixes.
- On 2026-06-02, Anthropic expanded Glasswing to about 150 new organizations in more than 15 countries.
- The expansion added underrepresented sectors such as power, water, healthcare, communications, hardware, vendors, nonprofits, critical open-source maintainers, and safety testers.
- Anthropic says most partners are organizations where a successful attack on their codebase could affect more than 100 million people.
- The current Mythos page frames Mythos 5 access as a small but growing trusted-access program for cybersecurity and, soon, biology research.

## Best practice

- Treat Glasswing as a model-access governance system, not just a security project. EVIDENCE-BASED
- Use Fable 5 for general Mythos-class work and treat Mythos 5 as requiring prior approval, security review, and safety monitoring. EVIDENCE-BASED
- Do not infer approval criteria from the public partner list; Anthropic says new organizations must meet security requirements, but it has not published those requirements. EVIDENCE-BASED
- Center any Mythos workflow on triage and patch throughput, not just finding more bugs. EVIDENCE-BASED
- Record disclosure state for every vulnerability-like finding: found, reproduced, severity-assessed, disclosed, patched, advisory issued, and deployed. PRACTITIONER
- For ordinary defensive work blocked by Fable, check whether Opus or Sonnet through the Cyber Verification Program is the documented path before assuming Mythos access is relevant. EVIDENCE-BASED

## Pitfalls

- Treating the named launch organizations as the full membership. The launch page names 12 launch organizations and separately mentions more than 40 additional organizations.
- Counting Anthropic as an external founding partner. The launch list includes Anthropic itself.
- Treating the Cyber Verification Program as a Mythos 5 approval path. The current help article says it applies only to Opus and Sonnet class models.
- Measuring Glasswing success by findings alone. Anthropic's own updates make human verification, disclosure, and patching the rate limit.
- Using press reports for country names or approval details as if Anthropic confirmed them. The official expansion page says more than 15 countries but does not name them.
- Assuming Mythos Preview access continues unchanged. Current docs frame Mythos 5 as the successor and upgrade path for eligible users.

## Sources

- Project Glasswing, Anthropic: https://www.anthropic.com/glasswing (published 2026-04-07, retrieved 2026-07-07).
- Assessing Claude Mythos Preview's cybersecurity capabilities, Anthropic Frontier Red Team: https://www.anthropic.com/research/mythos-preview (published 2026-04-07, retrieved 2026-07-07).
- Project Glasswing: An initial update, Anthropic: https://www.anthropic.com/research/glasswing-initial-update (published 2026-05-22, retrieved 2026-07-07).
- Coordinated vulnerability disclosure dashboard, Anthropic: https://red.anthropic.com/2026/cvd/ (retrieved 2026-07-07).
- Expanding Project Glasswing, Anthropic: https://www.anthropic.com/news/expanding-project-glasswing (published 2026-06-02, retrieved 2026-07-07).
- Claude Fable 5 and Claude Mythos 5, Anthropic: https://www.anthropic.com/news/claude-fable-5-mythos-5 (published 2026-06-09, retrieved 2026-07-07).
- Claude Mythos product page, Anthropic: https://www.anthropic.com/claude/mythos (retrieved 2026-07-07).
- Real-time cyber safeguards on Claude Opus and Sonnet, Claude Help Center: https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet (retrieved 2026-07-07).

## Related

- [[Claude Mythos 5]] is the current access-gated successor model in the program.
- [[Claude Fable 5]] is the generally available same-weight configuration with safeguards.
- [[Mythos-Class Model Tier]] explains why this program exists as a capability governance layer.
- [[Mythos 5 Access Criteria]] tracks what is known and unknown about approval.
- [[Anthropic Plans and Access Tiers]] distinguishes subscriptions, API access, CVP, and Glasswing.
- [[Fable 5 Dual-Use Safety Measures]] documents the classifier layer that substitutes for Glasswing gating in general release.
- [[Fable Mythos Operating Doctrine]] turns the program evidence into operator rules.
- [[Fable Mythos 5 System Card]] is the primary safety source for Mythos 5 and Fable 5.
- [[Anthropic]] is the entity operating the program and updating access policy.

## Next actions

- Watch the Glasswing page for published security requirements, appeal paths, and biology access criteria.
- Track the CVD dashboard at each source refresh and record whether patch throughput improves.
- Add named country and partner expansions only when Anthropic confirms them or when press claims are explicitly labeled as press-only.
- Recheck whether the Cyber Verification Program expands beyond Opus and Sonnet.
- Add a Glasswing workflow checklist if the user wants a practical security-ops playbook.
