# Round 0 — Top 5 Candidate Companies (against YC Summer 2026 RFS)

Founder assumption: strong technical founder(s), can ship full-stack + LLM/agent
systems fast, small team, US-based, can build an MVP now. Where founder-market fit
is load-bearing, it's flagged.

Selection logic: of the 15 RFS categories, the hard-tech ones (inference chips,
space electronics, lunar manufacturing, counter-swarm, semiconductor supply chain,
low-pesticide ag robotics) need capital/teams/regulatory access a modal technical
founder doesn't have. The software-buildable, RFS-blessed categories are:
AI-Native Service Companies, Company Brain, SaaS Challengers, Software for Agents,
AI OS for Companies, Dynamic Software Interfaces. My 5 picks come from there, each
narrowed to a *specific company*, not a category.

---

## #1 — DENIAL (RFS: AI-Native Service Companies)
**One-liner:** An AI-native denials-management + prior-authorization firm for
outpatient specialty clinics. We don't sell software — we *are* your billing back
office, staffed by agents, paid as a % of the revenue we recover.

- **Wedge:** Insurance claim denials. ~$260B in claims are initially denied
  annually in the US; ~60% are recoverable but ~half are never reworked because
  it's manual, tedious labor. Clinics eat the loss.
- **What we do:** Ingest the clinic's denied claims (via clearinghouse/EHR
  integration), agents read the payer's denial reason + the payer's own policy PDF,
  draft the appeal letter with the right clinical justification + CARC/RARC codes,
  submit, and track to payment. Human RCM specialist reviews edge cases.
- **Business model:** Contingency — 20–30% of recovered revenue. Zero risk to the
  clinic. We only get paid when they get paid.
- **Why now:** LLMs can now read a denial + a 90-page payer policy and produce a
  correct, cited appeal in seconds. Pre-2024 this was impossible.
- **Why us:** technical founder can build the agent pipeline; the "firm" model means
  we capture the whole margin, not a $500/mo SaaS seat.
- **Wedge → expansion:** denials → prior auth → full RCM → the AI-native billing
  company for a whole specialty (e.g., start with behavioral health or GI).
- **FMF risk:** need healthcare RCM credibility / a design partner clinic. HIGH.

## #2 — HARBOR (RFS: Software for Agents)
**One-liner:** Delegated authorization + scoped payments for AI agents — "let an
agent act on my accounts without giving it my password or my whole credit card."
The permission + payment rail agents use to transact with existing software.

- **Wedge:** Right now if you want an agent to book travel, buy parts, or manage a
  SaaS account on your behalf, you either hand it full credentials (insane) or it
  can't act. Harbor issues scoped, revocable, auditable delegated credentials +
  virtual single-use payment authority, with a policy engine ("max $500, only these
  merchants, needs my approval over $2k").
- **What we do:** (1) An agent-identity + delegation layer (OAuth-for-agents:
  human grants agent a scoped token). (2) Scoped payment issuance (virtual cards /
  pull-payment mandates). (3) A real-time policy + approval engine + full audit log.
- **Business model:** Interchange/fee on payment volume + per-seat for the policy
  console. Land with agent-builder startups, expand to enterprises deploying agents.
- **Why now:** "The next trillion users won't be people, they'll be agents." Agents
  can finally *do* things but the trust/payment substrate doesn't exist.
- **Why us:** technical founders can build auth+payments infra; this is a
  standards-adjacent land grab.
- **Risk:** Visa/Mastercard/Stripe + Skyfire/Payman are circling. Crowded, and the
  card networks may own the payment half. Need a wedge they can't/won't do fast.

## #3 — CORTEX (RFS: Company Brain)
**One-liner:** The executable knowledge layer for customer support & ops. We turn a
company's scattered tribal knowledge into *runnable* skills that agents execute —
not a search box, but the procedures themselves ("how we process a refund
exception," "how we escalate a Sev-1").
- **Wedge:** Support/CX first. Every support org has undocumented procedures living
  in senior agents' heads + old tickets + Slack. We mine resolved tickets +
  docs + Slack to synthesize step-by-step, executable procedures, keep them current
  as reality drifts, and expose them as skills the support agent (AI or human) runs.
- **Business model:** Per-seat + usage. Land in CX, expand to IT/ops/onboarding.
- **Why now:** LLMs can read 100k resolved tickets and induce the actual procedure
  (incl. the exceptions) — the thing nobody has time to document.
- **Risk:** Glean, Sierra, Decagon, every support-AI vendor claims adjacent ground.
  "Knowledge → executable skill" must be a real, defensible distinction, not a demo.

## #4 — MERIDIAN (RFS: SaaS Challengers)
**One-liner:** The AI-native agency management system (AMS) for independent
insurance agencies — a 10x cheaper, agent-run replacement for Applied Epic and
Vertafore AMS360, the hated, sticky, 20-year-old incumbents.
- **Wedge:** ~40,000 independent P&C agencies in the US run on legacy AMS software
  they despise (clunky, expensive, awful support). The AMS is the system of record:
  clients, policies, carriers, renewals, commissions, servicing. AI can now do the
  labor *inside* the system (data entry from carrier docs, renewal prep, certificate
  issuance, servicing emails) — so we sell a modern AMS where the software does the
  work, not just stores the record.
- **Business model:** Per-seat SaaS at ~1/3 incumbent price, expand via the labor we
  automate (usage/outcome pricing on servicing tasks).
- **Why now:** AI collapsed the cost of building + operating vertical software 10–100x;
  incumbents' moat (integrations + switching cost) is now attackable.
- **Risk:** switching cost is the whole game; data migration + carrier integrations
  are a slog; incumbents are entrenched. Distribution into 40k SMB agencies is hard.
- **FMF:** strongly rewards insurance-industry background.

## #5 — FLUX (RFS: Dynamic Software Interfaces)
**One-liner:** UI that assembles itself per user, per task, at runtime. A React-native
generative-UI runtime + SDK so any app can render the *right* interface for what the
user (or agent) is trying to do right now, instead of one static UI for everyone.
- **Wedge:** Start as the generative-UI layer for AI apps — agent produces intent +
  data, Flux renders a real interactive interface (forms, tables, controls), not a
  wall of chat text. Ship as an SDK/runtime + component protocol.
- **Business model:** Usage-based dev infra (per render / MAU) + enterprise.
- **Why now:** chat is a terrible UI for most tasks; models can now emit structured
  UI intent reliably; "generative UI" is becoming a real primitive.
- **Risk:** most speculative + most "vitamin." Vercel (v0), Thesys, and the frameworks
  themselves are moving here. Hard to show a burning customer wallet. Weakest of the 5.

---

## My prior going in (to be destroyed by the agents)
Rank: **#1 DENIAL > #4 MERIDIAN > #3 CORTEX > #2 HARBOR > #5 FLUX**.
Reasoning: DENIAL has aligned incentives (contingency = provable ROI, easy sale),
a real wound, and AI does the actual work. MERIDIAN is a classic "AI-native vertical
SaaS challenger" with a nameable enemy. HARBOR is the sexiest but most crowded/most
likely to be eaten by networks. FLUX is a feature, not a company (yet).

Open questions the adversarial partners must resolve:
1. For DENIAL: is contingency-services a venture-scale company or a lifestyle agency?
   Can it reach $100M ARR, or does it cap out as a services shop with services margins?
2. For MERIDIAN: can an outsider win 40k entrenched SMB agencies? Distribution?
3. For HARBOR: what's the wedge the card networks + Stripe won't do in 12 months?
4. Which 2 do we take to the final round?
