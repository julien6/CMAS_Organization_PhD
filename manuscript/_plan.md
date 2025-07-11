# Présentation Paul Théron sur le manuscrit

Objectifs:
 - finir le manuscrit
	 - fusionner les parties ajoutées
 - faire une présentation du manuscrit
	 - présenter l'intro
		 - contexte = explosion du monde IoT... hétérogenité, augmentation de la surface d'attaque...
		 - motivation = besoin de protéger les système en réseaux sur les potentiels points d'entrée avec une approche décentralisée et distribuée de cyberdéfense
		 - question de recherche = Comment concevoir automatiquement un SMA de Cyberdéfense qui optimise constament l'atteinte de son objectif de protection compte tenu des contraintes dynamiques de l'environnement de déploiement, des menaces cyber et d'exigences de conception ?
		 	- 4 verrous théoriques sont considérés dans cette question:
				1) Faible généralisabilité et automatisation des approches de conception de SMA de Cyberdéfense
				2) Peu d'adaptivité dans la réponse cyber vis à vis des contraintes dynamiques de l'environnement et des attaques cyber
				3) Faible explicabilité des SMA émergents
				4) Risque lié à l'experimentation directe en environnement réel
				5) Pas de formalisation du problème de conception d'un SMA de Cyberdéfense
		 - hypothèses pour répondre à la question = 
			 1) Concevoir un SMA de Cyberdéfense qui effectue au mieux son objectif de Cyberdéfense compte tenu de l'environnement (incluant les attaquants) et des exigences de conception, peut-être reformulé comme un Dec-POMDP modélisant le problème d'optimisation des politiques des agents sous des contraintes données pour maximiser la récompense qui modélise le succès des agents dans l'atteinte de l'objectif de cyberdéfense ;
			 2) L'utilisation de techniques "World Models" peut permettre de modéliser automatiquement, au moins partiellement, l'environnement comme une simulation permettant d'implémenter la fonction de transition d'état et la fonction d'observation utilisables dans la définition du problème ;
			 3) Ce problème peut être résolu automatiquement, au moins approximativement, par l'utilisation de techniques MARL ;
			 4) Les contraintes extrinsèques issues des exigences de conception, peuvent être intégrées dans le processus MARL en étant formalisées dans une vision organisationnelle explicite et transparente comprenant des roles et des objectifs, restreignant l'espace des politiques ;
			 5) Les comportements des agents entraînés peuvent également être vus avec une vision organisationnelle explicite et transparente comprenant des rôles et des objectifs comme éléments d'explicabilité permettant de comprendre les interactions des agents au niveau individuel et collectif.

		 - moyen de vérifier l'hypothèse: Nous proposons plusieurs contributions prenant appui sur les hypothèses précédentes que nous orchestrons dans une méthode de conception offrant une pipeline automatisée fermée de conception d'un SMA de Cyberdéfense. Cette méthode se décompose en 4 étapes séquentielles cycliques:

---

### 🔹 Étape 1 — Modélisation : Construction d’un Observation-based MDP (OMDP)

Cette étape introduit une première contribution centrée sur la **modélisation automatisée de l’environnement de déploiement**, en s’appuyant sur les approches dites *World Model*. À ce stade, on dispose d’un **ensemble conséquent de trajectoires** (ou historiques) d’agents, collectées lors de phases d’exploration avec la politique conjointe courante — initialisée de manière aléatoire à la première itération. Ces trajectoires sont stockées dans une base de données et exploitées pour construire un **Observation-based Markov Decision Process (OMDP)**, qui joue le rôle de **modèle de simulation**.

Dans ce OMDP, les **nœuds** correspondent à des **observations conjointes** $o_{\text{joint}} \in \Omega_1 \times \cdots \times \Omega_n$, et les **arêtes dirigées** représentent les **actions conjointes** $a_{\text{joint}} \in A_1 \times \cdots \times A_n$, donnant lieu à une dynamique $o^t_{\text{joint}} \xrightarrow{a^t_{\text{joint}}} o^{t+1}_{\text{joint}}$. À partir de cette structure, deux types de **fonctions prédictives d’observation** (Predictive Observation Functions, ou POF) sont dérivées :

#### a) Fonction prédictive exacte mais partielle :

On construit une fonction empirique

$$
\mathcal{O}_{\text{partielle}} : H_{joint} \times A_{joint} \rightarrow \Omega
$$

