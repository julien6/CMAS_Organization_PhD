# A semi-automated approach for MAS organization engineering

## Introduction

Context:
 - The traditional designing of MAS in large and complex deployment environments operates by trial and error and it can be costly while it is not guaranteed to converge to a sufficient solution that fulfils a goal
 - Agents need to be adapted and learn from their environment and to use social scheme or collective strategies to gain efficiency.
 - The organization among agents is the keystone to a MAS designing suited both for fulfilling given goals satisfying environmental and design constraints
 - Difficulty for a direct MAS designing approach on the target system: safety, time and energy costly, empirical, not ensured to converge
   - Variety of environment where MAS are to be deployed and operational and the required knowledge to apprehend them
 - MARL has proved to be successfully applied for various context allowing to generate joint-policies as the set of rules agents are to follow to reach a goal optimally

Problem:
 - MARL allows finding the right policies so agents can fullfil a goal BUT they do not describe the emergent collective phenomena, nor organization is considered during training either.
   - The issue of their organization is not explicitly addressed as the focus is set on the resulting efficiency.
   - We need to make these results understandable not only at individual but also social and collective level.

Contribution
 - A novel MAS design approach starting from the environment, the goals and design constraints to generate "learned" organizational specifications which can be relevant insights to help designing a suited MAS after those.

Results
 - We applied our approach in four spatial Atari games and the Cyberdefense drone swarm environment of the 3rd CAGE Challenge. Each environment have agents that are likely to organize after learning to achieve the best scores.
   - Resulting organizational specifications are indeed consistent with provided design constraints and expected collective strategies.
   - These insights led to build MASs with scores comparable to the leading ones.


## Related works and positioning

 - Works related to individual agents' policy explainability with few links with social or collective interaction...
   - neural networks, bayesian networks...
 - Works related to the extraction of organizational specifications out of collective phenomena emergence through MARL or MAS algorithms on various environments...
   - For MARL: PPO in gfootball, MADDPG in prey-predator...
   - For MAS: Coalition-based MAS, Market-based MAS...

 - Yet, none of these explicitly address the issue of organization as implicit entity to be described in a bottom-up way or to be impacting agents' policies in a top-down way
 - Moreover, there is no systematic available methodological approach to be used both at research and engineering levels that enables benefitting from the observation of emergent collective strategies for MAS designing

## An approach for designing MAS integrating MARL within an organization model

 - We proposed PAMID (Partially Action-based MOISE+ Identification DMO): an algorithm that allows both getting the organizational specifications out of trained agents; and driving their training to satisfy extra design organizational specifications as constraints.
   - [Algo PAMID...]

 - We developped PAMID as a Gym-wrapper to help in applying the proposed MAS design approach...
   - [Lien vers dépôt GitHub]
   - Description des fonctionalités

 - The general approach workflow follows:
   1) Reproducing target environment in simulation
   2) Defining the reward function so agents aim to achieve the goals
   3) Adding agents to be trained to solve the previously defined problem
   4) Launching the training in simulation with PAMID
   5) Getting the raw organizational specifications with PAMID
   6) Curating these to produce a safe MAS model
   7) Using that model to implement a proper MAS
   8) Check viability and requirements respect in simulation
   9) Deploy that MAS in the target system


## Validation and application for malware program in drone swarms

 - We successfully assessed our approach in "Prey-pretador with communication" or "Knights, archers and zombies"
   - Resulting PAMID organizational specification are indeed matching the expected ones
   - Learning in MARL with PAMID is indeed impacted by constraining organizational specifications and allows designer to take hand on the way agents' learn at an organization level

 - We also applied our approach the 3rd CAGE Challenge that consist in creating a suited MAS to protect an ad hoc drone swarm network being cyber-attacked by malware programs for it meets inherent embedded and distributed properties
   - We used the MARL algorithms that give the best score in the end of the challenge
   - Most resulting PAMID organizational specifications outlines some expected collective strategies
   - The curated MAS model and the associated implemented MAS are giving equivalent scores by comparing with finalists' MARL algorithms

## Conclusion

 - Need for easing the MAS design by assisting human designer
 - We proposed a novel general MAS design approach that consists in getting relevant organizational specifications out of agents in training satisfying design constraints. These insights allow implementing a suited safe MAS to be deployed on target system
 - We validated that approach for various different environments including in a Cyberdefense context.
 - Main perspective is to improve the reliability of PAMID between organizational specifications and agents' training satisfying to design constraints.
 - Another future work is to reduce the manual parts of our approach with implementation of a full integrated development environment.