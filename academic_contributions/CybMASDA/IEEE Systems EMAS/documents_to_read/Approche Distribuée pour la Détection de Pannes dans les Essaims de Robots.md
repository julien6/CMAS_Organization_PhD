# Approche Distribuée pour la Détection de Pannes dans les Essaims de Robots

## 1. Introduction
- **Systèmes Robotiques en Essaim (SRS)** : Systèmes multi-robots composés de robots simples.
- Comportements complexes émergent des décisions locales et des communications entre robots.
- Problématique : Malgré leur robustesse, quelques robots défectueux peuvent réduire considérablement les performances du SRS.
- **Proposition** : Une approche de détection de pannes distribuée, utilisant des classificateurs de machine learning pour identifier des robots défectueux.
- L'approche est basée sur des données collectées facilement via des plateformes robotiques en essaim.

## 2. Travaux Connexes
- **SRS** : Systèmes distribués où chaque robot peut coopérer avec d'autres pour accomplir une tâche.
- Malgré leur nature robuste, certains types de pannes peuvent fortement affecter la performance.
- Deux catégories d'approches de détection de pannes : exogènes (détecter les pannes chez les autres) et endogènes (autodiagnostic).
- Les algorithmes de classification des pannes peuvent être quantitatifs ou qualitatifs, utilisant soit des modèles basés sur la connaissance du domaine, soit des méthodes basées sur les données.

## 3. Approche Proposée pour la Détection de Pannes
### 3.1 Vue d'ensemble
- Chaque robot observe ses voisins, traite les mesures collectées, et utilise un algorithme de classification pour déterminer si un robot est défectueux ou non.
- L'algorithme fonctionne en trois phases : 
  1. Observation et traitement des données.
  2. Classification des robots observés.
  3. Vote entre robots pour décider collectivement si un robot est défectueux.

### 3.2 Phase A : Observer et Traiter
- Les robots mesurent la distance et l'angle par rapport à leurs voisins.
- Deux types de caractéristiques sont calculées : binaires et numériques.
  - **Caractéristiques binaires** : Modélisent les actions des moteurs et les interactions entre robots.
  - **Caractéristiques numériques** : Incluent la vitesse des roues et la distance parcourue.

### 3.3 Phase B : Classifier
- Utilisation de méthodes de machine learning (régression logistique ou arbres de décision) pour classifier les robots comme défectueux ou non.
- Les données sont préparées dans des ensembles d'entraînement avant d'être utilisées par les classificateurs.

### 3.4 Phase C : Vote
- Chaque robot partage ses classifications individuelles avec les autres robots.
- Un vote à la majorité permet de déterminer la classification collective (robot défectueux ou non).

## 4. Configuration Expérimentale
- Expérimentation menée dans un simulateur (ARGoS), avec des essaims de 20 robots e-puck équipés de capteurs infrarouges et de capteurs RAB.
- **Comportements testés** :
  1. **Agrégation** : Les robots se rapprochent les uns des autres.
  2. **Dispersion** : Les robots se déplacent de manière aléatoire.
  3. **Flocking** : Les robots se déplacent en formation coordonnée.
  4. **Homing** : Les robots se déplacent vers une balise statique.
- **Types de pannes testées** : Dysfonctionnement des moteurs, erreurs des capteurs de proximité, décalages dans les capteurs RAB.

## 5. Résultats Expérimentaux
### 5.1 Expériences avec un seul robot défectueux
- Comparaison des performances entre trois approches : 
  - **CRM-B** : Basée sur des caractéristiques binaires.
  - **ML-B** : Utilise des caractéristiques binaires avec machine learning.
  - **ML-N** : Utilise des caractéristiques numériques avec machine learning.
- **Résultats** : Les approches ML-B et ML-N surpassent souvent CRM-B en termes de détection des pannes.
- Les caractéristiques numériques (ML-N) sont particulièrement efficaces pour certaines pannes.

### 5.2 Expériences avec plusieurs robots défectueux
- **Résultats** : Les performances de la détection ne sont pas affectées de manière significative par la proportion de robots défectueux dans l'essaim.
- **ML-N** surpasse généralement ML-B dans les scénarios complexes.

## 6. Discussion
- **Avantages** de ML-N : Moins de dépendance à la connaissance du domaine, apprentissage automatique des meilleurs seuils de classification.
- **Inconvénients** : Nécessité de données labellisées pour l'entraînement des modèles.
- Potentiel pour étendre l'approche à la détection de pannes endogènes et exogènes simultanées.

## 7. Conclusion
- L'approche distribuée proposée utilise le machine learning pour classifier les robots défectueux dans un SRS.
- Les caractéristiques numériques offrent une plus grande flexibilité et de meilleures performances que les caractéristiques binaires.
- Des tests supplémentaires dans des environnements réels sont nécessaires pour valider l'approche.
