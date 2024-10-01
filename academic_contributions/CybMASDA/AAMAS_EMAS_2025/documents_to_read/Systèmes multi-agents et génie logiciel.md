# Systèmes multi-agents et génie logiciel

## 1. Introduction
- Évolution des machines et du Web → Applications distribuées complexes.
- Données et contrôles distribués logiquement, physiquement ou sémantiquement.
- Systèmes multi-agents (SMA) : macro-systèmes d’agents autonomes interagissant dans un environnement commun.
- Caractéristiques d’un agent :
  - Autonome et flexible.
  - Réactif et proactif.
  - Social, avec interaction entre agents via des langages de communication.
- Paradigme multi-agent : compréhension et modélisation des systèmes complexes en termes d'agents autonomes.

## 2. Processus de développement
- Méthodes de développement SMA inspirées de l’ingénierie orientée objet : cycles de vie en cascade, itératifs, en V, en spirale.
- Principales phases de développement :
  - Analyse des besoins.
  - Conception architecturale.
  - Conception détaillée.
  - Implémentation et déploiement.
- Exemple de méthodes :
  - ADELFE et INGENIAS : basées sur le processus unifié.
  - PASSI et ASPECS : processus itératif original.
  - GAIA et SODA : centrées sur l'analyse et la conception.
  - Prometheus et MaSE : excluent l'analyse des besoins.

## 3. Méta-modèles
- Importance des méta-modèles pour définir la nature des agents et du système associé à une méthode.
- Ingénierie dirigée par les modèles (IDM) : centraliser le développement sur les modèles plutôt que le code.
- Méta-modèles dédiés aux SMA et leur implémentation :
  - AMAS-ML dans ADELFE pour les agents coopératifs.
  - CRIO dans ASPECS pour les systèmes holoniques.

## 4. Analyse
- Analyse des besoins : identifier les fonctionnalités du système à concevoir, ses limites et contraintes.
- Méthodes centrées sur l’analyse des besoins : 
  - Tropos : cadre i* avec des acteurs et des dépendances stratégiques.
  - ADELFE, ASPECS, INGENIAS : analyse basée sur des rôles et interactions.
  - Prometheus : agents BDI.
- Lien entre les agents et les rôles, objectifs, interactions.

## 5. Conception
- Décrire le fonctionnement des agents et l'architecture générale du système multi-agent.
- Méthodes de conception :
  - GAIA : raffinage des modèles de rôle et d'interaction.
  - INGENIAS : définition de la société d’agents.
  - ADELFE : architecture d’agents coopératifs pour des comportements auto-organisateurs.
- Utilisation de modèles classiques (classes, interactions, comportements).

## 6. Implémentation
- Implémentation : production de code à partir des modèles conçus.
- Approches IDM : transformation des modèles en code.
- Exemples d’outils :
  - AMAS-ML et outil MAY dans ADELFE pour la génération de code spécifique.

## 7. Conclusion
- Les SMA facilitent la conception d’applications complexes et distribuées.
- De nombreuses méthodes de développement SMA existent, chacune avec ses spécificités.
- Certaines méthodes couvrent tout le cycle de vie, d'autres se concentrent sur l'analyse et la conception.
- L’avenir du développement SMA pourrait inclure des processus de développement adaptatifs et auto-configurables.

