# Notes orales pour la présentation JFSMA 2026

Objectif : support de parole pour une présentation d'environ 25 minutes.
Le texte ci-dessous n'est pas fait pour être lu mot à mot : il donne les points à couvrir et les transitions.

## 0. Titre

**Mots-clés**
- Cadre neuro-symbolique
- Modèles du monde multi-agents
- Fil conducteur : apprendre des modèles prédictifs, mais éviter les mondes impossibles

**Transition**
- Commencer par rappeler ce qu'est un modèle du monde, puis montrer pourquoi le multi-agent rend cette idée plus fragile.

## 1. Les Modèles du Monde : modèles mentaux

**Mots-clés**
- Idée ancienne : représentation interne du monde
- Anticiper les conséquences d'une action
- Prédiction comme ressource pour le contrôle
- Dynamique abstraite : `s_{t+1}=f(s_t,a_t)`

**Transition**
- Une fois l'idée posée, la question devient : peut-on apprendre cette dynamique plutôt que la définir à la main ?

## 2. Les Modèles du Monde : modèles prédictifs appris

**Mots-clés**
- Passage de modèles écrits à modèles appris
- Dynamique approchée `T_\theta`
- Rollouts imaginés pour améliorer la politique
- Gain attendu : frugalité en interactions réelles

**Transition**
- Cette idée devient vraiment puissante quand on ne prédit plus directement les observations brutes, mais un état latent compact.

## 3. Les Modèles du Monde : imagination latente

**Mots-clés**
- Compression observationnelle : encodeur vers `z_t`
- Mémoire récurrente : `\tilde{h}_t`
- Prédiction de l'observation future et de la récompense
- World Models modernes : imagination dans l'espace latent

**Transition**
- A partir de là, le modèle n'est plus seulement prédictif : il devient un support de planification.

## 4. Les Modèles du Monde : planification latente

**Mots-clés**
- PlaNet, Dreamer
- Rollouts multi-pas
- Optimiser une politique dans le modèle appris
- Problème central : les erreurs s'accumulent dans les horizons longs

**Transition**
- Les travaux récents montent encore en échelle, mais cette montée en généralité ne règle pas automatiquement la cohérence.

## 5. Les Modèles du Monde : modèles génériques

**Mots-clés**
- Foundation World Models
- Pré-entraînement massif, vidéo, IA incarnée
- Généralité et adaptation
- Question ouverte : que devient cette approche en multi-agent ?

**Transition**
- Le multi-agent ajoute une couche de difficulté : observations locales, interactions, non-stationnarité.

## 6. Difficultés en multi-agent : l'exemple de Gridcraft

**Mots-clés**
- Observation partielle
- Ambiguïté locale
- Dynamique non stationnaire due aux autres agents
- Erreurs de rollout qui deviennent des violations de structure
- Gridcraft comme cas concret : collecte, craft, coopération, ennemis

**Transition**
- On peut donc situer notre contribution par rapport à trois familles : WMs neuronaux, WMs multi-agents, et WMs neuro-symboliques.

## 7. Vers des modèles du monde multi-agents cohérents

**Mots-clés**
- WMs neuronaux : puissants, mais contraintes implicites
- WMs multi-agents : interactions mieux prises en compte
- Neuro-symbolique : connaissances explicites, mais peu appliqué aux WMs multi-agents
- Position : injecter des lois connues du monde dans le WM

**Transition**
- Avant la méthode, rappeler la base formelle : le Dec-POMDP et l'apprentissage basé modèle.

## 8. Bases : décision partiellement observable

**Mots-clés**
- Dec-POMDP : agents, observations locales, actions conjointes, récompense partagée
- Model-Based Reinforcement Learning : apprendre `T` et `R`
- Simuler des transitions pour réduire les interactions réelles

**Transition**
- On adapte maintenant cette idée au cas multi-agent avec observation et action conjointes.

## 9. Un modèle du monde multi-agent

**Mots-clés**
- Entrée : observation conjointe structurée et action conjointe
- Encodeur, LSTM, MLP de transition, décodeurs
- Prédiction de l'observation suivante et de la récompense
- Le WM reste neuronal à ce stade

**Transition**
- Le problème : un WM neuronal peut apprendre des régularités, mais pas garantir qu'il respecte les règles du monde.

## 10. Hypothèses de travail

**Mots-clés**
- Certaines parties du monde sont déterminables
- On peut les formaliser sous forme de règles partielles
- Trois hypothèses : structure, intégration neuro-symbolique, métrique de cohérence
- Présenter cela comme des hypothèses raisonnables, pas comme des certitudes

**Transition**
- La première étape est donc de structurer l'observation pour distinguer ce qui est déterminable et ce qui ne l'est pas.

