# Scoping audit of the precursor review literature

Supporting record for §1 and Table 1 of the article, and for the 1.31-fold value discussed at §4.1.

The article reports that of 297 full-text reviews of NAD⁺ precursors published 2020–2026, ten state that NAMPT is subject to product or feedback inhibition and none converts that statement into a quantity. This file holds the question, the search, the eligibility and coding rules, the per-record results, the sensitivity analysis and the limitations. The machine-readable record — the retrieved list with PMIDs, the per-record codes on all three axes, the adjudication notes, the term counts and the completed PRISMA-ScR checklist — is under `audit/` in this archive.

---

## 1. Question and reporting standard

The audit asks a single question: when a review of NAD⁺ precursors discusses the enzymes of the two branches, does it state that NAMPT is subject to product or feedback inhibition, and if so does it carry that statement into a quantity?

In PCC terms the population is the review literature on NAD⁺ precursors, the concept is the reporting of the NAMPT product-inhibition constraint, and the context is mammalian precursor supplementation. This is a scoping audit of what reviews state, not a synthesis of effect estimates; evidence is charted rather than appraised, and no risk-of-bias instrument applies.

Reporting follows the PRISMA extension for scoping reviews (PRISMA-ScR; Tricco et al., *Ann Intern Med* 2018;169:467–73). The completed checklist is at `audit/prisma_scr_checklist.csv`; the flow diagram is `figures/Figure_PRISMA_flow.eps`, with its counts at `audit/prisma_flow.csv`.

The protocol was not registered. The coding manual below was fixed after a pilot on 20 randomly drawn records (seed 2552), but before the full set was scored.

## 2. Search

PubMed was searched on 15 September 2026, with no language restriction:

```
((NAD[Title]) AND (nicotinamide OR niacin OR "nicotinic acid" OR NMN OR "nicotinamide riboside"))
AND review[pt] AND 2020:2026[dp]
```

The window opens in 2020 so that the audit covers the period after the principal precursor trials had reported. Publication type was restricted to *review* at the index level rather than by manual judgement, so that the sampling frame is reproducible from the string alone.

Verbatim string and the returned record list: `audit/retrieval_record.csv`.

## 3. Retrieval and eligibility

Records were mapped to PubMed Central; full text was fetched where open access permitted, and the remainder were sought through institutional subscription, prioritised by how NAMPT-centred the title and abstract were.

Records whose subject was non-mammalian NAD metabolism (plant, fungal, bacterial or protozoan), NAD kinase, or cofactor transport unrelated to precursor supplementation were coded ineligible **at the point of scoring** rather than screened out beforehand, so that the denominator remains the full retrieved set.

### Flow of records

| Stage | Records |
| --- | --- |
| Identified by the search string | 236 |
| Full text retrieved from PubMed Central | 150 |
| Full text retrieved by other means | 26 |
| Full text obtained, total (inhibition-axis denominator) | 176 |
| Full text not obtainable (abstract-level data only) | 60 |
| Coded ineligible on subject at scoring | 7 |

Percentages in Table 1 of the article are of 176.

## 4. Coding manual

Each full-text record was scored on two axes and one secondary axis. Scoring was by automated keyword screen followed by human adjudication of every flagged passage. The screen was deliberately over-inclusive: of the 21 passages it returned, 7 were adjudicated ineligible on subject (§6 below).

The screen ran over the 150 records whose full text came from PubMed Central. Of the 21 passages returned, 14 were adjudicated eligible — four naming NAMPT and ten the consuming enzymes. Three further eligible records were found among the 26 full texts obtained by other means, giving the five and the twelve of §5 and §6.

| Axis | Levels | Rule |
| --- | --- | --- |
| Inhibitor identity | NAD⁺ / nicotinamide / nicotinamide mononucleotide / none | The chemical species the text names as exerting the inhibition. A text that says only that the enzyme is "feedback-inhibited" without naming the species scores *none*. |
| Inhibited target | NAMPT (synthesis) / consuming enzymes / both / none | The enzyme the text says is inhibited. Statements about sirtuins, PARPs, CD38 or SARM1 score *consuming enzymes*, not NAMPT, however adjacent the sentences. |
| Carried into a quantity | yes / no | Scores *yes* only if the text converts the statement into a threshold, a ceiling, an inhibition-adjusted dose, or a criterion that published dose–response data could be tested against. Quoting an inhibition constant without using it scores *no*. |
| Secondary: branch stratification | A / B / B2 / C | **A**, NAD⁺ outcomes reported separately for acid- and amide-branch compounds; **B**, both branches named but outcomes pooled; **B2**, only amide-branch compounds discussed; **C**, "NAD⁺ precursor" treated as one category. Applied to the 32 records read in full duplicate (§7). |

