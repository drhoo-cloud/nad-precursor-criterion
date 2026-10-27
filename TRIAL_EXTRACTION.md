# The five human trials of Figure 2: identification, coding and node-by-node record

Supporting record for §3.3 of the article and for Figure 2. The machine-readable version of the table below is `data/figure2_trial_nodes.csv`; the same values on a single logarithmic scale are `figures/Figure_trial_nodes_log.eps`.

---

## 1. Search

PubMed, 15 September 2026:

```
("nicotinamide riboside"[tiab] OR "nicotinamide mononucleotide"[tiab])
AND humans[mh]
AND (muscle biopsy[tiab] OR skeletal muscle[tiab] OR skin biopsy[tiab])
AND NAD[tiab]
```

The search is deliberately narrow: it asks only for human studies that went as far as sampling tissue, because the question is what happens in tissue rather than what happens in blood. It returned 33 records.

## 2. Eligibility

A record was eligible if it

1. reported original human data,
2. administered an amide-branch precursor — nicotinamide, its riboside or its mononucleotide, and
3. reported NAD⁺ measured in a tissue sample against a comparator.

Five records met all three.

The 28 excluded were: reviews and meta-analyses (6), animal or cell studies (5), human studies not measuring tissue NAD⁺ (12), a study measuring whole blood only (1), a trial combining the precursor with coenzyme Q10 so that the precursor's contribution cannot be separated (1), a two-page journal-club commentary carrying no new data (1), a protocol without results (1), and one record already cited for a different purpose (1).

## 3. Node coding

Each eligible trial was coded on seven nodes:

| Node | What counts |
| --- | --- |
| Substrate | tissue nicotinamide |
| NAMPT | protein or transcript |
| Acid-branch intermediate | nicotinic acid adenine dinucleotide, nicotinic acid mononucleotide, nicotinic acid riboside |
| Methylated products | methylnicotinamide and the pyridone carboxamides |
| NAD⁺ in tissue | measured in a tissue sample |
| NAD⁺ in blood | whole blood or PBMC |
| Sirtuin output | protein acetylation |

A node was coded as **measured** only where the trial reported its own measurement with a result. Mentions of other studies' findings in introduction or discussion were not counted, and a metabolite reported as below the limit of quantification was recorded as *measured* rather than *absent*.

Coding was performed against the full text of each trial. Every value in the table below was taken from a complete sentence in the results rather than from a figure, with one stated exception: the methylated-product fold-changes for Elhassan 2019, which are read from its figure panels because its text gives the direction but no number.

## 4. Node-by-node record

An em dash means the node was not measured.

| Trial | Compound, dose, duration, n | Substrate (NAM) | NAMPT | Acid-branch intermediate | Methylated products | NAD⁺ in tissue | NAD⁺ in blood | Sirtuin output |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Elhassan 2019 | NR 1 g/d, 21 d, 12 | 92.0 vs 86.5 pmol mg⁻¹, P = 0.96 | mRNA unchanged | NAAD 2.09× (P = 0.004); blood 4.5× (P < 0.001) | MeNAM 4.14×, Me-2-py 6.00×, Me-4-py 5.33× | 210 vs 197 pmol mg⁻¹, P = 0.22 | 47.75 vs 20.90 µmol L⁻¹, P < 0.001 | Pan-acetylation unchanged |
| Dollerup 2020 | NR 2 g/d, 12 wk, 40 | — | Protein −14%; mRNA unchanged | — | — | Unchanged, interaction P = 0.10 | — | Pan-acetylation, SIRT3, PGC-1α unchanged |
| Remie 2020 | NR 1 g/d, 6 wk, 13 | Not separable from the paper's abbreviation | — | NAAD +677%, P < 0.01 | MeNAM +299%, P < 0.01 | 1.019 vs 1.125 nmol mg⁻¹, P = 0.34; MS assay P = 0.91 | — | — |
| Stocks 2021 | NR 1 g/d, 7 d, 8 | Unchanged, P = 0.265 | mRNA unchanged | NaMN P = 0.003; NAR P = 0.002 | Me-2-py and Me-4-py P = 0.002 each; MeNAM unaffected by NR | Unchanged, P = 0.093 | — | Total, p53 K382 and MnSOD K122 acetylation unchanged |
| Yoshino 2021 | NMN 250 mg/d, 10 wk, 25 | Unchanged (arbitrary units) | — | — | MeNAM, 2PY and 4PY increased | Unchanged | PBMC content increased; 240-min AUC +43%, P < 0.01 | — |
| **Measured / 5** | | 3 | 3 | 3 | 4 | 5 | 2 | 3 |
| **Direction** | | None rose | Protein fell in 1; transcript unchanged in 3 | All rose | All rose | None rose | Both rose | None changed |

