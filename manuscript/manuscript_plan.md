# Partie I — Introduction générale et construction de la démarche de recherche

**Objectif :** exposer le contexte de la cyberdéfense, présenter la revue critique des approches existantes, analyser leurs limites et justifier l'approche proposée. Introduire la méthode MAMAD, les hypothèses de travail, et l'organisation générale du manuscrit.

## Chapitre 1 — Contexte et problématique

**Objectif :** poser les fondations du domaine de recherche, identifier les enjeux de la cyberdéfense moderne, et formuler la question centrale de la thèse.

* 1.1 Évolution des menaces et besoins en cyberdéfense autonome
* 1.2 Vers une architecture agentielle (cadre AICA)
* 1.3 Problématique de conception d’un SMA de cyberdéfense
* 1.4 Question de recherche et objectifs scientifiques

## Chapitre 2 — Revue critique et émergence de l'approche

**Objectif :** présenter la revue de littérature réalisée, mettre en évidence les limites des approches existantes et motiver le recentrage vers le MARL guidé par organisation.

* 2.1 Conception classique des SMA : modèles symboliques, AOSE, architectures fixes
* 2.2 SMA en cybersécurité et cyberdéfense : état de l'art
* 2.3 Limites identifiées des approches existantes
* 2.4 Concepts clés pour une nouvelle approche : auto-organisation, adaptabilité, explicabilité
* 2.5 Recentrage vers l’apprentissage : RL/MARL et inférence non supervisée
* 2.6 Vers une structuration en 4 axes : modélisation, entraînement, analyse, transfert

## Chapitre 3 — Méthode, hypothèses et organisation du manuscrit

**Objectif :** formaliser la méthode MAMAD comme réponse à la problématique, présenter les hypothèses scientifiques H1–H5, et exposer le plan du manuscrit.

* 3.1 Méthode MAMAD : présentation générale
* 3.2 Hypothèses H1 à H5
* 3.3 Lien entre hypothèses et composantes de MAMAD
* 3.4 Organisation du manuscrit

---

# Partie II — Fondements théoriques et formels

**Objectif :** présenter les concepts et formalismes nécessaires, puis analyser chaque hypothèse à travers un état de l'art ciblé, l'identification d'un gap, et une reformulation justifiée.

## Chapitre 4 — Concepts transversaux pour la conception SMA/MARL

**Objectif :** définir les notions et modèles fondamentaux communs aux contributions.

* 4.1 Systèmes Multi-Agents : coordination, rôles, interactions
* 4.2 Modèles organisationnels : MOISE+
* 4.3 Apprentissage par renforcement multi-agent (MARL)
* 4.4 Intégration organisation-apprentissage

## Chapitre 5 — Analyse des hypothèses : état de l’art, gap, formulation

**Objectif :** pour chaque hypothèse H1–H5, analyser le domaine lié, identifier un manque, et formuler l’hypothèse comme réponse.

* 5.1 H1 : Formalisation du problème (Dec-POMDP contraint)
* 5.2 H2 : Modélisation par apprentissage de l’environnement (World Models)
* 5.3 H3 : Résolution par MARL adaptatif
* 5.4 H4 : Guidage organisationnel via contraintes MOISE+ (OAC/TRF)
* 5.5 H5 : Analyse organisationnelle (rôles/objectifs émergents)

---

# Partie III — Méthodologie de conception : MAMAD

**Objectif :** présenter en détail les 4 phases de la méthode MAMAD et les contributions associées. On montre aussi comment la méthode et chaque phase est aussi pensé pour la conception d'un AICA auto-organisé, adaptatif...

## Chapitre 6 : MAMAD comme réponse intégrée

* 6.1 Principe général et boucle itérative
* 6.2 Architecture globale

## Chapitre 7 : Phase 1 — Modélisation

* 7.1 Reconstruction partielle de l’environnement
* 7.2 Apprentissage de la dynamique observable
* 7.3 Intégration des contraintes de déploiement

## Chapitre 8 : Phase 2 — Apprentissage guidé (MARL contraint)

* 8.1 Cadres d’entraînement MARL utilisés
* 8.2 Contraintes organisationnelles dans MARL (OAC, TRF)
* 8.3 Politique composite et filtrage d’actions

## Chapitre 9 : Phase 3 — Analyse post-entraînement

* 9.1 Méthodes d’inférence des rôles et objectifs
* 9.2 Indicateurs : SOF, FOF, OF
* 9.3 Outil TEMM : fonctionnement, cas d’usage

## Chapitre 10 : Phase 4 — Transfert et supervision

* 10.1 Modes de transfert (centralisé/distribué)
* 10.2 Bouclage entre environnement réel et simulation

---

# Partie IV — Évaluation expérimentale

**Objectif :** valider les hypothèses, tester la méthode MAMAD sur des scénarios concrets, analyser les résultats. Enfin, analyser les apports de manière transversale par rapport à la question de recherche, discuter les limites de la méthode et la positionner par rapport à la littérature.

## Chapitre 11 : Implémentation et outils 
* 11.1 CybMASDE
* 11.2 MOISE+MARL

## Chapitre 11 : Protocole expérimental

* 12.1 Objectifs d’évaluation
* 12.2 Configuration, métriques, baselines

## Chapitre 13 : Études de cas

* 13.1 Scénario 1 : Infrastructure d’entreprise
* 13.2 Scénario 2 : Essaim de drones
* 13.3 Scénario 3 : Orchestration Kubernetes

## Chapitre 14 : Résultats et synthèse

* 14.1 Validation des hypothèses H1 à H5
* 14.2 Comparaison entre scénarios
* 14.3 Discussion des résultats

## Chapitre 15 : Analyse croisée des contributions

* 15.1 Conditions de validité et généralité
* 15.2 Positionnement dans l’écosystème de recherche

---

# Partie V — Conclusion et perspectives

**Objectif :** récapituler les apports, identifier les limites, et proposer des perspectives de recherche et de valorisation.

## Chapitre 16 : Bilan de la thèse

* 16.1 Synthèse de la démarche et des résultats
* 16.2 Limitations techniques, théoriques, expérimentales

## Chapitre 17 : Perspectives et ouvertures

* 17.1 Perspectives scientifiques à court et long terme
* 17.2 Ouvertures industrielles, valorisation, feuille de route AICA
