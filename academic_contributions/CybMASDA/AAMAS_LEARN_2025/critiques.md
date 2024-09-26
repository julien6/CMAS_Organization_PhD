## Résumé
L'idée principale consiste à guider le processus d'apprentissage multi-agent (MARL) en imposant des contraintes qui limitent l'ensemble des actions autorisées pour chaque agent. Ces contraintes sont définies par des paires (observation, historique) et peuvent être utilisées pour structurer l'organisation du système multi-agent (SMA), restreindre l'espace de recherche des politiques des agents et garantir le respect de certaines normes ou exigences (comme la sûreté de fonctionnement ou des exigences de sécurité).

**Objectifs de la contribution :**

- **Guidage de l'apprentissage :** Réduire l'espace de recherche des politiques des agents en imposant des contraintes, ce qui peut améliorer l'efficacité de l'apprentissage.
- **Sûreté et conformité :** Assurer que les politiques apprises respectent des contraintes de sûreté et de sécurité.
- **Explicabilité :** Offrir une structure plus compréhensible pour les humains en utilisant des contraintes qui reflètent des comportements ou des structures organisationnelles préexistantes.
- **Conception facilitée :** Permettre la conception d'un SMA où les détails exacts des politiques ne sont pas spécifiés en avance, mais où une forme abstraite des comportements attendus est déjà connue.

**Points de Clarification et Questions**

**Validité Théorique :**

- Comment formuler précisément les contraintes ? Quelle est la structure exacte des paires (observation, historique) et des ensembles d'actions autorisées ? Est-il nécessaire de définir formellement des relations d'ordre sur les actions ou les observations ?
- Comment s’assurer que les contraintes sont compatibles avec les capacités d’apprentissage des algorithmes MARL ? Par exemple, certaines contraintes pourraient-elles rendre l'espace d'apprentissage non convexe ou irréaliste à explorer pour les algorithmes courants ?

**État de l’Art et Originalité :**

- En quoi cette approche se distingue-t-elle des méthodes de Constrained Reinforcement Learning ou des approches de Safe Exploration déjà existantes ? Quelles sont les contributions exactes qui n'ont pas encore été explorées ?
- Existe-t-il des travaux similaires utilisant MOISE+ ou d’autres cadres organisationnels comme AGR pour imposer des contraintes pendant l’apprentissage ? Si oui, en quoi cette approche se différencie-t-elle ?

**Apport Mesurable :**

- Quels seraient les indicateurs ou métriques permettant de démontrer les bénéfices de cette approche ? Par exemple, quelles mesures montreraient une amélioration en termes de performance d'apprentissage, de respect des contraintes, ou de qualité de l'organisation par rapport à des méthodes sans contraintes ?
- Quels sont les scénarios expérimentaux envisagés pour valider cette approche ? Sont-ils suffisamment génériques pour montrer que la contribution est applicable à différents types de SMA ?

**Implémentation Pratique :**

- Comment intégrer ces contraintes dans un environnement d'apprentissage MARL existant ? Est-ce par le biais d’une approche de reward shaping, de policy shaping (modification des politiques en temps réel), ou par une autre méthode comme le Shielding ?
- Comment gérer les conflits potentiels entre différentes contraintes ? Par exemple, si deux contraintes dictent des actions incompatibles dans une même situation, quelle stratégie est utilisée pour résoudre ce conflit ?

**Objectifs Spécifiques :**

- Quel est le niveau de granularité des contraintes ? Sont-elles appliquées de manière fine (par agent individuel) ou à un niveau plus global (coordination d’équipe) ?
- Cette approche est-elle conçue pour être générale (applicable à tout type de SMA) ou pour des cas spécifiques (comme la défense cybernétique) ? Comment cela affecte-t-il la définition des contraintes ?

**Perspectives et Extensions :**

