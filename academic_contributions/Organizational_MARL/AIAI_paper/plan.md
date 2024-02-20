# A semi-automated approach for MAS organization engineering

=====> mes remarques sont à chaud : ne suit pas à la lettre ce que je dis, retient l'idée générale... si tu es d'accord évidement 
## Introduction

Context:
 - The traditional designing of MAS in large and complex deployment environments operates by trial and error and it can be costly while it is not guaranteed to converge to a sufficient solution that fulfils a goal
 - Agents need to be adapted and learn from their environment and to use social scheme or collective strategies to gain efficiency.
 - The organization among agents is the keystone to a MAS designing suited both for fulfilling given goals satisfying environmental and design constraints
 - Difficulty for a direct MAS designing approach on the target system: safety, time and energy costly, empirical, not ensured to converge
   - Variety of environment where MAS are to be deployed and operational and the required knowledge to apprehend them
 - MARL has proved to be successfully applied for various context allowing to generate joint-policies as the set of rules agents are to follow to reach a goal optimally

=====> CONTEXTE : traditional est le genre de mot qui n'apporte rien. 
Le MARL ne me parait pas a sa place dans le contexte. 
je dirai un phrase pour motiver l'interet des SMA (c'est pas les JF AAMAS...). 
La place de l'organisation dans leur conception et ses enjeux. 
Les difficultés de la conception de cette organisation.

Problem:
 - MARL allows finding the right policies so agents can fullfil a goal BUT they do not describe the emergent collective phenomena, nor organization is considered during training either.
   - The issue of their organization is not explicitly addressed as the focus is set on the resulting efficiency.
   - We need to make these results understandable not only at individual but also social and collective level.
====> PROBLEME je ne placerai pas le MARL a ce niveau là car c'est une partie de la solution. Je parlerai ici du problème auquel tu réponds avec la démarche et les outils (MARL) que tu proposes.

Contribution
 - A novel MAS design approach starting from the environment, the goals and design constraints to generate "learned" organizational specifications which can be relevant insights to help designing a suited MAS after those.
====> CONTRIBUTION est la réponse au problème décrit précédement... ici  tu peux effectivement parler apprentissage

Results
 - We applied our approach in four spatial Atari games and the Cyberdefense drone swarm environment of the 3rd CAGE Challenge. Each environment have agents that are likely to organize after learning to achieve the best scores.
   - Resulting organizational specifications are indeed consistent with provided design constraints and expected collective strategies.
   - These insights led to build MASs with scores comparable to the leading ones.
====> RESULTS : je mettrai dans contribution et en disant en une ou deux phrase qu'on a évaluer l'approche sur un cas de cyberdefense... si deux applications il faut parler de leur complémentarité (qu'on évalue pas les memes choses).

## Related works and positioning

 - Works related to individual agents' policy explainability with few links with social or collective interaction...
   - neural networks, bayesian networks...
 - Works related to the extraction of organizational specifications out of collective phenomena emergence through MARL or MAS algorithms on various environments...
   - For MARL: PPO in gfootball, MADDPG in prey-predator...
   - For MAS: Coalition-based MAS, Market-based MAS...

 - Yet, none of these explicitly address the issue of organization as implicit entity to be described in a bottom-up way or to be impacting agents' policies in a top-down way
 - Moreover, there is no systematic available methodological approach to be used both at research and engineering levels that enables benefitting from the observation of emergent collective strategies for MAS designing
 
 =====> On ne devrait pas parle d'explicabilité ici. Les travaux liés à ton probleme c'est les basics de l'organization, comment sont construites les actuellement les organisations, et des preconisations (la tu peux parler de tes outils MARL... 

## An approach for designing MAS integrating MARL within an organization model

====> le titre devrait plutot etre le nom de ton approche... Le titre me plait pas du tout car ton objectif c'est pas d'integrer le MARL dans l'organisation... c'est juste ce qui te parait etre le meilleur moyen pour proposer une approche pour xxxxxxxxxxxxxxxxxx. C'est le xxxxxxxxxxxxxxxxxx qui est important.


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

=====> tu précices que ce que tu veux valider, le protocole expérimental que tu mets enn oeuvre pour ça et les résultats.
 - We successfully assessed our approach in "Prey-pretador with communication" or "Knights, archers and zombies"
   - Resulting PAMID organizational specification are indeed matching the expected ones
   - Learning in MARL with PAMID is indeed impacted by constraining organizational specifications and allows designer to take hand on the way agents' learn at an organization level

 - We also applied our approach the 3rd CAGE Challenge that consist in creating a suited MAS to protect an ad hoc drone swarm network being cyber-attacked by malware programs for it meets inherent embedded and distributed properties
   - We used the MARL algorithms that give the best score in the end of the challenge
   - Most resulting PAMID organizational specifications outlines some expected collective strategies
   - The curated MAS model and the associated implemented MAS are giving equivalent scores by comparing with finalists' MARL algorithms

## Conclusion

=======> demande toi avant de rédiger la conclusion "Qu'est ce qui change dans l'état de l'art avec ce papier ?"... si tu avais lu ce papier et qu'il n'était pas de toi qu'est ce que tu te serai dis 

 - Need for easing the MAS design by assisting human designer
 - We proposed a novel general MAS design approach that consists in getting relevant organizational specifications out of agents in training satisfying design constraints. These insights allow implementing a suited safe MAS to be deployed on target system
 - We validated that approach for various different environments including in a Cyberdefense context.
 - Main perspective is to improve the reliability of PAMID between organizational specifications and agents' training satisfying to design constraints.
 - Another future work is to reduce the manual parts of our approach with implementation of a full integrated development environment.