# Méthodologie Gaia pour l'analyse et la conception orientées agents

## 1. Introduction
- Gaia : méthodologie pour l'analyse et la conception des systèmes multi-agents (SMA).
- Objectif : offrir un cadre pour modéliser et concevoir des systèmes complexes distribués.
- Applications typiques : systèmes où les agents sont des unités autonomes interagissant dans un environnement commun.

## 2. Caractéristiques des systèmes cibles de Gaia
- Les systèmes visés par Gaia sont :
  - **Grande échelle** : SMA à grande échelle, impliquant des ressources de calcul importantes pour chaque agent.
  - **Objectif global** : le système vise à maximiser une qualité globale, même si certains composants peuvent être sous-optimaux.
  - **Hétérogénéité** : les agents peuvent être implémentés avec différentes technologies.
  - **Structure statique** : les relations entre agents ne changent pas pendant l'exécution.
  - **Ressources statiques** : les capacités des agents et les services offerts restent constants.
  
## 3. Cadre conceptuel de Gaia
- **Modèles de Gaia** : permettent de passer des exigences à un design prêt pour l'implémentation.
- Concepts clés :
  - **Niveau macro (sociétal)** : interactions entre rôles au niveau de la société d'agents.
  - **Niveau micro (agent)** : comportements internes de chaque agent.
  
## 4. Analyse
- Objectif de l'analyse : comprendre la structure du système en définissant les rôles et leurs interactions.
- **Rôles** : les unités fonctionnelles abstraites au sein du système, définies par :
  - **Responsabilités** : propriétés de vivacité (actions à accomplir) et de sécurité (invariants à maintenir).
  - **Permissions** : ressources ou informations auxquelles le rôle a accès.
  - **Activités** : actions privées que l'agent peut accomplir sans interaction externe.
  - **Protocoles** : modèles d'interactions entre les rôles.
  
## 5. Conception
- La conception transforme les modèles abstraits en spécifications détaillées.
- Modèles clés :
  - **Modèle d'agent** : identifie les types d'agents et les instances à créer dans le système.
  - **Modèle de services** : spécifie les services associés aux rôles, leurs entrées, sorties, pré-conditions, et post-conditions.
  - **Modèle de connaissance** : définit les chemins de communication entre les agents.

## 6. Étude de cas : gestion de processus d'entreprise
- Exemple d'application de Gaia à un système de gestion de processus métier chez British Telecom.
- Description des rôles identifiés dans le système :
  - **CustomerHandler** : gère la communication avec le client et supervise le processus de génération de devis.
  - **QuoteManager** : gère le processus de devis, vérifie les clients et fournit les devis.
  - **CustomerVetter** : vérifie la solvabilité des clients.
  - **LegalAdvisor** : vérifie la légalité des demandes de services.
  - **NetworkDesigner** : conçoit le réseau pour répondre aux demandes de services spécifiques.
  - **Customer** : représente le client demandant un devis.

## 7. Comparaison avec d'autres méthodologies
- Problèmes des techniques orientées objets (OO) pour modéliser les agents :
  - Les agents ont une encapsulation plus forte que les objets.
  - Les modèles OO ne capturent pas bien les interactions dynamiques et les comportements autonomes des agents.
  
## 8. Conclusions
- Gaia offre un cadre flexible pour concevoir des SMA en tenant compte des aspects organisationnels et comportementaux des agents.
- Limites actuelles :
  - Gestion des systèmes dynamiques et ouverts.
  - Manque de protocoles de coopération riches.
  - Nécessité de normes internationales pour la communication entre agents.