- Comment cette méthode pourrait-elle être étendue à des SMA qui nécessitent des adaptations dynamiques des contraintes (par exemple, en fonction de changements dans l'environnement ou des objectifs) ?
- Comment cette approche pourrait-elle être combinée avec d'autres mécanismes d’apprentissage ou d’optimisation (par exemple, apprentissage par imitation ou apprentissage hiérarchique) pour améliorer la performance ou la robustesse des agents ?

-----
-----

### **Critiques du fond :**

#### 1. Comparaison avec d'autres modèles d'organisation :
   - **Critique :** Le choix de MOISE+ n'est pas suffisamment justifié par rapport à d'autres modèles d'organisation comme AGR. Il manque une comparaison détaillée avec ces modèles en termes d'apprentissage par renforcement.
   - **Suggestion :** Ajouter une section détaillée dans "Related Works" qui compare MOISE+ avec AGR et d'autres modèles organisationnels. Expliquer les avantages spécifiques de MOISE+ pour l'apprentissage par renforcement, comme la flexibilité de la réorganisation dynamique et le support des normes et missions.

#### 2. Comparaison avec d'autres techniques d'optimisation :
   - **Critique :** Le papier ne justifie pas pourquoi l'apprentissage par renforcement (RL) est préféré par rapport à d'autres techniques comme le contrôle prédictif (MPC), les algorithmes génétiques, ou le contrôle optimal stochastique.
   - **Suggestion :** Inclure une discussion sur les autres techniques d'optimisation, expliquant pourquoi RL a été choisi. Par exemple, mentionner la capacité de RL à gérer des environnements dynamiques et incertains, ce qui peut être difficile pour les techniques basées sur les modèles comme MPC.

#### 3. Manque de comparaison avec des algorithmes MARL existants :
   - **Critique :** Les performances de PRAHOMT ne sont pas comparées à d'autres algorithmes MARL utilisant des informations organisationnelles.
   - **Suggestion :** Inclure des comparaisons expérimentales avec d'autres algorithmes MARL qui utilisent des spécifications organisationnelles, en mettant en évidence les gains en termes de convergence, sécurité et stabilité.

#### 4. Explication insuffisante de PRAHOM vs PRAHOMT :
   - **Critique :** La différence entre PRAHOM et PRAHOMT n'est pas clairement expliquée. Il manque une description des concepts repris de PRAHOM et de ce qui est nouveau dans PRAHOMT.
   - **Suggestion :** Ajouter une sous-section dédiée dans "Methodology" expliquant les différences entre PRAHOM et PRAHOMT, en précisant les nouvelles contributions comme l'intégration explicite des missions et rôles dans les contraintes de politique.

#### 5. Explications floues sur l'intégration des organisations dans MARL :
   - **Critique :** Il n'est pas clair pourquoi l'ajout de structures organisationnelles est important et comment cela améliore l'apprentissage.
   - **Suggestion :** Revoir l'introduction pour clarifier les bénéfices de l'intégration des structures organisationnelles. Ajouter des exemples concrets montrant comment cela peut accélérer la convergence ou améliorer la coordination.

#### 6. Scénarios expérimentaux simples :
   - **Critique :** Les scénarios expérimentaux, comme le prédateur-proie, sont jugés trop simples pour démontrer l'efficacité de l'approche dans des environnements complexes.
   - **Suggestion :** Étendre les expériences à des scénarios plus complexes impliquant des interactions dynamiques entre les agents, des changements de rôles, et des communications inter-agents. Ajouter une discussion sur ces scénarios et sur la robustesse de PRAHOMT dans des environnements plus réalistes.

### **Critiques de la forme :**

#### 1. Clarté et organisation :
   - **Critique :** Le papier est jugé confus et certaines sections, comme l'introduction et les travaux connexes, nécessitent une révision approfondie pour une meilleure clarté.
   - **Suggestion :** Revoir l'introduction pour présenter clairement le problème, les contributions, et l'importance du travail. Réorganiser les travaux connexes pour qu'ils suivent un ordre logique, en partant des travaux les plus généraux vers les plus spécifiques à l'intégration de modèles organisationnels avec MARL.

#### 2. Références répétitives :
   - **Critique :** Des DOI sont référencés de manière répétitive, ce qui nuit à la lisibilité.
   - **Suggestion :** Nettoyer les références pour éliminer les duplications et assurer une citation cohérente et concise.

#### 3. Explication insuffisante des avantages spécifiques :
   - **Critique :** Le papier ne montre pas clairement en quoi MOISE+ et PRAHOMT sont meilleurs que les autres approches.
   - **Suggestion :** Ajouter une section qui met en avant les avantages uniques de MOISE+ et PRAHOMT en termes de flexibilité, sécurité, et stabilité par rapport à d'autres méthodes, avec des exemples concrets et des résultats expérimentaux.

### **Suggestions générales pour l'amélioration :**

1. **Ajouter des comparaisons et justifications supplémentaires** dans la section "Related Works" pour clarifier le choix des techniques et des modèles.
2. **Étendre les expérimentations** à des scénarios plus variés et complexes, et fournir une analyse comparative plus approfondie.
3. **Réorganiser le contenu** pour améliorer la fluidité de la lecture, en veillant à ce que chaque section introduise logiquement la suivante.
4. **Clarifier les contributions** de l'article en une section dédiée, en explicitant les différences avec les travaux antérieurs.

Ces modifications devraient aider à mieux répondre aux critiques des reviewers et à améliorer la qualité globale du document.


---
---


### Critiques de Fond

#### 1. **Justification du Choix du Modèle MOISE+**
- **Commentaire Reviewer #1 :** Pourquoi choisir MOISE+ plutôt qu’un autre modèle organisationnel comme AGR ? Une comparaison et une justification des avantages de MOISE+ par rapport à d'autres modèles sont nécessaires.
- **Suggestion :** Ajouter une section comparative qui montre pourquoi MOISE+ est mieux adapté pour des scénarios avec des contraintes organisationnelles et expliquer en quoi il est supérieur pour guider le processus d’apprentissage par rapport à d'autres frameworks comme AGR.

#### 2. **Choix de l'Apprentissage par Renforcement (RL)**
- **Commentaire Reviewer #1 :** Pourquoi utiliser le RL, en particulier les méthodes basées sur les politiques ? D'autres techniques comme la recherche de politique directe par neuro-évolution, les régulateurs linéaires quadratiques (LQR) ou le contrôle stochastique pourraient être pertinentes. Le papier entre dans le cadre du RL basé sur des modèles (model-based RL) mais ne discute pas d'autres alternatives comme le contrôle prédictif (MPC).
- **Suggestion :** Justifier pourquoi les techniques basées sur les politiques (policy-based RL) ont été choisies par rapport à ces autres techniques. Discuter des avantages spécifiques du RL par rapport à des approches basées sur l'optimisation ou des stratégies sans modèles.

#### 3. **Comparaison Expérimentale avec d'Autres Approches**
- **Commentaire Reviewer #1 et #2 :** Le papier manque de comparaison avec d’autres approches intégrant des spécifications organisationnelles dans le MARL.
- **Suggestion :** Inclure des expériences comparatives avec des méthodes utilisant des informations organisationnelles, comme ROMA ou des approches de co-apprentissage multi-agent. Comparer les performances en termes de convergence, robustesse et efficacité.

#### 4. **Qualité des Spécifications Organisationnelles**
- **Commentaire Reviewer #2 :** La performance des agents dépend fortement de la qualité des spécifications organisationnelles préalablement définies.
- **Suggestion :** Discuter des limitations potentielles de PRAHOMT lorsque les spécifications organisationnelles sont incomplètes ou mal définies. Proposer des stratégies pour automatiser ou apprendre ces spécifications à partir des données.

#### 5. **Utilisation et Extension de PRAHOM**
- **Commentaire Reviewer #3 :** Le papier ne clarifie pas suffisamment ce qui est emprunté de PRAHOM et ce qui est nouveau dans PRAHOMT. Les différences entre PRAHOM et PRAHOMT ne sont pas bien expliquées.
- **Suggestion :** Inclure une section spécifique expliquant en détail les contributions de PRAHOMT par rapport à PRAHOM. Mettre en avant les améliorations et les nouvelles fonctionnalités ajoutées, et expliquer pourquoi seules les missions et rôles sont utilisées.

#### 6. **Impact des Contraintes Organisationnelles dans des Scénarios Complexes**
- **Commentaire Reviewer #3 :** L'approche est testée dans un scénario relativement simple de prédateur-proie. Comment l'approche se généralise-t-elle à des scénarios plus complexes ?
- **Suggestion :** Ajouter des expériences ou des discussions sur des environnements plus complexes où les agents doivent coopérer de manière plus sophistiquée (par exemple, des tâches industrielles ou de sauvetage) pour montrer la robustesse et l’adaptabilité de PRAHOMT.

#### 7. **Explorations Alternatives comme le Model Predictive Control (MPC)**
- **Commentaire Reviewer #1 :** Le papier entre dans le cadre du model-based RL, mais ne discute pas d'autres alternatives comme le MPC.
- **Suggestion :** Inclure une discussion sur les avantages et inconvénients de PRAHOMT par rapport à des approches de contrôle prédictif (MPC) et d'autres méthodes d'optimisation basées sur des modèles.

### Critiques de Forme

#### 1. **Clarté de l'Introduction et des Objectifs**
- **Commentaire Reviewer #3 :** L'introduction est confuse et ne clarifie pas suffisamment les objectifs du travail.
- **Suggestion :** Réécrire l’introduction pour exposer clairement les objectifs du papier, les contributions principales, et la motivation derrière le choix de l’approche. Inclure un paragraphe expliquant pourquoi l'intégration des modèles organisationnels est importante pour le MARL.

#### 2. **Présentation et Organisation**
- **Commentaire Reviewer #1 et #3 :** Bien que l'organisation générale soit correcte, le texte contient des répétitions et manque de cohérence dans la présentation des concepts clés.
- **Suggestion :** Réorganiser les sections pour éviter les répétitions. Par exemple, regrouper les discussions sur PRAHOM et PRAHOMT dans une section dédiée, puis détailler la méthodologie.

#### 3. **Clarté de l'Écriture**
- **Commentaire Reviewer #3 :** Le texte est parfois confus et nécessite une révision complète.
- **Suggestion :** Simplifier le texte en utilisant des phrases plus courtes et des explications plus claires. Ajouter des exemples concrets pour illustrer les concepts complexes et améliorer la lisibilité globale.

#### 4. **Répétitions dans les Références**
- **Commentaire Reviewer #1 :** Certaines références sont répétées inutilement.
- **Suggestion :** Réviser les références pour éliminer les doublons et s'assurer que chaque référence apporte une information unique et pertinente.

#### 5. **Description des Expériences**
- **Commentaire Reviewer #2 :** Les expériences manquent de comparaisons avec d'autres algorithmes existants utilisant des informations organisationnelles.
- **Suggestion :** Ajouter des comparaisons directes avec d'autres algorithmes de MARL intégrant des informations organisationnelles, et fournir plus de détails sur les métriques et les configurations expérimentales.
