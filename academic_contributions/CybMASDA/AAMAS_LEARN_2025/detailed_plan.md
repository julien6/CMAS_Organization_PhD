### I) Introduction

**Contexte**

Le MARL peut être considéré comme une approche permettant de résoudre le problème de trouver une politique conjointe qui guide les agents vers l'atteinte d'un objectif donné dans un environnement spécifique.

Cette politique conjointe ne définit pas seulement les actions individuelles des agents, mais régit également leurs interactions entre eux, voire avec l'ensemble des autres agents, sans préconception d'un ordre ou d'une structure organisationnelle.

Toutefois, dans certains environnements, les contraintes imposées font que de nombreuses solutions optimales ou satisfaisantes conduisent à des comportements qui ressemblent à une organisation structurée et fonctionnelle, comparable à celle des organisations humaines.

Une idée intuitive est que cette ressemblance entre la politique et une organisation structurée n'est qu'une interprétation inspirée des sociétés humaines. Cela revient à associer les comportements des agents entraînés à des rôles, où chaque rôle délimite les actions possibles des agents et semble répondre à des objectifs précis, contribuant ainsi à maximiser la récompense dans l'atteinte de l'objectif final.

De manière plus générale, on peut interpréter les comportements des agents entraînés comme appartenant à un continuum allant d'un collectif d'agents déstructurés et non fonctionalisés à une organisation pleinement structurée et fonctionnelle. Cette ressemblance naturelle entre la politique conjointe avec une organisation structurée et fonctionnelle est fondamentalement influencée par les contraintes environnementales et les objectifs fixés.

Au-delà des contraintes environnementales et des objectifs initiaux, l'ajout de contraintes spécifiques peut encourager ou forcer les agents à adopter une organisation plus structurée et fonctionnelle, définie par l'utilisateur. Cela peut par exemple se faire en reprenant et affinant la structure et fonction de l'organisation émergente de la politique conjointe.

Nous appelons cette similitude entre la politique conjointe et une organisation structurée et fonctionnelle "adéquation organisationnelle".

**Problème**

Ce papier vise à explorer deux problèmes centraux liés à l'adéquation organisationnelle dans les systèmes multi-agents.

1. **Évaluation de l'adéquation organisationnelle** : Ce problème consiste à évaluer dans quelle mesure une politique conjointe peut être rapprochée d'une organisation structurée et fonctionnelle. Un des enjeux de ce problème est de mieux comprendre les cas où les agents peuvent être considérés comme formant une organisation structurée et fonctionnelle compte tenu des contraintes imposées par l'environnement, l'objectif et d'autres contraintes optionnelles.

    La littérature aborde l'évaluation des politiques en termes de rôles (structure) ou d'objectifs (fonction). Cependant, ces travaux manquent souvent d'une approche systématique et générale. Les méthodes actuelles offrent peu d'outils clairs pour mesurer de manière quantitative et qualitative cette adéquation organisationnelle.

2. **Contrôle de l'adéquation organisationnelle** : Ce problème consiste à guider les agents vers des politiques qui se conforment à une organisation structurée, définie par des contraintes spécifiques prédéfinies par l'utilisateur. L'objectif est de contraindre ou d'inciter les agents à adopter des comportements qui respectent des rôles et des missions, ce qui permet de contrôler leurs actions dans un cadre organisationnel. Les enjeux incluent la réduction de l'espace de recherche des politiques, l'amélioration de la convergence, et la garantie du respect des contraintes de sûreté.

   Les travaux existants dans ce domaine sont limités, notamment en ce qui concerne la manière dont l'utilisateur peut interagir avec les spécifications organisationnelles de manière pratique et flexible.

**Contribution**

Pour répondre à ces deux problèmes, nous proposons deux contributions majeures :

1. **MOISE+MARL Framework (MM)** : Nous introduisons un nouveau framework de MARL qui intègre le modèle organisationnel MOISE+ dans l'apprentissage multi-agent. Ce framework permet de formaliser et de contraindre les politiques des agents en utilisant les concepts de rôles et de missions issus du modèle MOISE+. Les spécifications organisationnelles peuvent être appliquées manuellement aux agents sous forme de contraintes, affectant automatiquement à la fois leurs politiques et la fonction de récompense. Ce framework introduit également des structures de données spécifiques telles que des patterns de comportement et des arbres de décision basé sur les patterns de comportements pour permettre à l'utilisateur de définir des rôles et des objectifs.

2. **History-based Evaluation in MOISE+MARL (HEMM)** : Nous proposons un algorithme permettant d'évaluer automatiquement l'adéquation organisationnelle des politiques apprises. Cet algorithme utilise des techniques d'apprentissage non supervisé pour généraliser des rôles et des missions à partir des comportements observés dans les politiques conjointes. En mesurant l'écart entre les spécifications organisationnelles inférées et les comportements réels, nous définissons une nouvelle métrique multi-dimensionnelle, le **niveau d'adéquation organisationnelle**, qui quantifie dans quelle mesure une politique respecte les spécifications organisationnelles.

**Structure du papier**

La suite du papier est organisée comme suit :
- **Section II** : Présentation du problème du contrôle de l'adéquation organisationnelle et des travaux existants dans ce domaine.
- **Section III** : Description détaillée du framework MOISE+MARL et justification des choix de conception.
- **Section IV** : Discussion du problème de l'évaluation de l'adéquation organisationnelle et analyse des travaux existants.
- **Section V** : Introduction de l'algorithme HEMM et démonstration de son application à l'évaluation de l'adéquation organisationnelle.
- **Section VI** : Description du cadre expérimental utilisé pour évaluer les contributions proposées.
- **Section VII** : Présentation des résultats expérimentaux.
- **Section VIII** : Discussion et conclusion sur l'évaluation et le contrôle de l'adéquation organisationnelle par les contributions proposées.

---

### II) Problème du contrôle de l'adéquation organisationnelle

Dans cette section, nous abordons le problème de guider les agents multi-agents vers des politiques respectant des spécifications organisationnelles. Les principaux défis incluent la formalisation de rôles et de missions adaptés, ainsi que la garantie que les politiques apprises soient sûres, interprétables et efficaces.

---

### III) Framework MOISE+MARL

Le framework MOISE+MARL permet d'étendre les concepts d'organisation dans le cadre de l'apprentissage multi-agent. Il repose sur l'intégration des rôles et des missions comme contraintes supplémentaires pour les agents, influençant à la fois leurs actions et la manière dont ils perçoivent les récompenses.

---

### IV) Problème de l'évaluation de l'adéquation organisationnelle

L'évaluation de l'adéquation organisationnelle consiste à déterminer si les politiques apprises par les agents peuvent être interprétées comme une organisation structurée. Cette section présente les approches et les défis actuels dans ce domaine.

---

### V) Algorithme HEMM

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

### Synthèse

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