The third axis is the one on which the audit turns. The first two exist to establish where the field places the inhibition when it mentions it at all.

Per-record codes: `audit/coding_manual.csv`, `audit/screen_adjudication.csv`.

## 5. Records stating inhibition of NAMPT

Five of 176: PMIDs 39026037, 36829935, 40926126, 36139711 and 42063312. **None scores *yes* on the third axis.**

| PMID | Source | Inhibitor named | How it appears |
| --- | --- | --- | --- |
| 39026037 | *Nat Rev Mol Cell Biol* 2024 | NAD⁺ | One clause: NAMPT is subject to feedback inhibition by NAD⁺, limiting the increase attainable through routes depending on the enzyme. |
| 36829935 | *Antioxidants* 2023 | NAD⁺ | One clause, as grounds for preferring the riboside: the NAMPT reaction is rate-limiting, energetically expensive and exposed to feedback inhibition by NAD⁺. |
| 40926126 | *Nat Aging* 2025 | Nicotinamide | A parenthesis in a table footnote defining efficacy tiers: metabolic bottlenecks, for example nicotinamide inhibits NAMPT. |
| 36139711 | *Antioxidants* 2022 | Nicotinamide mononucleotide | A hypothesis the authors mark unproven: high concentrations of the mononucleotide may feedback-inhibit NAMPT. |
| 42063312 | *Alzheimers Dement* 2026 | NAD⁺ | Only as the mechanism of a small-molecule NAMPT activator said to relieve NAD⁺ feedback inhibition. |

The inhibitor is NAD⁺ in three, nicotinamide in one and the mononucleotide in one. The statement occupies a clause, a footnote or a drug-mechanism column in every case.

Record list: `audit/records_stating_inhibition_search1.csv`.

## 6. Records placing the inhibition on the consuming enzymes

Twelve of 176: PMIDs 33353981, 33414897, 33028824, 32097708, 32411700, 39516787, 37503611, 35780654, 35888754, 35918544, 39492424 and 40516760.

In all twelve the inhibitor is nicotinamide and the targets are sirtuins, PARPs, CD38 or SARM1. The constraint is therefore not unfamiliar to the field; it is located downstream of the enzyme at which it acts on synthesis.

Seven further passages returned by the screen were adjudicated ineligible on subject: chloroplast phosphoglycerate dehydrogenase (34745158), yeast NAD homeostasis (34095234, 32092906, 35260986), mycobacterial *nadB* (33584600), NAD kinase (36512915) and pantothenate kinase in cofactor transport (35304818).

## 7. Naming asymmetry and the secondary axis

Counts are over the body text of each record as deposited in PubMed Central, excluding the abstract, the reference list and back matter, and cover both the abbreviation and the full enzyme name. The counting script is `count_enzyme_mentions.py`; its output is `audit/enzyme_mention_counts.csv`.

Across the 150 records, **NAMPT is mentioned 2,973 times against 517 for NAPRT, a ratio of 5.8 : 1**; 76 of those records (51%) never mention NAPRT. Counting the whole deposited text instead, including abstract and references, gives 4,893 against 741, a ratio of 6.6 : 1 — so the asymmetry is not an artefact of where the boundary is drawn.

Two reviews devoted to NAMPT pharmacology, neither of them in the audited set because neither carries *NAD* in its title, mention it 476 and 108 times and NAPRT 26 and 0 times respectively.

On the secondary branch-stratification axis, applied to the 32 records read in full duplicate: 4 scored A, 13 B, 11 B2 and 4 C. The A records are PMIDs 39026037, 40926126, 35888754 and 35918544. **This subset was selected for NAMPT centrality and is not representative of the 236.**

## 8. Limitations

Five.

1. Full text could not be obtained for 60 of the 236, so the inhibition axis is scored against 176. Were every one of those 60 to state the constraint, the proportion would not exceed 27%.
2. The full-text set is not a random subset, having been prioritised for retrieval by NAMPT centrality, which enriches for the statement being *present* rather than absent.
3. The keyword screen can only find inhibition that is stated in recognisable terms; a review that conveyed the constraint without any of the screened phrases would be missed.
4. The search required *NAD* in the title, which excludes reviews whose titles name a precursor but not the cofactor. §9 tests that restriction directly.
5. The two primary axes were scored by a single reader after the automated screen; only the 32 records of the secondary axis were read in duplicate.

The first two limits work against the result. The third could only inflate the count above zero on the third axis, and no record reached it.

## 9. Sensitivity analysis: the title restriction

The primary search requires *NAD* in the title. A second search of the same period, requiring instead a precursor term in the title and excluding records already identified, returned 191 reviews. Full text was obtained for 121 of them — 112 through PubMed Central and nine individually — and each was put through the same automated screen and human adjudication.

