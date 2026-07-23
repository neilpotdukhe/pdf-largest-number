# Round 2 — Synthesis of Panel + Three Sharpened Finalists

## What the panel killed and why
- **FLUX** — 0/3. Vitamin, no wallet, Vercel/Thesys/frameworks absorb the primitive. DEAD.
- **CORTEX** — squeezed between Glean (knowledge) and Decagon/Sierra (resolution), who own
  its inputs and outputs. Survives only if narrowed to a regulated-procedure vertical.
  Parked, not advanced.
- **HARBOR as pitched** — the neutral payment rail is owned by Visa/MC/Stripe (payment
  margin) and the model labs (agent identity). Two partners independently repivoted it to
  enterprise agent governance → carried forward as WARDEN.

## The three finalists (each rebuilt around its mandated pivot)

---

### FINALIST A — DENIAL v2 (RFS: AI-Native Service Companies)
**The panel's unanimous problem:** default outcome is a $10–30M BPO-margin services shop,
not venture scale. Contingency = easy sale but services margins + working-capital drag +
thousands of tiny accounts.

**The v2 answer — three things must all be true, and I'll pitch it as an AI-native billing
company for ONE specialty, engineered for software margins:**
1. **Automation rate is the whole thesis.** We win only if agents do 90%+ of the appeal
   labor. So we pick ONE specialty (behavioral health — high denial rate, high volume,
   relatively standardized clinical justification, fragmented providers) and go deep, so the
   agents get to near-full automation on that specialty's denial patterns. We instrument and
   report automation rate as our North Star metric from day one.
2. **MSO/roll-up distribution, not clinic-by-clinic.** One signature with a behavioral-health
   MSO or practice-management group = 20–40 clinics. Kills the "3,300 tiny accounts" problem.
3. **Data moat = specialty denial-outcome dataset.** "This CARC from this payer for this CPT
   wins with this argument 73% of the time." Compounds per specialty; Waystar's generic data
   doesn't capture the specialty nuance.
**Expansion:** denials → prior auth → full RCM → the AI-native billing company for behavioral
health. **FMF gate:** need an RCM/behavioral-health design partner + credibility. Highest
domain gate of the three, but the easiest first sale (contingency = provable ROI).

**Answers to the three kill questions:**
- *(Integration at scale / Epic cuts you off):* We integrate at the clearinghouse layer
  (Availity/Optum), which is payer-facing and specialty-agnostic, not per-EHR; behavioral
  health skews toward a handful of EHRs (e.g., a few dominant ones), so integration surface
  is small. We never depend on one EHR vendor's goodwill.
- *(Services margin / BPO):* North-star = automation rate; we only scale accounts where the
  human-in-loop ratio is already collapsing. If a specialty can't hit high automation, we
  don't take it. We publish the margin curve to ourselves monthly.
- *(Payer adjudication ceiling):* True, recovery has a payer-set ceiling — which is *why* the
  data moat matters: we optimize argument-selection against measured win-rates, beating both
  offshore BPOs (no data loop) and in-house staff (no scale of data).

---

### FINALIST B — MERIDIAN v2 (RFS: SaaS Challengers)
**The panel's problem:** best business model of all five, but (a) rip-and-replace migration
wall (carrier/IVANS download integrations) has killed every prior "modern AMS," and (b)
distribution into 40k conservative SMB agencies is a decade-long field war gated on insurance-
native relationships the founder doesn't obviously have.

**The v2 answer — LAND ON TOP, don't rip-replace (both Dalton & Jared demanded this):**
1. **Wedge = AI servicing layer on top of Applied Epic / AMS360, zero migration.** We connect
   to their existing AMS and automate the *labor*: renewal prep, ACORD-form data entry from
   carrier docs, certificate issuance, servicing-email drafting, endorsement processing.
   First sale is pure ROI ("we give each CSR back 10 hrs/week"), no switching cost, no fear.
