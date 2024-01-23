# Introduction

## Genèse / contexte du sujet

* AICA, besoins nouveaux, IoT/IoBT, etc.
* Approche centralisée peu adaptée, etc. pour des raisons d’interruptions de communication, hétérogénéité des SI, etc.
* Une approche MA pourrait être appliquée -> Système Multi-Agents de Cyberdéfense (SMAC)
* Mais sujet nouveau : pas de modélisation, travaux formels…

## Problématique générale

* Quelle méthode pour concevoir un SMAC qui atteint ses objectifs de cyberdéfense tout en satisfaisant les contraintes de déploiement et opérationelles du système hôte qu'il doit défendre ?

##	Positionnement et thèse défendue

* Un ensemble d’agents collaboratifs répond effectivement aux nouveaux besoins, etc. mieux que des solutions centralisées
* Une modélisation du "domaine" (environnement réseau + actions/observations possibles des red/blue/green teams), du "problème" (objectif de cyberdéfense / blue team + contraintes opérationelles/déploiement) sous forme d'un **problème d'optimisation sous-contraintes** ; permet de fournir des moyens objectifs d’évaluer de façon consistante si le SMA tient ses promesses dans plusieurs scénarios d’attaque…
# Aperçu du domaine et du problème 

##	Définitions et propriétés
* Définitions & propriétés fondammentales pour la suite
* cyberdéfense, RL et SMA (+IA hybride éventuellement)
* ex : ouverture, dynamique, auto/réorganisation, explicabilité, etc.

##	Aperçu des travaux liés
* Travaux liés à l’AICA et autres SMA de Cyberdéfense
  * SMA : organisation, modèle organisationel...
  * MARL : travaux de l'ACO
  * ...

##	Limitations et discussion
* Manque de généricité, consistance, pas/peu objectif, peu formel, etc.
* Besoin d’un cadre théorique consistant et générique si possible

##	Choix du cadre théorique
* Motivation pour : Green, blue, red teams + réseau de noeud avec système d’ataque/contre-attaques d’après les standards de cyberdéfense, reste générique, etc.

##	Approches de modélisation pour un SMA de Cyberdéfense
* Modèles partiels (Attack-defense tree, petri nets, etc)
* Modèles de la théorie des jeux (POSG, Dec-POMDP, etc.)

##	Comparaison et choix du modèle
* Tableau comparatifs, discussion…
* Motivations pour le Dec-PODMP d’après le rapprochement entre incertitude des observations, conditions pour les actions, dynamique de l’env, récompense collective et non individuelle, etc.
* Le Dec-POMDP reste assez générique : plusieurs approche d’organisation / mécanismes / algos d’IA sont envisageable dans ce cadre formel


# CybMASFM: Cyberdefense Multi-Agent Systems Formal Model

##	Modèle proposé du domaine
* Montrer comment le cadre théorique non-formel (environnement + teams) peut être formalisé dans le Dec-POMDP