Five state the constraint; **none converts it into a threshold, ceiling or testable criterion**, and none applies it to the heterogeneity of precursor trials. The proportion stating it is 4.1% (5 of 121) against 2.8% (5 of 176) in the primary set. The title restriction changes how often the constraint is *stated*; it does not change how often it is *costed*.

Across the two sets the audit covers **297 full-text reviews**, of which ten state the constraint and none costs it.

| PMID | Source | Inhibitor named | How it appears |
| --- | --- | --- | --- |
| 38921475 | *Metabolites* 2024 | NAD⁺ | Two clauses: NAMPT is subject to feedback inhibition limiting its ability to elevate NAD⁺, and the mononucleotide bypasses it. |
| 39037422 | *FASEB J* 2024 | NAD⁺ and nicotinamide | Both named, then the failure of nicotinamide in older people attributed to falling NAMPT expression rather than to the inhibition. |
| 32450270 | *Exp Gerontol* 2020 | NAD⁺ | One clause, reading a fall in muscle NAMPT protein after riboside as negative feedback limiting synthesis. |
| 34684434 | *Nutrients* 2021 | NAD⁺ | One clause within a description of the rate-limiting step. |
| 33918226 | *Int J Mol Sci* 2021 | NAD⁺ | Only as the mechanism of a small-molecule NAMPT activator. |

Record list: `audit/records_stating_inhibition_search2.csv`.

### Notable negative records

Three reviews of the sensitivity set are worth naming because of what they set out to do.

- **PMID 37478182** (*Science Advances* 2023, 10,934 words) asks in its title what is really known about nicotinamide riboside supplementation in humans, and does not mention the inhibition.
- **PMID 37364580** (*Endocrine Reviews* 2023, 25,426 words) calls NAMPT the rate-limiting enzyme of the salvage pathway without saying what limits it, and shares an author with one of the five records of the primary set.
- **PMID 39116016** (*Critical Reviews in Food Science and Nutrition* 2025) is a meta-analysis of oral mononucleotide trials and does not mention it either.

## 10. Records discussed here but not cited in the article

[S1] Manickam R, Santhana S, Xuan W, Bisht KS, Tipparaju SM. Nampt: a new therapeutic target for modulating NAD⁺ levels in metabolic, cardiovascular, and neurodegenerative diseases. *Can J Physiol Pharmacol* 2025;103:208–24.

[S2] Bhasin S, Seals D, Migaud M, Musi N, Baur JA. Nicotinamide adenine dinucleotide in aging biology: potential applications and many unknowns. *Endocr Rev* 2023;44:1047–73.

[S3] Zhang J, Poon ETC, Wong SHS. Efficacy of oral nicotinamide mononucleotide supplementation on glucose and lipid metabolism for adults: a systematic review with meta-analysis on randomized controlled trials. *Crit Rev Food Sci Nutr* 2025;65:4382–400.

The first is the second of the two NAMPT-pharmacology reviews of §7, in which that enzyme is named 108 times and its acid-branch counterpart not at all. The second and third are additions from the second search of §9. Neither mentions the inhibition.

---

## 11. The one amide-branch marker that clears the line

This section answers the article at §4.1, where the 1.31-fold value is discussed.

In HEK293 cells, 5 mmol L⁻¹ nicotinamide raised NAD⁺ by about 30% — the single amide-branch entry in Figure 1 to the right of the line, and the series from which the worked example of Box 1 is computed. **Throughout the article this rise is treated as a genuine amide-branch response.** That is the assumption most favourable to the amide branch, and it is adopted deliberately: the elasticity it yields, η = 0.05, is therefore an *upper bound* on what the amide branch achieved in that experiment.

There is reason to think the true figure is smaller.

Those authors report that their nicotinamide preparation contained up to 0.05% nicotinic acid, which at that dose delivers roughly 2.5 µmol L⁻¹ nicotinic acid — above the 1 µmol L⁻¹ at which nicotinic acid alone significantly raised NAD⁺ in the same cells — and they caution that studies using nicotinamide above 10 mmol L⁻¹ must be read with that in mind.

The evidence is chemical rather than inferential: those cells accumulated nicotinic acid adenine dinucleotide (7.1 ± 2.7 pmol per 10⁶ cells), an intermediate only the acid branch produces, which was below the limit of detection at every micromolar nicotinamide dose.

We do not apportion the rise between the two branches, because the data do not permit it. We note only the direction: **any part of it attributable to nicotinic acid contamination lowers η further below the threshold of equation 2**, so the conclusion drawn in Box 1 is conservative with respect to this uncertainty.
