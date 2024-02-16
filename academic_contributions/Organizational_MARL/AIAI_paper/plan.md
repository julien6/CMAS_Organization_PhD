# A Design Approach for Cyberdefense Multi-Agent System with Reinforcement Learning

## Introduction

Context:
 - AICA agents introduce the general concept of a Cybedefense Multi-Agent System (CMAS)
 - ...

Problem:
 - The human-based design process is costly and not necessarily converging to fulfilling a goal
 - MARL allows finding the right policies so agents can fullfil a goal BUT they do not describe the emergent collective phenomena, nor organization is considered during training either.

Proposition
 - A general algorithm that aims at integrating an organizational model within a MARL model both to drive the agents' training according to organizational constraints and to have an organizational representation of agents' behaviors
 - A design approach for designing a CMAS starting from the network environment and the red team, producing "learned" organizational specifications to help designing better CMAS after.

## The organizational issue in CMAS designing

 - A CMAS is a MAS ensuring the Cyberdefense on the networked environment where it is deployed on
   - Cyber-defenders agents are to collaborate to fullfil a common goal. They are thought suited for heterogenous, distributed systems whereas centralized Cyberdefense systems are inefficient
   - Agents need to be adapted and learn from their environment and to use social scheme or collective strategies to gain efficiency.

 - The organization among agents is the keystone to a CMAS designing suited both for fullfiling given goals satisfying environmental and design constraints

 - Difficulty for a direct CMAS designing approach on the target system: safety, time and energy costly, empirical, not ensured to converge
   - Categories of environment where CMAS/AICA are to be deployed and operational: drone swarm, company network, IoT system...
   - Raising the diversity of applicative context, the need for a thorough knowledge of each system if we want to design a CMAS
   - There is no systematic available methodological approach to be used both at research and engineering levels

 - Recent advances the closest to CMAS designing have been pushed forward MARL as an automated way to find the agents' policies that better fullfil the given Cyberdefense goals.
   - Yet, the issue of their organization is not explicitly addressed as the focus is set on the resulting efficiency.

We need to make these results understandable not only at individual but also social and collective level.

## Related works and positioning

 - Works related to individual agents' policy explainability with few links with social or collective interaction...
   - neural networks, bayesian networks...
 - Works related to collective phenomena emergence through MARL algorithms on various environments...
   - PPO in gfootball, MADDPG in prey-predator...

 - Yet, none of these explicitly address the issue of organization as implicit entity to be described in a bottom-up way or to be impacting agents' policies in a top-down way

## An approach for addressing organization within MARL in MAS

 - Organizational oriented MARL: a general research study focusing in integrating the organization in MARL at several aspects
 - DMO (Dec-POMDP MOISE+ OMARL): a class of algorithm falling into OMARL purposes that use MOISE+ as organizational model and Dec-POMDP as a MARL model
 - PAMID (Partially Action-based MOISE+ Identification DMO): a DMO algorithm that allows both getting the organizational specifications out of trained agents; and driving their training to satisfy extra design organizational specifications as constraints.

## An approach for designing CMAS with PAMID

 - The general approach workflow follows:
   1) Reproducing target environment in simulation
   2) Adding red agents possibly with scripted attacking policies
   3) Adding blue agents to be trained
   4) Launching the training in simulation
   5) Getting the raw organizational specifications
   6) Curating these to produce a safe CMAS MOISE+ model
   7) Using that model to implement a proper CMAS

 - We developped PAMID as a Gym-wrapper to help in applying the proposed CMAS design approach...

## Validation and application for malware program in drone swarms

 - We successfully assessed our approach in non Cyberdefense related environment such as "Prey-pretador with communication" or "Knights, archers and zombies"
   - Resulting PAMID organizational specification are indeed matching the expected ones
   - Learning in MARL with PAMID is indeed impacted by constraining organizational specifications and allows designer to take hand on the way agents' learn at an organization level

 - We applied our approach the 3rd CAGE Challenge that consist in creating a suited CMAS to protect an ad hoc drone swarm network being cyber-attacked by malware programs for it meets inherent embedded and distributed properties
   - We used the MARL algorithms that give the best score in the end of the challenge
   - Most resulting PAMID organizational specifications outlines some expected collective strategies
   - The curated MAS model and the associated implemented MAS are giving equivalent scores by comparing with finalists' MARL algorithms

## Conclusion

 - Need for easing the CMAS design by assisting human designer
 - We proposed a novel general approach for addressing organization within MARL in MAS
 - Using it, we proposed an approach for designing CMAS with PAMID
 - We validated that approach in independent environment and also proved it to be efficient in a Cyberdefense context