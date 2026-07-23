# YC Application — OVERTURN  ◇ CONDITIONAL #2
### RFS category: AI-Native Service Companies
### Tagline (≤50 chars): "AI that overturns insurance denials for BH clinics."

> Status after 4 rounds: bigger MARKET than WARDEN, higher GATE. Fundable ONLY if the
> founder lands (a) a design-partner book with a measured automation rate and (b) a
> committed RCM operator (advisor-with-equity floor, cofounder ideal). Without those
> two, this reads as "a technical founder asking us to fund the hypothesis that the
> hard part is easy." Written to be maximally strong given the honest FMF gap.

---

## Describe what your company does in 50 characters or less.
We recover denied insurance claims for BH clinics.

## What is your company going to make?

OVERTURN is the AI-native billing back office for behavioral-health clinics — we don't
sell software, we *are* the team that fights insurance denials, staffed by agents and
paid only when the clinic gets paid.

~$260B of US claims are denied yearly; most is recoverable but ~half is never reworked
because appealing is slow, manual labor, so clinics write it off. Behavioral health is
hit hardest: high denial rates, fragmented small providers, no billing team big enough
to chase it all.

We connect at the **clearinghouse layer** (Availity/Optum — payer-facing, so we're not
hostage to any one EHR). Our agents read the payer's denial codes (CARC/RARC) *and* the
payer's own medical policy, draft the correct cited appeal, submit it, and track to
payment; a human RCM specialist reviews hard cases. The clinic pays 20–30% of what we
recover — nothing if we recover nothing.