##	Expression du problème
**Ici je parle de MARL comme d'une solution au modèle pas comme d'une inspiration du modèle ; Dec-POMDP = modèle et MARL = approche de résolution possible ; on ne doit pas encore comprendre que le MARL sera choisi pour la suite en combinaison des modèles d'organisation de SMA comme Moise+**
* L'environnement peut être traduit en contraintes qui réduit l'espace des organisations (i.e joint-policy) à celles qui sont réellement possibles (cf. Moise+)
* Les spécifications appliquées à l'OE contraignent également l'espace des organisations (i.e joint-policy) à celles qui sont spécifiées par le concepteur
* Les objectifs de cyberdéfense peuvent être traduits en une fonction à maximiser
* **Problème** : Trouver l’ensemble des politiques (joint-policy) respectant les contraintes telles que sur un épisode, la récompense cumulée des agents bleus soit maximale / supérieur à un seuil
  * Pour une fonction de récompense donnée Rew, les variables inconnues à maximiser sont les politiques PIj (1<j<nb agents):
  		max (Sum{1, .., i, .., nb_it} Rew(PI1, PI2, …, PIn))
  * De plus, la joint-policy obtenue doit être associé à des specifications compréhensibles pour un être humain (gros problème d'explicabilité sinon...)
    * Design(Env., Specs_init, JointPolicy_init) = (Specs_opt, JointPolicy_opt)
* Maintenant que l'on a posé le problème il faut le résoudre...


# CybMASDA: Cyberdefense Multi-Agent Systems Developpment Approach

## Une vision unifiée de la conception d'une organisation dans les SMA
* Expliquer comment nous envisageons les organisations possibles au travers de : Conscience/inconscience de l’organisation + Centré agent / organisation.
  * Positionnement par rapport à la littérature
* Expliquer comment à partir du problème défini, on peut integrer la conception d'une organisation dans les 3 cas ci-dessous
* **Les organisations totalement prédéfinis** :
  * Les Specs_init contraignent totalement le processus de conception à une seule organisation possible
  * 1 seul épisode : chaque agent suit une liste de règles (associant un ensemble d’observation à une action) qui ne changent jamais (sans apprentissage mais basé sur la connaissance/expertise du concepteur) : hiérarchie, mécanisme d’enchère, coalition, etc.
  * Coalition based Multi Agent System AICA (CMASA), Market based Multi Agent System AICA (MMASA), etc.
* **Les organisations totalement indéfinies**
  * Les Specs_init n'ont aucun impact sur la façon dont on peut concevoir les agents (le concepteur humain ou MARL peut choisir librement comment concevoir les règles des agents)
  * Plusieurs épisodes : chaque agent voit ses propres règles changer quand cela maximise la récompense (QLearning, DQN en full automatique ou bien le concepteur humain)
  * Aboutit à une solution local (ensemble de politique) mais pas facilement explicable en MARL (d'où le besoin d'avoir des spécifications en même temps)
  * QLearning based Multi Agent System AICA (QMAS), etc.
* **Les organisation semi-définies**
  * Les Spec_init couvrent partiellement l'espace des organisations possibles
    * Par exemple : trouver des SMA satisfaisant l'architecture hierarchique mais sans savoir précisement quel agent doit adopter quel rôle, etc.
  * Mécanisme d’organisation déjà en place mais les hyper-paramètres doivent être ajustés avec un apprentissage
  * Mix entre agents au politique définis et indéfinis
  * D’abord indéfini avec recherche du mécanisme d’organisation défini optimal pour le scénario donné
  * Adaptive Multi Agent System AICA (AMASA) : Une architecture polyvalente pour un SMA de Cyberdéfense, etc.

## Approche de conception théorique combinant MARL et modèle d'organisation de MAS

## Approche de développement basée sur des cycles de simulation et émulation

##	La simulation pour une approche multi-agent de cyberdéfense
* Présentations des travaux correspondant au mieux aux besoins des SMA et de la cyberdéfense
* Comparaison et aboutissement sur l’idée d’étendre l’environnement CybORG du framework PettingZoo (code libre, issu d’un travail de recherche précédent publié à IJCAI, contexte d’application très proche et pertinent, compatibilité avec le modèle Dec-POMDP précédent, etc.)
# L’extension porte essentiellement sur la fonction d’évaluation, déploiement des agents, contraintes de l’embarqué, communication entre agents pour mieux prendre en compte l’aspect MA

## Une approche expérimentale pour évaluer un SMA de Cyberdéfense
* Montrer comment CybMASDE peut être utilisé de façon systématique/consistante pour définir un scénario (env, red team, green team) + une blue team (i.e un SMA de cyberdéfense) en définissant soit même les politiques des agents
* Montrer que les modèles de la simulation peuvent être mappés à des modèles émulés afin de verifier la veritable performance des SMA de cyberdéfense proposé AVEC l'intérêt du transfer learning pour l’apprentissage dans la simulation (car rapide et leger) et vérification dans l’émulation (machines virtuelles)
* Présentation de 3 cas d’études : Drone swarm, company network et mixed domotic IoT

# CybMASDE: Cyberdefense Multi-Agent Systems Developpment Environment

# Expérimentation et comparaisons

##	Aspects Multi-agents & Cyberdéfense
##	Evaluation pour les 3 cas d’étude dans l’approche simulation et émulation
##	Synthèse et discussions

# Conclusion

##	Problématique
##	Contribution de l’approche pour la cyberdéfense
##	Vers une application industrielle comme aide à la décision
* Simuler des événements qui pourraient arriver et essayer de gagner de l'expérience en prévision du moment où l’attaque sera déjà en cours
# Bibliographie
