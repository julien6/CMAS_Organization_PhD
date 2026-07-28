# Trace Schema Summary

The artifact should document the schema used to build the digital twin and evaluate policies.

## Core Fields

- `timestamp`: wall-clock or experiment-relative time.
- `scenario`: bottleneck, DDoS, pod failure, contention, or mixed.
- `service_id`: Kubernetes deployment or service identifier.
- `replicas_current`: deployed replicas.
- `replicas_desired`: desired replicas after controller decision.
- `failed_pods`: failed or unavailable pods.
- `pending_requests`: queued or pending requests.
- `cpu_usage`: CPU utilization or requested CPU proxy.
- `memory_usage`: memory utilization or requested memory proxy.
- `ingress_traffic`: incoming traffic rate.
- `egress_traffic`: outgoing traffic rate.
- `latency`: measured request latency.
- `availability`: service or endpoint availability indicator.
- `action`: autoscaling action proposed or applied.
- `role`: organizational role associated with the acting agent.
- `reward_global`: operational-resilience reward.
- `reward_mission`: role-specific mission reward.

## Notes

The final package should state the unit, sampling interval, normalization, and missing-value policy for each field.
