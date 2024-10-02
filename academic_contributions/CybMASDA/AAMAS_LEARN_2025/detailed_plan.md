### I) Introduction

**Contexte**

Le MARL peut être considéré comme une approche permettant de résoudre le problème de trouver une politique conjointe qui guide les agents vers l'atteinte d'un objectif donné dans un environnement spécifique.

Cette politique conjointe ne définit pas seulement les actions individuelles des agents, mais régit également leurs interactions entre eux, voire avec l'ensemble des autres agents, sans préconception d'un ordre ou d'une structure organisationnelle.

Toutefois, dans certains environnements, les contraintes imposées font que de nombreuses solutions optimales ou satisfaisantes conduisent à des comportements qui ressemblent à une organisation structurée et fonctionnelle, comparable à celle des organisations humaines.

Une idée intuitive est que cette ressemblance entre la politique et une organisation structurée et fonctionnel n'est qu'une interprétation inspirée des sociétés humaines. Cela revient à associer les comportements des agents entraînés à des rôles, où chaque rôle délimite les actions possibles des agents et semble répondre à des fonctions précises, contribuant ainsi à maximiser la récompense dans l'atteinte de l'objectif final.

De manière plus générale, on peut interpréter les comportements des agents entraînés comme appartenant à un continuum allant d'un collectif d'agents déstructurés et non fonctionalisés à une organisation pleinement structurée et fonctionnelle. Cette ressemblance naturelle entre la politique conjointe avec une organisation structurée et fonctionnelle est fondamentalement influencée par les contraintes environnementales et les objectifs fixés.

Au-delà des contraintes environnementales et de l'objectif initial, l'ajout de contraintes spécifiques peut encourager ou forcer les agents à adopter une organisation plus structurée et fonctionnelle, définie par l'utilisateur. Cela peut par exemple se faire en reprenant et affinant les rôles et sous-objectifs de l'organisation émergente issue de la politique conjointe.

Nous appelons cette similitude entre la politique conjointe et une organisation structurée et fonctionnelle "adéquation organisationnelle".

**Problème**

Ce papier vise à explorer deux problèmes centraux liés à l'adéquation organisationnelle dans les systèmes multi-agents.

1. **Évaluation de l'adéquation organisationnelle** : Ce problème consiste à évaluer dans quelle mesure une politique conjointe peut être rapprochée d'une organisation structurée et fonctionnelle. Un des enjeux de ce problème est de mieux comprendre les cas où les agents peuvent être considérés comme formant une organisation structurée et fonctionnelle compte tenu des contraintes imposées par l'environnement, l'objectif et d'autres contraintes optionnelles.

    La littérature aborde l'évaluation des politiques en termes de rôles (structure) ou d'objectifs (fonction). Cependant, ces travaux manquent souvent d'une approche systématique et générale. Les méthodes actuelles offrent peu d'outils clairs pour mesurer de manière quantitative et qualitative cette adéquation organisationnelle.

2. **Contrôle de l'adéquation organisationnelle** : Ce problème consiste à guider les agents vers des politiques qui se conforment à une organisation structurée, définie par des contraintes spécifiques prédéfinies par l'utilisateur. L'objectif est de contraindre ou d'inciter les agents à adopter des comportements qui respectent des rôles et des missions, ce qui permet de contrôler leurs actions dans un cadre organisationnel. Les enjeux incluent la réduction de l'espace de recherche des politiques, l'amélioration de la convergence, et la garantie du respect des contraintes de sûreté.

   Les travaux existants dans ce domaine sont limités, notamment en ce qui concerne la manière dont l'utilisateur peut interagir avec les spécifications organisationnelles de manière pratique et flexible.

**Contribution**

Pour répondre à ces deux problèmes, nous proposons deux contributions majeures :

1. **MOISE+MARL Framework (MM)** : Nous introduisons un nouveau framework de MARL qui intègre le modèle organisationnel MOISE+ dans l'apprentissage multi-agent. Ce framework permet de formaliser et de contraindre les politiques des agents en introduisant des **spécifications organisationnelles** que sont les rôles et les missions issus du modèle MOISE+. Les spécifications organisationnelles peuvent être appliquées manuellement aux agents sous forme de contraintes additionnelles, affectant automatiquement à la fois leurs politiques et la fonction de récompense. Ce framework introduit également des structures de données spécifiques telles que des patterns de comportement et des arbres de décision basé sur les patterns de comportements pour permettre à l'utilisateur de définir des rôles et des objectifs.

