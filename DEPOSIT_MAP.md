# Where to find each item the article calls "the deposited record"

The manuscript refers to this archive eighteen times. This file maps each reference to the item that answers it, so a reader or reviewer does not have to search.

| Article location | What it asks for | File in this archive |
|---|---|---|
| §1, audit result | search strings, coding manual, per-record codes, limitations of the audit | `audit/coding_manual.csv`, `audit/retrieval_record.csv`, `audit/records_stating_inhibition_search1.csv`, `audit/records_stating_inhibition_search2.csv`, `audit/screen_adjudication.csv`, `AUDIT_NOTES.md` |
| §1, audit reporting standard | completed PRISMA-ScR checklist and flow diagram | `audit/prisma_scr_checklist.csv`, `audit/prisma_flow.csv`, `figures/Figure_PRISMA_flow.eps` |
| §2.4, enzyme-naming asymmetry | term counts behind the 5.8 : 1 ratio | `audit/enzyme_mention_counts.csv`, produced by `count_enzyme_mentions.py` |
| §3.3, five human trials | how the five were identified and how each node was coded | `data/figure2_trial_nodes.csv`, `TRIAL_EXTRACTION.md` |
| §3.3 / Figure 2 | treated and placebo values, fold-changes and P values | `data/figure2_trial_nodes.csv`; the same values on a single logarithmic scale, `figures/Figure_trial_nodes_log.eps` |
| §4.1 / Figure 1 | doses, durations, baseline state and reported outcome for every plotted row | `data/figure1_human_rows.csv`, `data/figure1_plotted_values.csv` |
| §4.1, the 1.31-fold value | why the true figure may be smaller still | `AUDIT_NOTES.md`, section "The one amide-branch marker that clears the line" |
| §5.1, two further objections | free against bound NAD⁺; nuclear–cytosolic equilibration | `MODEL_NOTES.md` |
| §5.1 / Appendix A.4, the competing K_S | the two circulating values and the measurement conditions of each | `MODEL_NOTES.md`; swept in `data/table_S2_KS_alternative.csv` |
| §6.1, branch assignment | the supporting record for the naming and route rules | `data/table_S9_compound_branch.csv`, `data/table_S10_route_by_compound.csv` |
| §6.2, the methylation account | NRF2 and N-methylnicotinamide | `MODEL_NOTES.md` |
| Figures 3 and 4 | the plotted values and their derivations | `data/table_S3_thresholds_by_M.csv`, `data/table_S5_eta_req_by_M.csv`, `data/table_S7_output_ratio.csv` |
| AI declaration | tool, version, sections involved and prompts | `AI_USE.md` |

## What is **not** here, because it is in the article

| Item | Where it is |
|---|---|
| Derivation of equations 1 and 2 and of M\*; the IC₅₀ = K_i substitution; what the model omits | **Appendix A** |
| Enzyme identity and assay conditions to the STRENDA standard | **Table B.1** |
| Sensitivity of every derived quantity to the three contested inputs | **Table B.2** |
| Branch by compound and by route | **Table C.1** |
| Audit result | **Table 1** |
| Parameters and derived quantities | **Table 2** |
| The four decisive measurements | **Table 3** |
