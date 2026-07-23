# YC Application — WARDEN  ★ PRIMARY
### RFS category: Software for Agents
### Tagline (≤50 chars): "The control plane for AI agents in production."

> Status after 4 rounds of adversarial review: the strongest application for a
> technical founder, because founder-market fit is provable here, not borrowed.
> Bracketed [ ] fields are the real traction/bio only the founder can supply — but
> §"Traction bar" states exactly what has to be true for this to be a YES.

---

## Describe what your company does in 50 characters or less.
Runtime control plane + audit log for AI agents.

## What is your company going to make?

WARDEN is the control plane companies install before they let AI agents touch
production. Today, when a team ships an internal agent, that agent ends up holding
live API keys, database credentials, and prod access with no leash — it can do
anything the human who deployed it can, and nobody can prove afterward what it did.
That's a SOC 2 / incident-response nightmare, and right now it's the #1 reason agents
stall in "pilot" and never reach production.

WARDEN gives four things:
1. **Scoped, revocable credentials** — agents get short-lived, least-privilege access
   issued per task, never your raw keys. One-click kill switch per agent.
2. **A real-time policy engine** — "this agent may spend ≤$500, call only these tools,
   touch only these records; anything above needs a human."
3. **Human-in-the-loop approvals** — high-risk actions pause for a one-click approve in
   Slack/console instead of executing silently.
4. **The audit log of record** — every action every agent took, across every tool,
   tamper-evident and replayable, exportable for your auditor.

**Deploy modes (this is a real engineering answer, not a hand-wave):** you can run
WARDEN as an inline proxy or as a sidecar/SDK. Most teams start with the SDK wrapping
their tool-call layer — no new network hop, ~single-digit-ms overhead, and it
**fails open** on the enforcement path with async logging, so WARDEN can never take
down prod. Teams that want hard enforcement graduate to the inline proxy in
**fail-closed** mode for their highest-risk agents. Model- and framework-agnostic:
OpenAI, Anthropic, LangGraph, CrewAI, MCP servers, custom loops.

## What's open source vs. paid (the monetization boundary)?

Open source is the **single-agent** proxy/SDK and a **local, ephemeral** log — enough
to govern one agent and win the developer. We monetize the moment governance goes
**multi-agent and multi-team**: the centralized, tamper-evident, cryptographically
attested **log of record** — with retention, replay, cross-tool correlation, and
auditor-export — lives only in the hosted/enterprise tier. The OSS log is per-agent
and local; the compliance system-of-record is centralized and immutable, and it's
ours. You can self-host to try. You cannot pass a SOC 2 on the free tier. That's the
paywall, and it's the same line every account crosses the first time an auditor asks
"show me what your agents did."

## Why did you pick this idea? Do you have domain expertise?

> [Founder: make this specific and true. Template below is the shape that lands.]
At [company] I built the internal agent platform that [N] engineers used to run
[specific workflow — e.g., automated infra remediation / data pipelines] in
production. I personally handed those agents scoped cloud credentials and then spent
[weeks] hand-rolling an approval-and-audit layer because nothing existed to buy — that
hacked-together system is the seed of WARDEN. I've been the platform engineer who gets
the "you gave an agent prod access?" message from security. I'm building the tool I
already tried to build once internally and shouldn't have had to. This is the one idea
where I'm the buyer, the builder, and the user — no domain gate.

## Why now?

Two step-changes collided in 2025–26. (1) Agents crossed from demo to production —
they now *take actions* in eng, ops, support, and finance, not just generate text.
(2) Non-human identities have exploded past human identities, and SOC 2 / ISO auditors
have started writing findings on ungoverned agent access — a real access-control
(e.g. SOC 2 CC6.x) finding when an agent holds a standing prod credential. The forcing
function isn't hype, it's the audit. Impossible to sell in 2022 (agents took no real
actions); impossible to avoid in 2026 (they do, and the auditor is asking).

## Who are your competitors? Who do you fear most?

We're clear-eyed that this is a live land-rush; our edge is depth on agent-native
workflow + the action-of-record, not being first.
- **Runtime owners (our biggest existential threat):** MCP, the OpenAI Agents SDK /
  AgentKit, and LangGraph Platform are building tool-permissioning and human-approval
  primitives into the runtime we plug into. If approvals go native to the framework,
  a thin proxy is disintermediated. Our answer: the cross-tool, cross-framework *audit
  system of record* is exactly what a single runtime can't own — it spans all of them.
