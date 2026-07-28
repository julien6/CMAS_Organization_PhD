# Hyperparameters And Optuna Summary

The manuscript reports the main hyperparameters in the reproducibility table. The full artifact should include the Optuna study export and the selected final configuration.

## Reported Defaults

- MAPPO budget: up to 2200 episodes.
- Learning rate: `3e-4`.
- Clipping range: `0.2`.
- Entropy coefficient: `0.01`.
- Advantage-estimation lambda: `0.95`.
- Discount factor: `0.99`.
- Actor and critic networks: two hidden layers of 128 units.
- Digital twin: neural transition model with three hidden layers of 128 units.
- Digital-twin optimizer: Adam with learning rate `1e-3`.
- Optuna budget: 50 trials.

## To Include Before Submission

- Final selected trial identifiers.
- Search ranges for all optimized parameters.
- Seed list.
- Early stopping thresholds.
- Scenario-specific convergence thresholds.
- Runtime environment and package versions.