2. **History-based Evaluation in MOISE+MARL (HEMM)** : Nous proposons un algorithme permettant d'évaluer quantitativement et automatiquement l'adéquation organisationnelle des politiques apprises. Cet algorithme utilise des techniques d'apprentissage non supervisé pour généraliser des rôles et des missions à partir de l'ensemble des comportements observés au cours de plusieurs épisodes de test. En mesurant l'écart entre les spécifications organisationnelles abstraites inférées et les comportements réels, nous définissons une nouvelle métrique multi-dimensionnelle, le **niveau d'adéquation organisationnelle**, qui quantifie dans quelle mesure une politique se conforme aux spécifications organisationnelles inferées.

**Evaluation & Trouvailles**

Nous avons évalué conjointement MOISE+MARL et HEMM en mettant en jeu:
 - Quatre environnements présentant différentes contraintes environnementales et objectifs dont pour certains on s'attend à ce que les politiques conjointes efficaces soient proches ou éloginées de politique adéquates organisationnellement. Ces environnements sont: overcooked, predator-prey, warehouse management, ant simulation
 - Deux algorithmes MARL policy-based (Multi-Agent REINFORCE et MAPPO) connus pour favoriser une convergence stable, deux algorithmes Actor-Critic (MADDPG et SAC), un algorithme value-based (DQN) et un algorithme model-based (Dyna-Q) qui favorise la performance sur le long terme.
 - Trois ensembles de spécifications organisationnelles pour chacun des environnements de sorte à contraindre progressivement davantage les agents à se conformer à des comportements prédéfinis ou leur permettre plus de degré de liberté.

Nous vérifions bien que :
 - Dans les environnements perçus comme plus susceptibles de faire émérger des politiques adéquates organisationnellement, on peut non-seulement manuellement constater que les agents semblent se conformer à des rôles "naturels" pour atteindre des objectifs "naturels", mais aussi vérifier que le "niveau d'adéquation organisationel" inferé par HEMM est plus important dans ces environnements par rapport aux autres. Les rôles et missions inferés via HEMM correspondent aux observations manuelles et attentes.
 - Les algorithmes policy-based en particulier MADDPG semblent plus appropriés pour faire converger les agents vers des politiques stables nécéssaires pour permettre aux agents de tendre à des comportements homogènes à chaque épisode. A contrario, les algorithmes value-based tels que Q-Mix, montre une trop grande variance de comportement bien que les performances des agents restent élevées.
 - L'application de spécifications organisationnelles issues d'ensemble de spécifications contraignants augmentent significativement le "niveau d'adéquation" calculé via HEMM tandis que les rôles et missions obtenus par généralisation via HEMM sont quasiment identiques aux spécifications prédéfinies appliquées. Cela prouve que le framework MOISE+MARL permet bien de controler les agents par le biais de spécifications organisationnelles prédéfinies et que les modifications opérées dans les politiques au moyen de contraintes ou incitations sont retrouvables quasiment à l'identique avec HEMM.

**Structure du papier**

La suite du papier est organisée comme suit :
- **Section II** : Met en relation le problème du contrôle de l'adéquation organisationnelle vis-à-vis des travaux de les SMA et le MARL.
- **Section III** : Introduit le framework MOISE+MARL et montre comment il permet le controle de l'adéquation organisationnelle.
- **Section IV** : Introduit le problème de l'évaluation de l'adéquation organisationnelle au regard des travaux existants.
- **Section V** : Introduit l'algorithme HEMM qui propose une approche quantitative pour l'évaluation de l'adéquation organisationnelle.
- **Section VI** : Décrit le protocole experimental et justifie les choix relatifs au protocole d'experimentions tels que les environnements, les algorithmes MARL et hyper-paramètres choisis.
- **Section VII** : Présentation des résultats expérimentaux.
- **Section VIII** : Discussion et conclusion sur l'évaluation et le contrôle de l'adéquation organisationnelle par les contributions proposées.

---

### II) Le contrôle de l'adéquation organisationnelle dans la litterature

Dans cette section, nous abordons le problème de guider les agents multi-agents vers des politiques respectant des spécifications organisationnelles. Les principaux défis incluent la formalisation de rôles et de missions adaptés, ainsi que la garantie que les politiques apprises soient sûres, interprétables et efficaces.

---

### III) Le Framework MOISE+MARL

Le framework MOISE+MARL permet d'étendre les concepts d'organisation dans le cadre de l'apprentissage multi-agent. Il repose sur l'intégration des rôles et des missions comme contraintes supplémentaires pour les agents, influençant à la fois leurs actions et la manière dont ils perçoivent les récompenses.

---

### IV) Le problème de l'évaluation de l'adéquation organisationnelle dans la littérature

L'évaluation de l'adéquation organisationnelle consiste à déterminer si les politiques apprises par les agents peuvent être interprétées comme une organisation structurée. Cette section présente les approches et les défis actuels dans ce domaine.

---

### V) L'algorithme HEMM

