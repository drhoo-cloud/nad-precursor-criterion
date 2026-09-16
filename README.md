# Resting NAD⁺ sets the ceiling, not the dose — analysis code and audit record

Analysis code, literature-audit record and trial extraction for the review manuscript

> **Resting NAD⁺ sets the ceiling, not the dose: a quantitative criterion for vitamin B3 precursors across tissues**
> Sun Z\*, Nguyen TTM\*, Kim J-W, Wang X, Shin M-K, Yin C, Yim S-V, Yi T-H
> \* joint first authors
> Kyung Hee University, Republic of Korea, and Hubei University of Chinese Medicine, China

This repository is Supplementary Code S1 of that manuscript. It reproduces every
calculated value in the paper, carries the full coding record of the literature
audit behind Table 1, and generates Figures 1, 3 and 4.

No new experimental data were generated. Every input is taken from the published
sources cited in the manuscript and is listed in Table 2 and in Supplementary
Tables S1–S10.

## What the model says

Two terms. A **gain** bounded above by the resting concentration, and a
**penalty** with no lower bound:

```
A/A0 = G(N) · P(M)

G(N) = [N/(K_S+N)] / [N0/(K_S+N0)]        gain, relative to the resting state
P(M) = (1 + M0/K_i) / (1 + M/K_i)         penalty, relative to the resting state
```

from which follow the three quantities of §4.3:

```
G_max      = (K_S+N0)/N0                  the ceiling the tissue sets
M*         solves  G_max = (K_i+M*)/(K_i+M0)    above it, nothing restores baseline
eta_req(M) = M(K_S+N0) / [K_S(K_i+M)]     the threshold, and it climbs with M
M+         = K_S·K_i/N0                   where eta_req crosses unity
```

### Parameter dictionary — the single source of truth

Replacing this block regenerates every output consistently. These five values are
the rows above the rule in Table 2; everything else in the paper is arithmetic on
them.

| Symbol | Quantity | Value | Status |
|---|---|---|---|
| `K_S` | SIRT1 Michaelis constant for NAD⁺ | 29 µmol L⁻¹ | measured, one study |
| `K_I` | SIRT1 inhibition constant for nicotinamide (IC₅₀ = *K*ᵢ) | 175 µmol L⁻¹ | measured, same study, read from its figure panels |
| `N_UN` | nuclear free NAD⁺, unstressed | 100 µmol L⁻¹ | biosensor measurement |
| `N_DP` | nuclear free NAD⁺, depleted | 25 µmol L⁻¹ | assumed, fourfold fall |
| `M0` | resting intracellular nicotinamide | 30 µmol L⁻¹ | measured in murine tissues, not in keratinocytes |
| `ETA` | highest published elasticity | 0.34 | measured |

Sensitivity of every derived quantity to the contested inputs is tabulated in
`data/table_S1_sensitivity.csv` and `data/table_S2_KS_alternative.csv`. The
direction of every entry is invariant across the ranges swept there.

## Files

| File | What it is |
|---|---|
| `verify_values.py` | prints every derived number quoted in the manuscript, beside the value printed in the paper |
| `PharmRes_Figure1.py` | Figure 1 — every located measurement, by tissue, with the NAPRT column and the branch-and-state strip |
| `PharmRes_figures34.py` | Figures 3 and 4 from the model, and the separate panel files |
| `PharmRes_FigureS2_prisma.py` | Supplementary Figure S2 — the PRISMA-ScR flow of records |
| `count_enzyme_mentions.py` | reproduces the enzyme-naming counts of Table 1C from PubMed and PubMed Central |
| `PharmRes_GraphicalAbstract.py` | the graphical abstract |
| `data/` | the numerical tables of the supplementary material, as CSV |
| `audit/` | the scoping-audit record: PRISMA-ScR flow, coding manual, and the ten records that state the constraint |
| `figures/` | output written by the scripts (EPS, 600 dpi TIFF, PNG preview) |
| `requirements.txt` | tested dependency versions |
| `CITATION.cff`, `.zenodo.json` | citation and archive metadata |
| `VERIFICATION.md` | how to check each kind of claim in the paper, and where judgement was exercised |
| `UPLOAD_CHECKLIST.md` | what to verify before publishing a release, and what to update afterwards |

**Figure 2 is a hand-drawn pathway schematic and has no generating script.** Its
source values are in `data/figure2_trial_nodes.csv`.

Every figure the scripts write is placed in `figures/`, which is empty in the
repository and filled by running them.

## The literature audit

`audit/` holds the record behind Table 1 and §3. PubMed was searched for reviews
published 2020–2026 carrying NAD in the title with any vitamin B3 precursor term
(236 records, full text obtained for 176); a second search of the same period
requiring a precursor term in the title instead added 121. Across 297 full-text
reviews, ten state that NAMPT is subject to product or feedback inhibition, and
none converts the statement into a threshold, a ceiling or a testable criterion.

The search string in `audit/` reproduces the 236 records exactly, and the PubMed
Central mapping returns the same 150 full texts, so the retrieval step can be
repeated from the string alone.

| File | What it is |
|---|---|
| `prisma_flow.csv` | records at each stage, matching Supplementary Figure S2 |
| `coding_manual.csv` | the three axes and the rule applied to each |
| `records_stating_inhibition_search1.csv` | the five records of the primary search, with PMID and how the statement appears |
| `records_stating_inhibition_search2.csv` | the five of the second search |
| `prisma_scr_checklist.csv` | the completed PRISMA-ScR checklist, 22 items, with the location of each |
| `retrieval_record.csv` | all 236 records: PMID, PMC identifier, whether full text came from PMC, and the screen class |
| `enzyme_mention_counts.csv` | NAMPT and NAPRT mentions per record, body text and whole deposited text |
| `screen_adjudication.csv` | the 21 records the screen returned and the three found outside PMC: eligible or not, target named, and the reason for each exclusion |

## Reproducing

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 verify_values.py            # every derived number, against the paper
python3 PharmRes_Figure1.py         # Figure 1
python3 PharmRes_figures34.py       # Figures 3 and 4, and the panels
python3 PharmRes_FigureS2_prisma.py # Supplementary Figure S2
```

`verify_values.py` prints the manuscript's own value beside each computed one, so
a mismatch is visible without opening the paper. `VERIFICATION.md` sets out what
else can be checked and where judgement was exercised.

Figures are drawn at 190 mm (Elsevier full-page width) with 8 pt text, above the
7 pt minimum at final printed size, as vector EPS with a 600 dpi LZW TIFF
alongside. The scripts set `FONT = "Nimbus Sans"`, which is metric-compatible
with Helvetica and Arial; substitute a locally available equivalent if it is not
installed.

## Notes on scope

The model implements sirtuin-dependent output only. PARP1, CD38 and the redox
couples are not represented, and equation 1 omits the substrate inhibition of
NAMPT by nicotinamide, so its output is an **upper bound**: the entrance penalty
can only worsen it. This is stated in the manuscript and repeated here so the
code is not read as a complete model of NAD⁺ metabolism.

Neither η nor η_req is a measurement. Both are arithmetic — one on published
percentages, the other on the constants above — and neither carries an
experimental error term.

## Licence

Code is released under the MIT Licence (`LICENSE`). The manuscript text and
figures are subject to the publisher's terms. The CSV files under `data/` and
`audit/` are the authors' own extraction and coding record and are released under
the same terms as the code.

## Contact

Tae-Hoo Yi — drhoo@khu.ac.kr
ORCID [0000-0001-9369-6542](https://orcid.org/0000-0001-9369-6542)
