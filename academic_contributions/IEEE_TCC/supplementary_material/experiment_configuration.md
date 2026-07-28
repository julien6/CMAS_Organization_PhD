# Experiment Configuration Summary

## Environment

- Kubernetes Chained Services topology with four services.
- One worker node for prototype evaluation.
- Autoscaling decision interval: 30 seconds.
- Prometheus scrape interval: 5 seconds.
- Ten independent seeds for learning-based results.

## Scenarios

- Bottleneck resolution.
- DDoS-like overload.
- Pod failures.
- Resource contention.
- Mixed concurrent disturbance scenario.

## Baselines And Ablations

- KHPA.
- Gym-HPA.
- Rlad-core.
- AWARE.
- Single-agent RL.
- Multi-agent without organization.
- Roles only.
- Missions only.
- Soft organization.
- Hard organization.
- Full KARMA.

## Metrics

- Success rate.
- Latency compliance.
- Pending requests.
- Recovery time.
- Service availability.
- Reward variance.
- Sim-to-real gap.
- Behavioral separability.
- Computational cost.