## 11. Espace latent d'observation structuré

**Mots-clés**
- Observation comme ensemble de caractéristiques
- Séparation `\omega^d` déterminable et `\omega^u` indéterminable
- Exemples : terrain, collision, inventaire, agents visibles
- Intérêt : cibler précisément ce que les règles peuvent contraindre

**Transition**
- Une fois les caractéristiques identifiées, on peut définir des règles de transition partielles.

## 12. Règle de transition symbolique partielle

**Mots-clés**
- PSTR : règle qui ne prédit qu'une partie de la transition
- Masque de déterminabilité
- La règle ne remplace pas tout le modèle
- Elle impose seulement ce qui est connu

**Transition**
- Ces règles peuvent ensuite être intégrées au WM de plusieurs façons.

## 13. Stratégies d'intégration neuro-symbolique

**Mots-clés**
- Régularisation : ajouter une loss symbolique
- Projection : corriger la sortie à l'inférence
- Résiduel : prédire neuronalement seulement la partie non déterminable
- Trois compromis : souplesse, garantie, factorisation

**Transition**
- Pour évaluer ces stratégies, il faut mesurer non seulement l'erreur numérique, mais aussi les violations de règles.

## 14. Taux de violation des règles

**Mots-clés**
- RVR : Rule Violation Rate
- Comparer la prédiction brute et la prédiction corrigée
- RVR par règle = signature de couverture
- RVR global utile, mais insuffisant seul

**Transition**
- Après le cadre méthodologique, présenter l'implémentation et le protocole expérimental.

## 15. Configuration logicielle et matérielle

**Mots-clés**
- Implémentation PyTorch
- Entraînement WM, stratégies NS-MAWM, environnement Gridcraft
- Matériel : NVIDIA DGX Spark
- Message : expérience reproductible à échelle laboratoire, pas uniquement très grand calcul

**Transition**
- Les expériences ne portent pas seulement sur Gridcraft : il faut situer les environnements et les règles.

## 16. Environnements et ensembles de règles

**Mots-clés**
- Gridcraft, Overcooked, MPE, SMACv2
- Gridcraft comme environnement détaillé
- Ensembles de règles selon les domaines
- Même logique : règles partielles sur transitions déterminables

**Transition**
- Décrire maintenant les métriques qui permettent de comparer les baselines.

## 17. Cadre d'évaluation

**Mots-clés**
- MSE horizon 25
- RVR pré et post
- Récompense en aval
- Ressources de calcul
- Comparer toutes les baselines selon les trois gaps

**Transition**
- Avant les résultats numériques, montrer visuellement ce que sont les PSTR dans Gridcraft.

## 18. Autres exemples de PSTR dans Gridcraft

**Mots-clés**
- Harvest, pickup, mémoire partagée
- Une PSTR décrit une mécanique locale
- La règle est partielle : elle ne prétend pas prédire tout l'état
- Insister sur pickup : item adjacent, pas superposé à l'agent

**Transition**
- Certaines règles sont individuelles, d'autres sont conjointes et portent sur la mémoire partagée.

## 19. Autres exemples de PSTR dans Gridcraft (suite)

**Mots-clés**
- Fusion de carte
- Collision multi-agent
- Mise à jour monde partagé
- Couverture neuro-symbolique = ensemble de règles activées

**Transition**
- On peut maintenant passer aux résultats : d'abord une synthèse des huit baselines.

## 20. Résultats : synthèse des 8 baselines

**Mots-clés**
- Baseline model-free
- WM neuronal pur
- Régularisation, projection, résiduel
- Couverture légère `k=0.3` et étendue `k=0.6`
- QR code pour consulter le rapport complet

**Transition**
- La table donne la vue globale ; la slide suivante montre qualitativement le comportement dans Gridcraft.

## 21. Résultats visuels

**Mots-clés**
- Rollout Gridcraft avec projection
- Horizon 25
- Visualiser que le WM sert à simuler une trajectoire
- La cohérence visuelle reste importante pour interpréter les métriques

**Transition**
- On analyse ensuite les résultats par gap, en commençant par l'apprentissage en aval.

## 22. G1 : apprentissage en aval

**Mots-clés**
- Récompense réelle
- Sans WM, WM pur, variantes NS-MAWM
- NS-MAWM légèrement au-dessus du WM pur
- Le model-free reste fort dans cette configuration

**Transition**
- Pour comprendre cette récompense, il faut regarder aussi la fidélité prédictive du WM.

## 23. G1 : fidélité du WM et récompense en aval

**Mots-clés**
- MSE horizon 25
- Récompense en aval
- WM pur compétitif
- NS-MAWM améliore légèrement la fidélité et la récompense
- Gain modéré, mais cohérent avec l'hypothèse G1

