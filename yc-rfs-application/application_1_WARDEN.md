# YC Application — WARDEN
### RFS category: Software for Agents
### Tagline (≤50 chars): "The control plane for AI agents in production."

> Note to founder: bracketed [ ] fields are the things only you can fill — traction
> numbers, your bio, design-partner names. Everything else is written to submit.

---

## Describe what your company does in 50 characters or less.
Runtime control plane + audit log for AI agents.

## What is your company going to make?

WARDEN is the control plane companies install before they let AI agents touch
production. Today, when a team deploys an internal agent, that agent ends up holding
live API keys, database credentials, and prod access with no leash — it can do
anything the human who deployed it can, and nobody can prove afterward what it did.
That is a SOC 2 / ISO / incident-response nightmare, and it is happening at every
company shipping agents right now.

WARDEN sits between your agents and everything they touch and gives you four things:
1. **Scoped, revocable credentials** — agents get short-lived, least-privilege
   access issued per task, never your raw keys. Kill switch on every agent.
2. **A real-time policy engine** — "this agent may spend ≤$500, only call these
   tools, only touch these records; anything above that needs a human to approve."
3. **Human-in-the-loop approvals** — high-risk actions pause for a one-click approve
   in Slack/console instead of executing silently.
4. **A complete, replayable audit log of record** — every action every agent took,
   across every tool, queryable and exportable for your auditor. This is the piece
   nobody else has, and it's our moat: identity vendors capture *access granted*;
   we capture *actions taken across every system*, which is what compliance and
   incident response actually need.

You install it as a proxy/SDK in an afternoon (`npm install`, point your agent's
tool calls at us). It's model-agnostic and framework-agnostic — works with OpenAI,
Anthropic, LangGraph, CrewAI, custom loops, MCP servers, whatever.

## Why did you pick this idea? Do you have domain expertise?

We're building the thing we needed and couldn't buy. We [build/ship agent systems
in production / built internal agents at ___], and the moment an agent went past a
demo we hit the same wall: to make it useful we had to hand it real credentials, and
the second we did that, security and compliance (rightly) panicked. There was no
"Okta for the agent" — a way to give an agent scoped power and keep a provable record
of what it did. We are the exact users of this product, we speak the buyer's
language (platform + security engineers), and we can build the hard part — a
low-latency policy proxy and a tamper-evident action log — fast. This is the one
idea on our list with zero domain gate: it sells to our own tribe.

## Why now?

Two step-changes collided in 2025–26. (1) Agents crossed from demo to production —
companies now run internal agents in eng, ops, support, and finance that *take
actions*, not just generate text. (2) The number of non-human identities (service
accounts, agent credentials) has exploded past human identities, and auditors have
started flagging ungoverned agent access in SOC 2 / ISO reviews. The forcing
function isn't hype — it's the audit. You could not have sold this in 2022 because
agents didn't take real actions; you can't avoid it in 2026 because they do and the
auditor is asking.

## Who are your competitors? Who do you fear most?

We're clear-eyed that this is a live land-rush, and our edge is depth on the
agent-native workflow + the action-of-record, not being first.
- **Incumbents waking up:** Okta (announced identity for AI agents / cross-app
  access) and HashiCorp Vault (secrets) — our real long-term fear. Their advantage
  is distribution to the exact CISO we sell to. Our defense: they're identity/secrets
  companies; the *replayable cross-tool audit log* is a different, stickier surface
  their models don't naturally produce, and we get there first and deepest.
- **Adjacent startups:** non-human-identity/workload-identity players (Aembit,
  Astrix, Teleport-style access), LLM-security/guardrail startups (prompt-injection,
  runtime firewalls), and agent-observability tools (LangSmith, Langfuse) that log
  traces but don't *govern* or produce an audit-of-record.
- **Who we fear most:** Okta shipping "good enough" governance bundled free into a
  renewal. We beat that by owning the audit/compliance system-of-record — once your
  auditor runs on our log, ripping us out means losing your audit trail.

## What's new? What do people do today because this doesn't exist?

Today teams do one of three bad things: (a) hand the agent full credentials and hope,
(b) hard-code brittle per-agent guardrails by hand, or (c) refuse to ship the agent
to production at all (the most common — governance is the #1 blocker to agents in
prod). What's new: a single runtime layer that makes an agent *safe to deploy* and
*provable after the fact*, across any framework, with the audit log as a first-class
product rather than a side effect of observability.

## How do you make money? How big can it get?

Open-core. The proxy + basic audit SDK are open source (distribution + developer
trust). Paid tiers priced on usage (agents governed / actions audited) + enterprise
seats for the policy console, SSO, retention, and compliance exports. Land bottoms-up
with a platform engineer, expand to a security/platform team contract
([target] $2–5K/mo entry, $50–200K enterprise ACV).
Endgame: every company running agents needs a system of record for "what are our
agents allowed to do, and what did they do." If agents become the majority of
actors hitting internal systems, that control plane is infrastructure on the scale
of identity — a multi-billion-dollar seat at the center of every company's agent
stack. TAM = the security/identity budget line item that agents create.

## How far along are you? Traction?

[Fill with real numbers before submitting. Target state for a strong app:]
- Open-sourced the WARDEN proxy + audit-log SDK on [date]; [N] GitHub stars,
  [N] installs, [notable inbound].
- [N] design partners running it against real internal agents ([names/logos or
  "two Series B fintech/dev-tools companies"]).
- [First paid pilot / LOI], triggered by [their SOC 2 auditor flagging agent access].
- Demo video: [link] — show an agent try to exfil data / overspend, WARDEN blocks
  it, then replay the full audit log for an "auditor."

## How will you get your first users?

Developer-led. (1) Show HN / open-source launch of the proxy + audit log. (2) Direct
outreach to Heads of Platform/Security and staff platform engineers at Series B–D
companies we know run internal agents in prod (sourced from job posts for "AI
engineer, internal agent platform" + our network + YC network). Script: "Your agents
are holding live prod creds right now — want scoped creds + a full replayable audit
log before your next SOC 2?" No procurement wall, no BAA, no domain gate: we sell to
engineers, as engineers.

## The single biggest risk (and how we retire it)
Risk: "it's a feature Okta bolts on." Retirement: win the audit-of-record as a
standalone system of record fast, go deep on agent-native workflows the identity
incumbents won't prioritize, and make the OSS proxy the default install so we own
the developer relationship before the CISO gets the Okta upsell.

## Why us (founder-market fit, one paragraph for the "why will you win" question)
We are the buyer and the builder. We ship agent systems, we've felt this exact pain,
we can build a low-latency policy proxy + tamper-evident log, and we sell to
engineers without pretending to be someone we're not. Our whole moat strategy —
audit-of-record — is the boring, compliance-shaped surface that founders chasing the
sexy "agent identity" headline will under-build. We'll out-execute them on the part
that's sticky.
