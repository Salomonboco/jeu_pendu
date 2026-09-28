# 🔤 Jeu du Pendu

Une application Python interactive en ligne de commande pour deviner des mots secrets tout en gérant un profil joueur, un score cumulé et des niveaux de difficulté.

## 🚀 Fonctionnalités

* **Profil joueur :** Saisie et validation du nom (au moins 4 lettres alphabétiques) lors de la première partie.
* **Choix de la difficulté :** Sélection dynamique du dictionnaire de mots au début de chaque manche :
  * **Facile :** Mots courts (4 à 5 lettres)
  * **Moyen :** Mots moyens (6 à 7 lettres)
  * **Difficile :** Mots longs (8 lettres et plus)
* **Calcul dynamique du score :** Attribution de +10 points par victoire, conservés au fil des parties.
* **Re-jouabilité fluide :** Option de relancer une manche directement sans réinitialiser le profil ni le score global.
* **Saisie sécurisée :** Détection et gestion des erreurs (chiffres, symboles ou lettres déjà proposées).

### ⏳ À venir

* **Interface graphique (GUI) :** Migration de la console vers une interface utilisateur visuelle avec Tkinter ou Pygame.
* **Dessin dynamique :** Affichage progressif du bonhomme pendu à chaque erreur.
* **Effets sonores :** Ajout d'effets audio pour les victoires, défaites et saisies de lettres.

## 🛠️ Stack technique

* **Langage :** Python 3.7+
* **Modules standards :** `random` (sélection aléatoire des mots), `string` (gestion de l'alphabet)
* **Structures de données :** `set` (optimisation du suivi des lettres en complexité temporelle $O(1)$)

## 🗺️ Roadmap

- [x] Structure modulaire du jeu et gestion des fonctions principales
- [x] Validation du profil joueur et du pseudo
- [x] Catégorisation des mots en 3 niveaux de difficulté
- [x] Système de score cumulé et re-jouabilité
- [ ] Création d'une interface graphique (GUI avec Tkinter)
- [ ] Sauvegarde locale des meilleurs scores (High Scores)

## 💡 Ce que j'ai appris

* **Modularité du code :** Séparation claire de la logique du jeu (`hangman.py`) et des données (`mots.py`).
* **Optimisation algorithmique :** Emploi des ensembles (`set`) Python pour effectuer des opérations de recherche d'éléments et de différences d'ensembles de manière optimale.
* **Gestion des états :** Suivi des variables globales (score, nom du joueur) à travers plusieurs manches d'exécution.
* **Contrôle et validation des saisies :** Nettoyage des chaînes de caractères (`capitalize()`, `upper()`, `isalpha()`) pour garantir une expérience utilisateur sans crash.

## 🎯 Exécution du projet

1. Clone le dépôt GitHub :
   ```bash
   git clone [https://github.com/salomonboco/jeu-du-pendu.git](https://github.com/salomonboco/jeu-du-pendu.git)
   cd jeu-du-pendu
   

## Licence

MIT
   

[Salomon Boco](https://github.com/salomonboco)