We start on the **administrative** denials (auth-not-on-file, timely filing, coding —
CARC 197/16/29), which are near-fully automatable. The harder **medical-necessity**
bucket (argued on a clinician's narrative note) gets an AI-assembled packet with a human
sign-off. **We deliberately decline medical-necessity-heavy cohorts** that would drag us
toward BPO economics. North Star = automation rate (share of recovered *dollars* needing
no human), reported weekly; it's our go/no-go on every cohort.

## Why us? (founder-market fit — the honest, maximal version)

> This field decides the application. Fill it truthfully in this shape:
I'm not an RCM lifer and won't pretend to be — which is exactly why we chose a model
that pays us only when we're right. I've spent [N] years building [production LLM/agent
systems that did X at scale]. Denials recovery is fundamentally document-reasoning at
scale — read a CARC/RARC + a 90-page payer policy + a clinical note, produce a cited,
code-accurate argument — the exact thing I've shipped and the exact thing that became
possible in 2024. The domain knowledge I lack I'm buying honestly: **[name] spent [X]
years as [VP of RCM / denials lead] at [BH provider] and is [co-founding / advising with
equity]** and grades our appeals. Contingency is my forcing function — I don't get to
*claim* I understand BH denials; I only get paid when the payer agrees I did. In four
months I've read [N hundred] real denials and can tell you which three CARC codes drive
half of BH write-offs. That's not a lifetime of RCM — it's the fastest anyone without
one gets to the truth, and the model punishes me instantly if I'm wrong.
> Non-negotiables: (a) named equity-committed RCM operator; (b) a specific earned
> insight a non-expert couldn't fake; (c) contingency framed as epistemic forcing
> function. Without (a), this field stays a liability no wording fixes.

## Why now?
An LLM can now read a specific denial + the payer's full medical policy and produce a
correct, cited appeal — the task that used to need a trained biller and 20 min/claim.
Pre-2024 you threw offshore labor at it (the incumbent model). Now the labor is
automatable, flipping denials from a BPO cost center into a software-margin business —
for whoever builds the specialty data loop first.

## The margin question (services vs. software) — answered with numbers, not assertion
> The ONLY sentence that wins this, once you have a book:
"On our design-partner book, the administrative bucket — [58%] of recovered dollars —
closed at **[71%] zero-touch automation** and a **[34]-day cash-conversion cycle**, so
blended contingency gross margin is already **[61%]** and rises monthly as the outcome
dataset retires more human review; we decline margin-dilutive medical-necessity cohorts."
Real automation %, cash-conversion days, and blended gross margin — plus willingness to
*turn away* bad-margin work — is the only thing separating this from a Manila BPO with a
nicer UI. Without those numbers a partner correctly prices it as a services company.

## Working capital (a real weakness, answered)
Contingency = we front labor/compute now, collect a slice 30–120 days later on money
that may not arrive. We manage it three ways: (1) start on aged denials with short,
predictable cycles; (2) keep compute cost per appeal near-zero via automation so the
float we finance is small; (3) raise a modest recovery-financing facility only once the
cohort cash-conversion cycle is proven (~[34] days). We report cash-conversion cycle
alongside automation rate.

## Who are your competitors? Who do you fear most?
- **Rails / data owners:** Waystar, Availity, Optum/Change, R1 — own clearinghouse +
  payer data. **Note the real threat:** Optum owns a huge BH *provider* footprint, so BH
  is not a specialty they ignore. Our edge is a closed BH outcome-data loop + contingency
  service to fragmented providers they don't serve.
- **AI-RCM startups:** Adonis, Candid Health, Thoughtful AI, Infinitus, Anomaly; prior-
  auth: Cohere Health. Most sell software to big provider orgs; we run the service on
  contingency and compound BH-specific data.
- **Offshore BPOs** — labor, no learning loop.
- **Fear most:** a BH roll-up building in-house, or Adonis shipping a BH module before we
  compound a data head-start. Defense = specialty depth + speed + the data loop below.

## Moat
Not the appeal-drafting agent (anyone builds that). The **BH denial-outcome dataset** —
"this CARC from this payer for this CPT wins with this argument N% of the time" — used to
optimize argument selection against measured win rates. A loop offshore BPOs (no data)
and in-house billers (no scale) can't run. Compounds per specialty; why we go one
specialty deep.

## How do you make money? How big?
20–30% of recovered revenue. A $4M BH clinic denies ~$400K/yr, ~$120K recoverable-but-
abandoned, at 25% ≈ $30K/yr/clinic. Venture case is NOT thousands of tiny clinics — it's
**BH MSO/roll-up distribution** (one deal = 20–40 clinics) + rising ACV as we expand
denials → prior auth → full RCM. A few hundred clinics via a handful of MSO deals, with
automation carrying the margin. Endgame: the AI-native billing company for behavioral
health, then adjacent specialties.

## Solving the go-to-market circularity (MSOs want references; references need a book)
The wedge and the moat point at each other, so we sequence it: (1) **de-identified
historical denials first** — no live PHI, no BAA — to prove win-rate and automation rate
on real data with zero compliance gate; (2) sign ONE design-partner clinic whose
compliance officer we've already cleared, run live under their cover entity on their
clearinghouse creds; (3) use that book's recovered-dollars + automation number as the
reference that opens the first MSO pilot. We lead with a HIPAA risk assessment +
pen-test report a compliance officer can accept in week one — not a SOC 2 certificate
that's a year out (Type II is in observation now).

## Traction bar — the minimum for a YES (need ALL, with real numbers)
1. Design-partner book LIVE: ≥2 clinics or 1 small group, signed BAA, ≥~$150K in denied
   claims actually handed over (not promised).
2. Dollars recovered: ≥$25–50K actually recovered + invoiced (cycle closed to cash).
3. Measured automation rate: ≥60% zero-touch on ≥200 real administrative denials, weekly.
4. One real MSO conversation that reached "send us your data / scope a pilot."
5. RCM operator committed (advisor-with-equity floor; cofounder ideal).
Hit 1–3 + one of 4/5 → fundable. Hit none → it's a pitch deck.

## How will you get first users?
Contingency = easiest first sale in healthcare (zero buyer financial risk). Cold outreach
to practice managers/RCM directors at 10+ clinic BH groups and VPs of RCM at roll-ups
(SonderMind, Talkiatry, Array, Charlie Health, PE-backed regionals): "Hand me your denied
and written-off claims from the last 6 months — pure contingency, pay only on recovery,
I'll report the automation rate." Then the MSO channel: one deal = dozens of clinics.

## The experiment to run THIS WEEK
Get de-identified denials from one friendly clinic and run the agent on 100–200 real
cases to produce a measured administrative-bucket automation rate. In parallel, email 15
BH practice managers/RCM directors + 5 VPs of RCM at roll-ups asking for a contingency
book. **Kill signal:** 3 weeks, not one group hands over a book AND automation on real
denials sits <60% → the data-access wall + automation ceiling are fatal for a no-logo
team; the venture case collapses. **Go signal:** one book loaded + measured automation
≥60%.