- **Hyperscaler IAM:** Microsoft Entra Agent ID, AWS Bedrock AgentCore, Google — each
  shipping agent identity with distribution to our exact CISO. The "good-enough free
  bundle" risk is more likely to come from here than from Okta.
- **Identity/secrets incumbents:** Okta (identity for AI agents), HashiCorp Vault,
  Aembit/Astrix/Teleport (non-human & workload identity) — capture *access granted*,
  not *actions taken*.
- **Compliance-automation:** Vanta / Drata own the auditor relationship today; the
  natural place agent-governance evidence gets bolted on. We integrate with them and
  become the agent-action feed their audits consume.
- **Observability:** LangSmith / Langfuse log traces but don't govern or produce an
  audit-of-record.
- **Who we fear most:** the runtime owners making governance native. We beat it by
  owning the boring, cross-tool compliance system-of-record before they extend past
  their own walls.

## What's new? What do people do today because this doesn't exist?

Today teams (a) hand the agent full credentials and hope, (b) hand-code brittle
per-agent guardrails, or (c) refuse to ship to production at all (most common). What's
new: one runtime layer that makes an agent *safe to deploy* and *provable after the
fact*, across any framework, with the audit-of-record as a first-class product rather
than a byproduct of tracing.

## How do you make money? How big can it get?

Open-core, land dev-led / expand security-led. The **conversion trigger is concrete**:
a free proxy install becomes a paid contract the first time the team needs multi-agent
governance or an auditor asks for the action log — SOC 2 season is the mechanized
forcing function, not a vibe. Entry [$2–5K/mo], enterprise ACV [$50–200K] with the
console, SSO, retention, and compliance exports. Endgame: every company running agents
needs a system of record for "what are our agents allowed to do, and what did they do."
If agents become the majority of actors hitting internal systems, that control plane is
infrastructure on the scale of identity — a multi-billion-dollar category seat.

## Traction bar — what must be TRUE for this to be a YES (governance infra sells on evidence, not stars)
1. **2–3 design partners running WARDEN in production** (not demos) against real
   internal agents — crisp descriptors even if unnamed (stage, eng headcount, what the
   agents do).
2. **≥1 paid pilot or signed LOI** (even $1–2K/mo) — the thesis is that this is a budget
   line; a partner who won't pay undercuts it.
3. **The auditor anecdote, real and specific:** one named framework control (SOC 2
   CC6.x), one real finding ("agent held a live Postgres credential"), WARDEN's log
   closing it. This single anecdote is worth more than any usage metric — it makes the
   moat present-tense. **Lead with it.**
4. OSS as *supporting* evidence only: meaningful weekly installs + one notable inbound
   company. Not raw star count.
Not enough: OSS launch + stars + "lots of inbound" + zero paid usage.

## How will you get your first users?
Developer-led. (1) Show HN / OSS launch of the proxy + audit log. (2) Direct outreach
to Heads of Platform/Security and staff platform engineers at Series B–D companies we
know run internal agents in prod (sourced from "AI engineer, internal agent platform"
job posts + our network + YC network). "Your agents are holding live prod creds right
now — want scoped creds + a full replayable audit log before your next SOC 2?" No
procurement wall, no BAA, no domain gate: we sell to engineers, as engineers.

## Biggest risk (and how we retire it)
Risk: it's a feature a runtime owner or Okta bolts on. Retirement: own the cross-tool
audit-of-record as a standalone compliance system-of-record fast; make the OSS proxy
the default install so we own the developer relationship before the CISO gets the
upsell; go deep on agent-native workflows the identity/runtime incumbents won't
prioritize because they're busy defending their own surface.

## The experiment to run THIS WEEK
Ship the OSS proxy + audit log (Show HN). In parallel, email 15 Heads of
Platform/Security at companies known to run internal agents: "Are your agents holding
live prod creds right now? Would you pay for scoped/revocable creds + a full replayable
audit log before your next SOC 2?" **Kill signal:** <3/15 say "live problem, I'd pay
this quarter" AND the OSS drop draws no real installs → pain is 12 months early.
**Go signal:** 3+ paid-pilot yeses or genuine OSS inbound.
