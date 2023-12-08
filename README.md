# About Cyberdefense Multi-Agent System Organization (Autonomous Intelligent Cyberdefense Agent - AICA)

## Topic description

**Context**:
- Need to ensure Cyberdefense in distributed, heterogeneous networked systems: IoT (drones swarm, domotic) or classical infrastructures while centralized solution show to be inefficient.
- Carried out architectural works for an AICA agent that is to be deployed on networked systems to ensure Cyberdefense.
- Current AICA architecture should be revised to take advantage of a multi-agent approach in order to address issues related to decentralization, distribution, scalability, adaptability...

**Problem**:

> **What are the organizations among cyber-defender agents so the resulting CMAS can be deployed and operate under the networked environment constraints in order to reach its cyber-goal in the most efficient way?**

_Considering an AICA agent is a particular case of a Cybedefense Multi-Agent System (CMAS) that is made up from a set of cyber-defender agents collaborating together to reach their cyber-goal._



**Related works in literature**:
- Very few works dealing with the concept of a CMAS (except AICA works)
- No works dealing with organization and related issues of a CMAS...

**Expected contributions**
- **Academic**: Organizational mechanisms of a CMAS taking into account the deployment and operational constraints in environment and the cyber-goal to reach.
- **Industrial**: A method and a tool to develop CMAS for given networked environment and cyber-goals in order to help in various case studies.

**Litterature approach to address the problem**
- For each work dealing with a CMAS, we tried to establish trends between the core CMAS organization, networked environment and cyber-goal
    - Results not meaningful: not enough works, too specific, not consistent, subjective analyze...

**General academic contribution roadmap**
1) Established a study framework consisting in a networked environment with blue, red, and green teams
2) Established a formalization of the study framework with related Cyberdefense and MAS concepts through a Dec-POMDP model
3) Established a methodological approach to design, implement, and assess several types of blue team organizations to know what organization to foster for given networked environment and cyber-goal
4) Developped a methodological tool to support the approach relying on simulation and emulation
5) Use the method with the help of the tool in academic case studies

**General industrial contribution roadmap**
1) Adapt the methodological approach to help in designing organization in light of drawn trends between organization, networked environment and cyber-goals
2) Adapt the methodological tool into an industrial tool providing practical means for designing, implementing, assessing and deploying a CMAS, by relying on the adapted methodological approach
5) Use the method with the help of the tool in industrial case studies

----

## Works in progress

- CybMASFM: Cyberdefense Multi-Agent System Formal Model
    - An extended dec-POMDP formalism as a general basis for any scenario falling into the study framework
    - Mean for building models of scenarios to be quantitatively assessed with various resolution approaches in simulation and emulation
    - Integration of existing works in Cyberdefense frameworks simulation/emulation, collective AI, MAS concepts, etc. through the Dec-POMDP formalism
    - Special focus on MAS organization by integrating and positioning related concepts (re/self-organization, emergence, Agent Centered Point of View / Organization Centered Point of View, etc.)

- CybMASDA: Cyberdefense Multi-Agent System Development Approach
    - Instrumentation of the CybMASFM towards a method for both academic and industrial needs
    - General iterative approach to design, implement, assess, analyze CMAS relying on a simulation/emulation coupling
    - A lifecycle taking a networked environment description and cyber-goals as parameters and expecting some operational CMASs and the learnt trends which indicate what organization to foster according to the networked environment and cyber-goals
    - Theoritical means to help in designing, assessing, analyzing CMAS providing steps, guidelines, metrics, analysis, forms, tools, algorithms, etc.

- CybMASDE: Cyberdefense Multi-Agent System Development Environment
    - Support of CybMASDA using suited simulator and emulator
    - A practical mean to help researcher (and engineer) to apply CybMASDA automating the whole process and easing manual configuration by providing existing elements and restricting to high-level choice of configuration