2. **Distribution = agency networks/clusters/aggregators** (SIAA, Smart Choice, Keystone,
   PIA), each representing hundreds–thousands of member agencies. One network endorsement =
   200 agencies. This is the ONLY realistic channel and it's gated on FMF.
3. **Land-and-expand into the system of record.** Once we run the servicing labor and have
   accumulated the carrier-doc + servicing dataset (and quietly built carrier download), we
   flip agencies to our AMS as system of record — now sticky, on our terms, migration de-risked.
**ACV story:** start ~$10–20K on servicing automation (outcome-priced on labor), expand into
the full AMS seat + labor budget. Software margins, expanding ACV, structurally the healthiest
P&L. **FMF gate:** MANDATORY insurance-native co-founder or signed network channel partner.
Without it, uninvestable-by-this-team. Highest business quality, highest FMF requirement.

---

### FINALIST C — WARDEN (RFS: Software for Agents) [repivot of HARBOR]
**Origin:** two partners independently rebuilt HARBOR into this. Drop the neutral payment
rail entirely (Visa/Stripe/labs own it). Build the governance/security surface they won't.

**One-liner:** Okta + Vault + FinOps for AI agents. The control plane that lets a company
deploy agents into production without a security/audit nightmare — scoped, revocable,
human-in-the-loop-approval credentials + real-time policy + spend limits + a complete,
replayable audit log of every action every agent took.

**Why this is the fundable version:**
1. **Burning wallet TODAY.** Every company deploying internal agents (which is now every
   company) has agents holding live API keys, DB creds, and prod access with no leash. That
   is a SOC2 / ISO / audit / incident-response nightmare *right now* — not a bet on future
   agentic commerce. Security/platform teams have budget for exactly this.
2. **Pure technical FMF — no domain gate.** A strong technical founder builds this tonight.
   The most "fundable-on-day-one for this founder" of all candidates (Garry's whole point).
3. **Not eaten by networks/labs.** We don't move money or mint agents — we govern them. We
   sit on top of Stripe/Visa (spend governance) and on top of OpenAI/Anthropic (identity),
   as a *buyer* of those, not a competitor. The governance/audit/compliance surface is
   exactly the boring, budgeted layer the platforms won't prioritize.
4. **Moat:** the policy graph + audit dataset + integrations into every enterprise tool the
   agent touches = switching cost once you're the system of record for "what are our agents
   allowed to do and what did they do." Compliance/audit stickiness is durable.
**Wedge:** land with mid-market companies deploying agents in ops/eng/support; sell to the
platform/security lead. Expand to enterprise. Payments/spend-authority is a *later* feature
riding whatever rail wins. **Risk:** could be a feature Okta/Vault bolt on — must own the
agent-native workflow deeply and fast before they wake up.

---

## The strategic tension the finals must resolve (drives which 2 we pick)
- **WARDEN** = best FMF for a generic technical founder, real budget today, no domain gate,
  but "could be a feature" and newest category (execution race vs. Okta/incumbents waking up).
- **MERIDIAN** = best business model + clearest enemy + best "why now," but MANDATES an
  insurance-native co-founder/channel; uninvestable without it.
- **DENIAL** = realest wound + easiest first sale + provable ROI, but margin thesis is
  unproven and needs healthcare RCM credibility.

**Decision rule for the mock-interview round:** the finalist survives only if its ONE gating
question is answerable with phone calls, not code (Jared's closing point). For each:
- WARDEN: "does a mid-market platform lead say 'yes, I'd pay for this today'?" (10 calls)
- MERIDIAN: "can you land an insurance network/cluster channel partner + co-founder?" (10 calls)
- DENIAL: "will an RCM/MSO give you a book to prove >90% automation?" (10 calls)

Whichever two have the most credible "yes" path for THIS founder become the final 2.
My going-in read for a generic strong-technical founder with no stated domain: **WARDEN is the
day-one company; MERIDIAN is the highest-ceiling company IF the co-founder exists; DENIAL is
the middle.** Mock interviews to decide the final two.