qui, pour un historique partiel $h_i^t$ et une action $a_i^t$, retourne une observation probable $o_i^{t+1}$ **si** une trajectoire identique ou très proche a déjà été observée dans l’OMDP. Cette fonction s’appuie sur la recherche de sous-trajectoires similaires dans la base, et permet de prédire l’observation suivante **lorsque la situation a déjà été rencontrée**.

#### b) Fonction prédictive généralisée :

On entraîne une version approximative et généralisée de

$$
\mathcal{O}_{\text{approx}} : H_{joint} \times A_{joint} \rightarrow \Omega
$$

à l’aide d’un modèle basé sur une architecture de **réseau de neurones récurrent (RNN)**, capable d’apprendre la dynamique de génération des observations à partir d’un grand nombre d’historiques. Cette fonction vise à **généraliser au-delà des trajectoires déjà vues**, en capturant les régularités dans la structure de l’environnement à travers l’évolution des observations conditionnées aux actions.

### 🔹 Étape 2 — Entrainement : 

            2) Entrainement : Cette étape intègre une deuxième contribution sur l'intégration d'un modèle organisationnel comprenant des spécifications structurelles et fonctionnelles pour formaliser les exigences de conception et les rendre effectifs dans le processus d'apprentissage MARL pour résoudre le problème Dec-POMDP. Les roles sont représentés par une relation qui à chaque couple (historique, observation) associe l'ensemble des actions attendues priorisées par un poids (l'implémentation de cette relation peut prendre la forme d'un script ou d'un ensemble de règles utilisant possiblement des TP). Les objectifs sont représenté par une relation qui à tout historique associe un bonus/malus en se basant sur l'analyse de l'historique de l'agent pour détérminer si l'agent se rapproche d'un des objectifs intermediaires (son implémentation peut prendre la forme d'un script ou utiliser des règles TP). Dans cette étape, les rôles et les objectifs prédéfinis sont integrées dans le framework proposée MOISE+MARL pour lancer l'entrainement et utiliser le processus de HPO que nous proposons pour le reste (en ayant la possibilité de prédéfinir des hyper-paramètres).
            3) Analyse : Cette étape intègre une troisième contribution qui est la méthode proposée TEMM permettant l'analyse des trajectoires par des techniques d'apprentissage non-supervisées, des agents entrainés pour extraire des éléments d'explicabilité des agents au niveau individuels et collectifs sous la forme des spécifications organisationnelles issues du modèle MOISE+. La première hypothèse sous-jacente de cette contribution est qu'un role peut être vu comme un ensemble très fréquent de transitions observables que l'on peut reformuler comme un ensemble de règles de transition représentant un role. La deuxième hypothèse sous-jacente est qu'un objectif est qu'un objectif intermediaire peut être vu comme un ensemble d'état ou observations que les agents doivent traverser très fréquement, représentant une étape intermediaire que l'on peut considérer comme un objectif. Dans cette étape, la pipeline de cette méthode est appliquée en suivant plusieurs étapes commençant par la préparation des trajectoires, puis le clustering hierarchique des trajectoires pour extraire des patterns de transitions et d'observations caractéristiques qui sont ensuite utilisées pour inferrer des roles et des objectifs.
            4) Transfert : Cette étape intègre une contribution technique en tant que framework qui structure l'implémentation de la méthode en un jumeau numérique (dans lequel s'éxécute une pipeline éxécutant les étapes de modélisation, d'entrainement et d'analyse ont lieu) et un composant "Transferer" qui permet de lier le jumeau digital avec l'environnement cible. Il permet deux tâches :
				- a) Le transfert régulier des politiques des agent obtenus après entrainement du jumeau numérique vers le système cible de déploiement: Les poltiques entrainées des agents sont transferées dans l'environnement réel selon deux modes: 1) "execution à distance" : les politiques des agents sont executées sur un noeud central éventuellement externe à l'environnement et les actions sont appliquées à distance ; 2) "éxécution directe" : les politiques des agents sont copiées sur les systèmes hôtes des agents eux-mêmes en considérant qu'ils ont les capacités en mémoire et en calcul d'executer les modèles entrainés. Dans cette étape, l'environnement est considéré comme accessible ponctuellement pour effectuer la mise à jour des politiques des agents. Durant la mise à jour des politique, l'ancienne politique continue d'être active tandis que la nouvelle politique est en cours de copie. Une fois la copie effectuée, la nouvelle instance est activée tandis que l'instance ancienne de la politique des agents est désactivée. 
				- b) La collecte en continu des trajectoires des agents : en executant leur politique, les agents sont amenés à générer des trajectoires. Dans le cas de l'éxécution à distance, les trajectoires sont collectées directement depuis le "Transferer" et transmis au jumeau numérique. Dans le cas d'une "éxécution interne", les agents peuvent garder en mémoire leur trajectoire sur un nombre de step variable (en fonction des capacité de mémoire) et les envoyer au "Transferer" qui les transmettrra au jumeau numérique durant les moments de connexion possible entre le jumeau numérique et l'environnement cible sur des intervals de temps donnés.
	 - présenter le raisonnement/logique du manuscrit

