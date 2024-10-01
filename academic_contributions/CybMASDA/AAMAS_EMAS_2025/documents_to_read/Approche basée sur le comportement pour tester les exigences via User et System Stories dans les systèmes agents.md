# Approche basée sur le comportement pour tester les exigences via User et System Stories dans les systèmes agents

## 1. Introduction
- **Test et validation** : Cruciaux pour les systèmes logiciels, particulièrement pour les systèmes autonomes.
- **Objectif de l'article** : Proposer une approche basée sur le développement dirigé par le comportement (BDD) pour tester les exigences comportementales d'un système agent.
- Utilisation des **User Stories (USS)** et des **System Stories** pour capturer et tester les exigences du système.

## 2. Contexte et travaux connexes
### 2.1 User and System Stories (USS)
- **User Stories** : Descriptions informelles des exigences du point de vue de l'utilisateur, exprimées sous forme narrative.
- **System Stories** : Extensions des User Stories pour représenter les exigences du point de vue du système.
- Les deux types de stories sont utilisés pour capturer les comportements attendus du système et guider le développement.

### 2.2 Behaviour Driven Development (BDD)
- **BDD** : Pratique de développement agile qui favorise la collaboration entre les développeurs techniques et les experts du domaine.
- Processus en trois étapes : spécification des histoires, création des critères d'acceptation, et développement guidé par les tests.
- Utilisation d'outils comme **Cucumber** pour spécifier les tests dans un format compatible avec les stories.

### 2.3 Objectifs et plans dans les systèmes agents
- **Objectifs (Goals)** : Conditions à atteindre ou à maintenir par un agent. Ils sont persistants jusqu'à ce qu'ils soient atteints ou jugés impossibles.
- **Plans** : Séquences d'actions que l'agent exécute pour atteindre un objectif.
- **Percepts et Beliefs** : Les perceptions fournissent des informations à l'agent, qui génère des croyances sur l'état du monde.

## 3. Extension des USS pour le BDD
- Proposition d'une classification des **System Stories** pour capturer les informations requises pour les tests.
- **Goal Stories** : Décrivent un objectif que l'agent doit atteindre ou maintenir.
- **Plan Stories** : Décrivent les plans utilisés pour atteindre un objectif ou maintenir une condition.
- **Belief Inference Stories** : Capturent les relations entre les croyances d'un agent.
- **Perception Stories** : Capturent la manière dont un agent réagit à une perception.

## 4. Cadre de test
### 4.1 Aperçu et outils
- Utilisation d'outils modernes comme **Cucumber** et **JUnit** pour traduire les histoires en tests exécutables.
- Intégration avec le langage de programmation **SARL** pour implémenter les agents.
- Utilisation de **Mockito** pour isoler les composants et vérifier les interactions.

### 4.2 Implémentation des tests
- Les critères d'acceptation des histoires sont traduits en tests exécutables avec des annotations (Given, When, Then).
- Exemple d'implémentation des étapes de tests en SARL avec Cucumber.

### 4.3 Exécution des tests
- Génération de rapports de test pour évaluer le respect des critères d'acceptation.
- Illustration des résultats de tests avec des scénarios réussis et échoués.

### 4.4 Mutation Testing
- Utilisation de **PITest** pour tester la qualité de la suite de tests.
- **Mutation Testing** : Introduit des fautes mineures dans le code pour vérifier si les tests les détectent.
- **Résultats** : Mesure de la couverture de ligne, de la couverture de mutation, et de la force des tests.
- Exemple d'amélioration des scénarios de test basés sur les mutants non détectés.

## 5. Conclusion
- Approche basée sur les **User et System Stories** pour capturer les exigences comportementales dans un système d'agents.
- Utilisation d'outils standards de l'industrie pour assurer la qualité et la facilité d'adoption.
- **Travaux futurs** : Support pour d'autres langages orientés agents et schémas de mutation spécifiques à SARL.
