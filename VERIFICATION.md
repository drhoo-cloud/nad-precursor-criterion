# How to check this paper

Everything quoted in the manuscript can be recovered from what is in this
repository, from the published sources it cites, or from PubMed. This note says
where each kind of claim comes from and how to test it.

## The derived numbers

```bash
python3 verify_values.py
```

Every quantity the manuscript derives is printed beside the value printed in the
paper: the gain ceiling, the concentration above which no attainable NAD⁺
restores baseline, the required elasticity and the concentration at which it
crosses unity, the worked example of §5.1, and the figures quoted in §4.4. A
mismatch is visible without opening the paper.

None of these is a measurement. All of them are arithmetic on the five inputs
above the rule in Table 2, which were measured or assumed by others.

## The literature audit

```bash
python3 count_enzyme_mentions.py
```

The search string returns 236 records, and the PubMed Central mapping returns the
same 150 full texts, so the retrieval step can be repeated from the string alone.
The script reports the enzyme-naming counts of Table 1C under two scopes: the
article body, which is the scope quoted in the manuscript, and the whole
deposited record. The asymmetry holds under both.

`audit/` carries the rest: all 236 records with their PMID, PMC identifier and
screen class; the 21 records the screen returned with the adjudication and the
reason for each exclusion; the coding manual; the PRISMA-ScR checklist; and the
per-record mention counts.

## The plotted values

`data/figure1_plotted_values.csv` gives all nineteen points of Figure 1 with
compound, branch, system, exposure, reference and value.
`data/figure2_trial_nodes.csv` gives the node-by-node record of the five trials.
The remaining CSV files are the numerical tables of the supplementary material.

## Where judgement was exercised

Four places, stated here rather than left to be found.

**Two values are read from a figure of their source.** The mouse skin row of
Figure 1 and the methylated-product fold-changes of Figure 2 are not printed as
numbers anywhere in the papers they come from. Both are marked as read from a
figure in the supplementary material, and the mouse row carries the abdominal
control from the same panel so the comparison can be judged.

**One source prints an impossible unit.** Elhassan 2019 gives its blood NAD⁺ and
blood nicotinamide concentrations in mM. They are reported here in µmol L⁻¹, the
only physiologically possible reading. The slip is that source's, not ours.

**One plotted point did not reach significance in its source.** The nicotinic
acid mononucleotide entry of Figure 1 is marked ns. Every other entry is
significant as reported.

**One state is assumed rather than measured.** The depleted nuclear
concentration, a fourfold fall, is an assumption; §5.3 states the single
measurement that would confirm or overturn it, and `data/table_S1_sensitivity.csv`
sweeps the derived quantities across the contested inputs. The direction of every
one of them is invariant across those ranges.

## What this repository does not contain

The manuscript and supplementary text, which are subject to the publisher's
terms; the full text of any cited paper; and any generating script for Figure 2,
which is a hand-drawn pathway schematic. Its source values are in
`data/figure2_trial_nodes.csv`.
