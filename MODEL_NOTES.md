# Model notes: contested parameters, objections, and routes that require no rise

Supporting record for §5.1 and §6.2 of the article, and for Appendix A.4. Reference numbers are omitted here deliberately; sources are named so that this file stays correct whatever the article's final numbering. The parameter sweeps are at `data/table_S2_KS_alternative.csv`, `data/table_S3_thresholds_by_M.csv`, `data/table_S5_eta_req_by_M.csv` and `data/table_S7_output_ratio.csv`; the in-article summary is Table B.2.

---

## 1. The constant: two values for the same quantity

This is the third of the three points raised against the objection answered in §5.1. It is set out here because **the choice it describes runs against our own conclusion.**

Two values circulate for the Michaelis constant of SIRT1 for NAD⁺.

The objection uses **90 µmol L⁻¹**, a figure gathered from the literature without the conditions under which it was measured, and the estimates behind it span more than tenfold.

We use **29 ± 3 µmol L⁻¹**, measured in a single study that states its conditions: 0.2 µmol L⁻¹ enzyme, 20 mmol L⁻¹ sodium phosphate at pH 7.5, 37 °C, reversed-phase chromatographic quantification, n ≥ 3 with the standard deviation of the mean (Table 2; Table B.1).

### The choice goes against us

A larger K_S places the enzyme further from saturation and leaves more room to gain.

| K_S (µmol L⁻¹) | Source | η_req unstressed | η_req depleted | G_max unstressed | G_max depleted |
| --- | --- | --- | --- | --- | --- |
| 29 | Measured, acetyl-H3K9 (**adopted**) | 0.65 | 0.27 | 1.29 | 2.16 |
| 50 | intermediate | 0.44 | 0.22 | 1.50 | 3.00 |
| 90 | review value, conditions unstated | 0.31 | 0.19 | 1.90 | 4.60 |

M₀ = 30 µmol L⁻¹ and K_i = 175 µmol L⁻¹ throughout; all entries are derived, not measured.

At 90 the unstressed ceiling would be 1.90 rather than 1.29, and the required elasticity at the resting concentration 0.31 rather than 0.65. **Both changes make the amide branch easier to defend, not harder.** We take the smaller value and the narrower ceiling because it is the one measured under stated conditions, and we record here that the choice favours our conclusion rather than our case.

Every derived quantity changes across the sweep; the direction of none of them does. **That direction, and not the value 0.27, is what §6.4 claims.**

## 2. Where the other two sweeps do and do not run one way

The sweeps over nuclear free NAD⁺ (N₀) and over the sirtuin Michaelis constant (K_S) are one-directional: deeper depletion and a larger K_S both widen the ceiling and lower the threshold, and neither reverses the conclusion.

**The sweep over resting nicotinamide (M₀) does not run one way.** Below about 15 µmol L⁻¹ the largest measured elasticity (0.34) clears the threshold in both states rather than in the depleted state alone. The adopted value is 30 µmol L⁻¹, from murine tissue.

| M₀ (µmol L⁻¹) | η_req unstressed | η_req depleted | M\* unstressed | M\* depleted | Largest measured η (0.34) clears |
| --- | --- | --- | --- | --- | --- |
| 10 | 0.24 | 0.10 | 64 | 225 | both states |
| 15 | 0.35 | 0.15 | 70 | 235 | depleted only |
| 30 (**adopted**) | 0.65 | 0.27 | 89 | 268 | depleted only |
| 39 | 0.81 | 0.34 | 101 | 287 | depleted only, at the boundary |
| 100 | 1.62 | 0.68 | 180 | 419 | neither state |

This is the reason the article's Limitations state the invariance claim at **the concentrations in use** rather than at the resting concentration. At M₀ the direction is not invariant; at the concentrations at which nicotinamide is actually applied it is, and by a wide margin.

## 3. Two further objections to the compartment argument

> **Drafted for this deposit and not yet carried through author verification.** The article's §5.1 refers two objections to this record. The ARR version of the manuscript referred the same two objections to its Appendix S5, which in fact contains only §1 above; the answer was never written out. What follows is the argument the article's own framework supplies. It should be checked by the authors against the primary sources before the deposit is published, or the referring sentence removed from §5.1.

**That a biosensor reports free rather than bound NAD⁺.** This is true and is the reason the biosensor value is the one used. Michaelis–Menten kinetics are written in the free concentration of the substrate, so the quantity equation 1 requires is free nuclear NAD⁺ and not the total. The objection would bear on the argument only if the bound fraction were available to the enzyme, in which case the effective N₀ would be *higher* than 100 µmol L⁻¹ — which lowers the ceiling G_max and makes the amide branch harder to defend, not easier.

**That the nuclear envelope equilibrates the nuclear and cytosolic pools.** Granting this does not restore the objector's figure. The biosensor reports each compartment separately and places the nuclear and cytosolic free concentrations near the Michaelis constants of the enzymes resident in each; equilibration between two compartments that both sit near 100 µmol L⁻¹ leaves N₀ near 100 µmol L⁻¹. It is the whole-cell measurement of 400–700 µmol L⁻¹, which sums free and bound across every compartment including the mitochondrion, that the objection would have to recover, and pore-mediated exchange of the free pool does not recover it.

Neither objection moves the ceiling in the direction that would rescue the amide branch. The sweep of §1 above shows what would: a larger K_S. We adopt the smaller.

## 4. A third route that requires no rise: methylation

Skin expresses nicotinamide N-methyltransferase, and two of nicotinamide's effects in irradiated keratinocytes were not reversed by NAMPT inhibition; those authors attributed them to the methylation product acting through NRF2.

Like PARP-1 inhibition, **this route consumes nicotinamide rather than raising NAD⁺**, so equation 1 is unaffected by whether it operates.

The three accounts listed in §6.2 are therefore alternatives to repletion, not to one another.
