# Artifact Manifest

## Required Items

- Source code for KARMA and baseline wrappers.
- Kubernetes manifests for the Chained Services topology.
- Prometheus scraping configuration and metric extraction scripts.
- Workload-generation scripts, including Locust configuration.
- Disturbance-injection scripts for bottleneck, DDoS-like overload, pod failures, contention, and mixed scenarios.
- Digital-twin training scripts and saved configuration files.
- MAPPO training scripts and role/mission configuration files.
- Evaluation scripts for RQ1-RQ6.
- Plotting scripts for learning curves and trajectory clustering.
- Per-run logs for the ten independent seeds used in the manuscript.
- Final aggregated CSV or JSON files used for all reported tables.

## Pre-Submission Checks

- Archive or tag the exact code version used by the manuscript.
- Add checksums for large trace/log files.
- Confirm that no confidential infrastructure information is included.
- Confirm that all referenced secondary figures are present or reproducible.