**Transition**
- Le deuxième gap porte sur la stratégie d'intégration neuro-symbolique et la couverture des règles.

## 24. G2 : apprentissage du WM

**Mots-clés**
- Loss WM brute
- Régularisation au-dessus du WM pur : coût d'ajustement symbolique
- `k=0.6` au-dessus de `k=0.3` : plus de règles, plus de contraintes
- Projection/résiduel restent proches des autres courbes

**Transition**
- La loss seule ne dit pas tout : il faut regarder comment la stratégie et le niveau de couverture influencent les autres métriques.

## 25. G2 : effet de la stratégie et de la couverture `k`

**Mots-clés**
- `k=0.3` : couverture légère
- `k=0.6` : couverture étendue
- La couverture aide surtout quand la stratégie l'exploite bien
- Résiduel plus contraignant quand trop de règles sont imposées

**Transition**
- Le troisième gap concerne la cohérence symbolique : est-ce que les règles sont effectivement respectées ?

## 26. G3 : cohérence neuro-symbolique

**Mots-clés**
- RVR pré : violations avant correction
- WM pur hors comparaison directe si aucune PSTR activée
- Projection et résiduel : RVR post nul
- Régularisation réduit mais ne garantit pas

**Transition**
- Pour être précis, distinguer pré-correction et post-correction.

## 27. G3 : cohérence symbolique pré/post correction

**Mots-clés**
- Barres pré/post
- Projection/résiduel imposent la cohérence sur `\mathcal{F}^d`
- Régularisation reste souple
- Important : garantie limitée aux champs couverts

**Transition**
- Le RVR global est utile, mais la vraie lecture se fait règle par règle.

## 28. G3 : signature de couverture par PSTR

**Mots-clés**
- Colonnes = familles de règles
- Chaque PSTR donne une signature de violation
- Identifier les règles difficiles ou rares
- Diagnostic plus informatif que le seul RVR global

**Transition**
- Après les trois gaps, synthétiser les messages principaux et les ablations.

## 29. Bilan des résultats

**Mots-clés**
- G1 : gain modéré mais cohérent du WM neuro-symbolique
- G2 : effet de `k` dépend de la stratégie
- G3 : projection/résiduel donnent une garantie post-correction
- Loss seule insuffisante : croiser MSE, RVR, reward

**Transition**
- Dernier point expérimental : le coût de calcul, car les méthodes neuro-symboliques ne sont utiles que si elles restent entraînables.

## 30. Ressources de calcul : utilisation GPU

**Mots-clés**
- Utilisation GPU par baseline
- Model-free moins coûteux GPU
- Régularisation plus soutenue
- Projection/résiduel plus irréguliers
- Interprétation : coût réel des contraintes, pas seulement performance

**Transition**
- On peut maintenant conclure : rappeler les contributions, les résultats, puis les limites.

## 31. Conclusion

**Mots-clés**
- Contributions : représentation structurée, PSTR, trois stratégies, RVR
- Résultats : amélioration légère du WM pur, RVR post nul pour projection/résiduel
- Limites : règles manuelles, coût, couverture partielle
- Perspectives : extraction automatique, compilation/vectorisation, planification

**Transition**
- Remercier, puis inviter aux questions sur le rapport et le code.

## 32. Merci / QR codes

**Mots-clés**
- QR rapport complet
- QR code source et données
- Inviter aux questions

**Transition**
- Si question sur les chiffres : revenir au rapport.
- Si question sur la méthode : revenir aux PSTR et aux stratégies.
- Si question sur limites : insister sur couverture partielle et règles manuelles.

## Références

**Mots-clés**
- Slides annexes, pas à présenter dans les 25 minutes.
- Les garder disponibles pour questions bibliographiques.

## Fil narratif court

1. Les WMs sont une idée ancienne : anticiper pour agir.
2. Les WMs modernes apprennent cette anticipation dans un espace latent.
3. En multi-agent, les rollouts peuvent devenir sémantiquement incohérents.
4. NS-MAWM injecte des règles partielles sur les parties déterminables.
5. Trois stratégies : régularisation, projection, résiduel.
6. L'évaluation doit croiser fidélité, cohérence et contrôle en aval.
7. Les résultats montrent des gains modérés mais cohérents, avec une garantie forte de RVR post pour projection/résiduel.

## Répartition temporelle indicative

- Introduction et histoire des WMs : 5 min
- Problème multi-agent et état de l'art : 4 min
- Bases et méthode NS-MAWM : 7 min
- Expérimentations et PSTR Gridcraft : 3 min
- Résultats : 5 min
- Conclusion : 1 min