L'algorithme HEMM vise à inférer et évaluer les rôles et missions des agents dans un environnement multi-agent, à partir de l'historique des actions et observations. Il généralise les comportements en créant des structures organisationnelles implicites basées sur les actions des agents et en identifiant des sous-objectifs à partir des observations. Voici une formalisation propre de cet algorithme.

#### Définition des Concepts Clés

- **Rôle** : Un agent ayant un rôle est contraint à se comporter de manière stéréotypée en suivant un ensemble de règles. Ces règles peuvent être explicites ou implicites et dictent les actions possibles dans certains états ou sous-objectifs.
  
- **Objectif** : Un objectif est une tâche ou un but que l'agent cherche à atteindre. Un agent cherchant à atteindre un objectif suit un ensemble limité mais pertinent d'historiques. Chaque objectif est potentiellement composé de plusieurs sous-objectifs atteints à travers des actions cohérentes.

#### Etapes de l'algorithme HEMM

1. **Génération d'un ensemble d'historiques conjoints** :
   - Soit un ensemble $\Pi = \{\pi_1, \pi_2, ..., \pi_n\}$ de politiques individuelles pour les agents. La politique conjointe $\pi_c$ est définie par l'ensemble des politiques individuelles agissant de manière synchronisée.
   - L'algorithme génère un ensemble $\mathcal{H}$ d'historiques conjoints $\mathcal{H} = \{H_1, H_2, ..., H_k\}$ en simulant $\pi_c$ dans l'environnement pour un certain nombre d'épisodes. Chaque historique $H_i$ est une séquence d'états, actions et observations $(s_t, a_t, o_t)$ pour chaque agent à chaque instant $t$.

2. **Généralisation des structures organisationnelles** (basée sur les actions) :
   Pour chaque historique conjoint $H_i$ :

   2.1 **Représentation des historiques sous forme de séquences d'actions** :
   - Chaque historique $H_i$ d'un agent $j$ est représenté comme une séquence d'actions $A_j = \{a_1, a_2, ..., a_T\}$, où $T$ est la longueur de l'historique.

   2.2 **Clustering hiérarchique des séquences d'actions** :
   - Appliquer l'algorithme de **Hierarchical Clustering** sur les séquences d'actions des différents agents. Utiliser la **longueur commune maximale de sous-séquence** comme mesure de similarité entre deux séquences $A_j$ et $A_k$. Cette longueur est définie comme :
     \[
     LCS(A_j, A_k) = \max\{l : A_j[1:l] = A_k[1:l]\}
     \]
   - Les séquences qui ont une similarité supérieure à un seuil $\epsilon$ sont regroupées dans le même cluster.

   2.3 **Identification des rôles abstraits** :
   - Pour chaque cluster, la séquence d'actions commune la plus longue (obtenue via LCS) est utilisée comme représentation abstraite du **rôle de niveau 1**. Cette séquence abstraite, notée $R_1$, représente les comportements stéréotypés des agents dans ce cluster.
   - La variance entre la séquence abstraite $R_1$ et les séquences réelles des agents dans le cluster est calculée pour quantifier l'écart entre le comportement observé et le rôle abstrait. Cela permet de déterminer à quel point les agents se conforment à ce rôle.

   2.4 **Clusterisation récursive des rôles abstraits** :
   - Enregistrer les séquences abstraites obtenues à l'étape précédente et appliquer à nouveau un clustering hiérarchique pour généraliser des rôles de plus haut niveau (niveau 2, etc.). Cela permet d'identifier une hiérarchie de rôles allant des comportements spécifiques à des comportements plus généraux.
   
   - À l'issue de cette étape, on obtient un ensemble de rôles abstraits à plusieurs niveaux de granularité pour chaque historique conjoint $H_i$.

3. **Généralisation des objectifs (missions) basée sur les observations** :

   Pour chaque historique conjoint $H_i$ correspondant à un rôle identifié :

   3.1 **Projection des observations dans un espace 2D** :
   - Appliquer une technique de réduction de dimensionnalité telle que **Principal Component Analysis (PCA)** pour projeter les observations des agents dans un espace 2D. Chaque observation $o_t$ est projetée dans cet espace, formant une trajectoire $O_j = \{o_1, o_2, ..., o_T\}$ pour chaque agent $j$.

   3.2 **Analyse des trajectoires d'observation** :
   - Représenter les trajectoires des agents comme des chemins dans l'espace 2D. Identifier les points où les trajectoires convergent ou sont proches, et détecter les **nœuds d'étranglement** où plusieurs agents suivent des chemins similaires.
   
   3.3 **Détection des sous-objectifs** :
   - Les points de convergence et les nœuds d'étranglement sont interprétés comme des sous-objectifs intermédiaires, qui constituent des étapes critiques pour atteindre l'objectif global. Chaque sous-objectif est représenté par un point ou une région dans l'espace 2D.
   
   3.4 **Échantillonnage des parcours** :
   - Un échantillonnage judicieux des trajectoires permet de déterminer les séquences d'observations clés pour chaque agent, qui correspondent aux sous-objectifs identifiés. Ces sous-objectifs sont ensuite utilisés pour inférer une mission pour chaque rôle abstrait identifié à l'étape 2.

