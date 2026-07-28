# KARMA TCC Supplementary Material

This supplementary package accompanies the IEEE Transactions on Cloud Computing submission:

**KARMA: An Automated Multi-Agent Framework for Resilient Kubernetes Autoscaling**

The main manuscript states that several implementation and reproduction details are kept outside the paper to preserve the 12-page TCC limit. This package is intended to be submitted separately from the main manuscript PDF.

## Contents Expected For Reproduction

The supplementary material should include or point to:

- trace schemas for Kubernetes, Prometheus, workload, disturbance, and autoscaling-action records;
- full configuration files for the Chained Services topology, scenario definitions, baseline settings, replica bounds, and decision intervals;
- selected hyperparameter trials and final MAPPO/Optuna settings;
- per-run logs or a stable location where the per-run logs can be retrieved;
- scripts to reproduce preprocessing, training, evaluation, plotting, and metric aggregation;
- secondary behavioral-analysis figures not included in the main paper;
- final run metadata used to generate the reported tables.

## Artifact Reference

The manuscript currently points to the KARMA source code and artifact location:

<https://github.com/julien6/KARMA>

Before submission, verify that this repository or an archived artifact contains the exact commit, scripts, traces, and logs corresponding to the TCC manuscript.

## Files In This Package

- `README.md`: this overview.
- `artifact_manifest.md`: checklist of required artifact items.
- `trace_schema.md`: compact trace-schema description.
- `experiment_configuration.md`: reproduction and configuration summary.
- `hyperparameters.md`: hyperparameter and Optuna summary.
- `submission_checklist.md`: final ScholarOne upload checklist.

If raw traces or logs are too large for ScholarOne, include a persistent archival link and checksum list in this package before submission.