### Conventions and caveats

- **Units.** Elhassan 2019 prints its blood NAD⁺ and blood nicotinamide concentrations in mM. They are given here in µmol L⁻¹, the only physiologically possible reading; the slip is the source's rather than ours.
- **Figure-read values.** The methylated-product fold-changes for Elhassan 2019 are read from its figure panels. Every other value in the table is quoted from text or a table of its source.
- Where a trial reported only a P value and a direction, that is what appears; where it reported concentrations, both are given.
- Elhassan 2019 measured muscle and whole blood in the same twelve participants.
- Remie 2020 defines *NAM* in its figure legend as nicotinamide adenosine mononucleotide rather than nicotinamide, so its substrate cell is left unresolved.
- Yoshino 2021 reports muscle metabolites in arbitrary units, so no fold-change can be derived.
- In Elhassan 2019, muscle nicotinic acid riboside and nicotinamide mononucleotide were below the limit of quantification, which is not the same as unmeasured; urinary nicotinic acid riboside rose 18-fold (P = 0.001) in the same trial.

**Abbreviations.** NAM, nicotinamide; NaMN, nicotinic acid mononucleotide; NAR, nicotinic acid riboside; NAAD, nicotinic acid adenine dinucleotide; MeNAM, methylnicotinamide; Me-2-py and Me-4-py, the corresponding pyridone carboxamides.

## 5. Limits

Five trials is a small denominator, and the narrow search will have missed human studies that measured tissue NAD⁺ without the terms above in title or abstract.

Two of the five share authors, so the acid-branch observation rests on two independent groups rather than three.

None of the five was designed to test the criterion of §5. The coding records what they measured, not what they set out to show.

---

## 6. Human tissue rows added to Figure 1

Machine-readable: `data/figure1_human_rows.csv`.

| Compound | Branch | System | Dose and duration | Baseline state | Reported outcome | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Niacin | Acid | Human skeletal muscle, mitochondrial myopathy | 750–1000 mg daily, 10 months (patients) / 4 months (controls) | Depleted | Patient muscle NAD⁺ reached control concentration; blood NAD⁺ up to 8-fold | Pirinen 2020 |
| Nicotinamide riboside | Amide | Human skeletal muscle, men aged 70–80 | 1000 mg daily, 21 days, placebo-controlled crossover | Unstressed | 210 vs 197 pmol mg⁻¹, P = 0.2; muscle NAAD 0.73 vs 0.35 pmol mg⁻¹, P = 0.004 | Elhassan 2019 |
| Nicotinamide riboside | Amide | Human skeletal muscle, overweight and obese adults | 1000 mg daily, 6 weeks, placebo-controlled crossover | Unstressed | No difference in muscle NAD⁺; NAAD and methylnicotinamide elevated | Remie 2020 |

The two blocks are not a clean branch comparison: the niacin subjects were depleted and the riboside subjects were not. The rows are plotted with open and filled markers accordingly, and the confound is the state term of §5 rather than a defect in the comparison. What the riboside rows establish independently of branch is that the compound reached the tissue, and that the intermediate which rose was an acid-branch one.