#### Résultats de l'algorithme
- À l'issue de ces étapes, l'algorithme HEMM produit :
   1. **Un ensemble de rôles abstraits** à plusieurs niveaux de granularité, représentant les comportements stéréotypés des agents à partir de leurs séquences d'actions.
   2. **Un ensemble de sous-objectifs** (missions), généralisé à partir des trajectoires d'observations des agents.
   3. **Une métrique d'adéquation organisationnelle**, basée sur la variance entre les rôles abstraits et les comportements observés, ainsi que sur la correspondance entre les sous-objectifs inférés et les actions réalisées.

#### Synthèse

L'algorithme HEMM permet de générer des rôles et des missions implicites à partir de l'observation des actions et des observations des agents dans un environnement multi-agent. En appliquant des techniques d'apprentissage non supervisé, HEMM propose une méthode pour évaluer quantitativement et qualitativement l'adéquation d'une politique conjointe à une organisation structurée, tout en fournissant une métrique d'évaluation robuste pour mesurer cette adéquation.

---

### VI) Cadre d'expérimentation

Nous décrivons ici les scénarios expérimentaux utilisés pour valider nos contributions, en comparant les résultats obtenus par MOISE+MARL et HEMM à ceux des travaux existants.

---

### VII) Résultats

Cette section présente les résultats expérimentaux et montre comment nos contributions améliorent la performance des agents en termes de coordination, sûreté et interprétabilité.

---

### VIII) Discussion et conclusion

Nous concluons en soulignant l'importance de l'adéquation organisationnelle dans les systèmes multi-agents et en proposant des pistes pour de futurs travaux dans ce domaine.



### Annexes

// Draft
Note:

Adéquation organisationnelle:
 - Pourquoi ? Le point de départ de ce concept vient que dans certains environnements les contraintes environnementales font que les agents aboutissent naturellement à une politique conjointe dont l'ensemble des comportements observés peut s'apparenter à une organisation structurée (disposant de rôles) et fonctionnelle (les agents ayant des rôles cherchent à atteindre des sous-objectifs). Cependant, cette ressemblance n'est pas parfaite ou totale car il est toujours possible que certains des agents entrainés choissent des actions qui n'appartiennent pas aux actions habituellement associé au rôle qu'on leur présume. Le concept d'adéquation orga

 - un rôle qui mappe toutes les observations possibles à une seule action va totalement contraindre les comportements des agents. Si tous les agents adhèrent à de tels rôles, alors le niveau d'adéquation organisationnelle est maximum car la variance au sein de chacun des clusters des historiques des agents est très faible (i.e tous les historiques qui se ressemblent suffisament se ressemblent fortement)
 - un rôle qui mappe toutes les observations à au moins une action, laisant plus de marge de manoeuvre aux agents. Par conséquent, deux cas extrèmes sont possible: ou bien les agents générent des actions différentes de façon constante, c'est à dire que les politiques ne convergent pas et donc la variance augmente; ou bien les politiques convergent vers des politiques stables et donc la variance est plus petite. Ainsi, dans ce cas, il y a plus de marge de manoeuvre aux agents car ils doivent aussi apprendre par eux-même quels actions associer aux observations non-connues. Ainsi, dans un cas extrème les agents qui convergent vers des politiques stables ont tendance à générer des historiques regroupables dans des cluster de faible variance. Dans une autre extrème, les agents qui ne convergent pas vers des politiques stables présentent un nombre de cluster supérieur au nombre de rôle prédéfinis avec des variances élevées.
 - un rôle qui mappe une partie des observations à toutes les actions possibles, correspond en fait à aucun rôle car les agents doivent apprendre eux-mêmes à associer une observation à une action.

Ainsi, si les agents ne convergent pas soit en raison de l'environnement et de l'objectif (qui impose des contraintes ou incitations qui guident les agents vers des rôles "naturels"), alors il est toujours possible d'ajouter des spécifications organisationnelles (qui impose des contraintes supplémentaires vers des rôles "artificiels" qui peuvent néanmoins étendre le fonctionnement des rôles "naturels").
Dans le cas où l'on applique des rôles aux agents afin de contraindre les comportements des agents dans l'espoir de les faire converger vers des rôles, les agents doivent optimiser les comportements non-couverts afin d'atteindre l'objectif final. Pour réaliser ce raffinement de la partie restant à optimiser des politiques, il est possible de les orienter dans la bonne direction en les incitant à atteindre des objectifs intermediaires pour les agents qui adoptent le même rôle (qui constituent donc la partie fonctionnelle des agents).