------
Etat actuel du manuscrit


## Chapitre 1 : Introduction

### Section 1.1 : Un contexte de Cyberdéfense avec des défis futurs et nouveaux 
% Contexte général : Présenter le contexte dans lequel le sujet de la thèse s'inscrit

### Section 1.2 : L’idée d’un système multi-agents de Cyberdéfense
% Contexte spécifique : Présenter le SMA de Cyberdéfense et son histoire comme point de départ du sujet de thèse

### Section 1.3 : Question de recherche
% Problème : Présenter la question de recherche

### Section 1.4 : Démarche de construction de la réponse, hypothèses de la thèse
% Contribution : Présenter la démarche de recherche qui a conduit à proposer une méthode (MAMAD) comme réponse à la question de recherche et les hypothèses associées soutenant cette réponse.

### Section 1.5 : Organisation du manuscrit
% Organisation : Présenter l'organisation du manuscrit:
 - Partie I : présenter les bases pour chaque hypothèse, état de l'art pour chaque hypothèse, les verrous à franchir pour prendre appuie pleinement sur les hypothèses précédentes compte tenu des lacunes de la littérature
 - Partie II : présenter la méthode comme réponse principale qui orchestre toutes les contributions théoriques, puis détailler ces mêmes contributions qui permettent de combler les verrous théoriques et techniques identifiés précédement
 - Partie III : présenter le cadre experimental en commençant par l'implémentation de chacune des contributions théoriques et l'implémentation finale de la méthode MAMAD (qui est un logiciel qui s'appelle CybMASDE) ; puis expliquer le protocole experimental adopté (environnements, configuration matériel, baselines avec différentes spécifications organisationnelles...). Enfin, présenter et discuter des résultats vis-à-vis des verrous identifiés
 - Chapitre 6 : conclure en commençant par résumer brièvement le contexte, problème, hypothèse, gaps, contributions, experimentations et résultats avec discussion ; Ensuite, on doit pouvoir établir un plan structuré des différents travaux futurs comme ouverture de thèse afin de se rapprocher le plus possible d'une contribution de recherche pour développer un agent AICA pleinement opérationel.

# Partie I : notions, état de l'art, verrous, hypothèses

## Chapitre 2 : Vers un système multi-agents de cyberdéfense

### Section 2.1 : Concepts dans les systèmes multi-agents et l’organisation

### Section 2.2 : Un état de l’art en matière de Cyberdéfense distribuée ou décentralisée

### Section 2.3 : Synthèse et identification des verrous théoriques

## Chapitre 3 : Problèmes détaillées et hypothèses de travail

### 3.1 Problèmes à considérer

### 3.2 Hypothèses et contributions proposées


# Partie II : contributions théoriques

## 4.2 Présentation générale de la méthode MAMAD

## Modélisation

## Entrainement

## Analyse

## Transfert

# 4.3 La méthode MAMAD orientée pour l'AICA

## Une modélisation en simulation adaptée aux environnements cyber

## Un cadre de spécifications organisationnelles pour l'AICA

## Une analyse des comportements adaptés aux environnements cyber

## Un framework de transfert adapté aux environnements cyber


# Partie III : implémentation, cadre experimental, évaluation et discussion

## 5 Implémentation et configuration matérielle

### 5.2 MOISE+MARL : Un outil pour adapter le MARL à une vision organisationnelle

### 5.1 CybSMADE : Environnement de développement de systèmes multi-agents de Cyberdéfense

## 6 Experimentation et évaluation

### 6.2 Expériences à travers trois études de cas

### 6.3 Un scénario d’infrastructure d’entreprise

### 6.4 Un scénario d’essaim de drones

### 6.5 Un scénario d’Architecture de microservices

## 5.6 Résultats et discussion

## 5.7 Tendances générales qui ressortent des résultats et de la synthèse

## 6 conclusion et travaux futurs

### 6.1 Vers une application industrielle pour la prise de décision en matière de Cyberdéfense

### 6.2 Limitations et perspectives
