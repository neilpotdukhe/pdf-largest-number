# YC Application — OVERTURN  (internal codename: DENIAL)
### RFS category: AI-Native Service Companies
### Tagline (≤50 chars): "AI that overturns insurance denials for BH clinics."

> Note to founder: OVERTURN's honest gate is a healthcare/RCM design partner + a
> first book of denied claims. This app is written to be submittable now, but the
> [bracketed] traction and any RCM-credibility you can add are what make it a yes.

---

## Describe what your company does in 50 characters or less.
We recover denied insurance claims for BH clinics.

## What is your company going to make?

OVERTURN is the AI-native billing back office for behavioral-health clinics — we
don't sell software, we *are* the team that fights insurance denials, staffed by
agents and paid only when the clinic gets paid.

~$260B of US medical claims are denied every year; most is recoverable, but roughly
half is never reworked because appealing is slow, manual, tedious labor. Clinics
simply write the money off. Behavioral health is hit hardest: high denial rates,
fragmented small providers, and no billing team big enough to chase it all.

We connect to the clinic's claims data at the clearinghouse layer (Availity/Optum —
payer-facing, so we're not hostage to any one EHR). For each denial our agents read
the payer's denial codes (CARC/RARC) *and* the payer's own medical policy, draft the
correct, cited appeal, submit it, and track it to payment. A human RCM specialist
reviews the hard cases. The clinic pays us 20–30% of what we recover — nothing if we
recover nothing.

We start with the ~60% of denials that are **administrative** (eligibility,
auth-not-on-file, timely filing, coding mismatches) — these are near-fully automatable
today. The harder ~40% (medical-necessity, argued on a clinician's narrative note)
get an AI-assembled appeal packet with a human sign-off. Our North Star metric,
reported from day one, is **automation rate** — the share of recovered dollars that
required no human. That single number is the difference between a software-margin
company and a billing shop, and we manage the business to it.

## Why did you pick this idea? Do you have domain expertise?

[Founder to add any real RCM/healthcare exposure — this is the load-bearing FMF field.
If you have a design-partner clinic or an RCM operator advising/co-founding, say so
here; it materially strengthens the app.]

We picked it because it's the rare "AI-native services" idea where the AI does the
actual expensive labor (reading a 90-page payer policy and writing a cited appeal in
seconds — impossible before 2024) *and* the sale is trivial: contingency pricing
means the clinic takes zero financial risk, so we can earn a first book of claims
without a brand. We know the pain is real because [design partner / interviews with N
BH practice managers / your own experience with ___].

## Why now?

The capability is brand-new: an LLM can now read a specific denial plus the payer's
full medical policy and produce a correct, code-accurate, cited appeal — the exact
task that used to require a trained biller and 20 minutes per claim. Pre-2024 you had
to throw offshore labor at this (that's the incumbent model). Now the labor is
automatable, which flips denials management from a BPO cost center into a
software-margin business — but only for whoever builds the specialty data loop first.

## Who are your competitors? Who do you fear most?

- **Incumbent rails / data owners:** Waystar, Availity, Optum/Change, R1 RCM — they
  own the clearinghouse and payer relationships and sit on more denial data than we
  ever will. But they sell horizontal breadth and have no incentive to go deep on one
  small specialty. We rent their rails and out-specialize them.
- **AI-RCM startups:** Adonis, Candid Health, Thoughtful AI, Infinitus, Anomaly, and
  prior-auth players like Cohere Health. Most sell software to big provider orgs; we
  run the service on contingency for fragmented BH providers and compound a
  BH-specific outcome dataset.
- **The offshore BPOs** we're really replacing — they have labor but no closed
  learning loop.
- **Who we fear most:** a BH roll-up (MSO) building this in-house, or Waystar shipping
  a BH denial module. Our defense is the specialty data moat below + speed.

## What's the moat?

The appeal-drafting agent is not the moat — anyone can build that. The moat is the
**behavioral-health denial-outcome dataset**: "this CARC from this payer for this CPT
wins with this argument N% of the time." We optimize argument selection against
measured win rates — a loop offshore BPOs (no data) and in-house billers (no scale)
can't run. It compounds per specialty, which is exactly why we go one specialty deep
instead of horizontal.

## How do you make money? How big can it get?

Contingency: 20–30% of recovered revenue. Unit math (conservative): a $4M BH clinic
denies ~$400K/yr, ~$120K is recoverable-but-abandoned, at 25% = ~$30K/yr revenue per
clinic. The venture case is NOT thousands of tiny clinics — it's **distribution
through BH MSOs/roll-ups** (one signature = 20–40 clinics) plus rising ACV as we
expand denials → prior authorization → full RCM for the specialty. Get to a few
hundred clinics via a handful of MSO deals and the automation rate carries the margin
to software-like levels. Expansion path: the AI-native billing company for all of
behavioral health, then adjacent specialties.

## How far along are you? Traction?

[Fill before submitting. Target strong-app state:]
- Built the denial→policy→cited-appeal agent; demo: feed a real denial + payer policy,
  watch it draft a submittable, cited appeal in seconds. [Demo video link]
- [First design-partner clinic/group or MSO handed us a contingency book of denied
  claims]; [$X recovered] at [Y%] automation rate on the administrative bucket.
- [N interviews with BH practice managers / VPs of RCM confirming the write-off pile.]

## How will you get your first users?

Contingency = the easiest first sale in healthcare. (1) Cold outreach to practice
managers/RCM directors at 10+ clinic BH groups and VPs of RCM at BH roll-ups
(SonderMind, Talkiatry, Array, Charlie Health, regional PE-backed groups): "Hand me
your denied and written-off claims from the last 6 months — I work them on pure
contingency, you pay only on recovery, and I'll report the automation rate back."
Zero financial risk to them. (2) The real unlock is the MSO/roll-up channel: one deal
= dozens of clinics.

## The single biggest risk (and how we retire it)
Two, named honestly. (1) **Automation-rate ceiling** — if BH medical-necessity
denials keep a human in the loop, margins stay BPO-shaped. Retirement: start on the
administrative bucket where automation is real, and only scale accounts/specialties
where the measured human-in-loop ratio is already collapsing; the automation rate is
our go/no-go on every cohort. (2) **Data-access/trust wall** — a no-name seed team
getting PHI + a claims book. Retirement: contingency removes the buyer's financial
risk, BAA + SOC 2 from day one, and land one design-partner book to generate the
references that open MSO doors.

## Why us (founder-market fit)
[Strongest if you can name RCM/BH credibility or an operator cofounder here.] We can
build the agent pipeline fast, and the contingency model lets us prove the automation
thesis on real claims before we scale — turning a services wedge into a data-moated,
software-margin company for one specialty we own end to end.
