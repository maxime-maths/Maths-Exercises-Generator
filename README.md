# 🧮 Générateur de feuilles d'exercices (Mathématiques)

Un script Python conçu pour générer automatiquement des feuilles d'exercices de mathématiques (et leurs corrigés détaillés). 

J'ai développé cet outil pour m'accompagner dans la préparation de mes cours particuliers. Il permet de créer des séries d'entraînement uniques à l'infini, avec un focus particulier sur la rigueur des notations mathématiques exigées au lycée et en classe préparatoire.

## 🎯 Niveau ciblé
- **Classe de Première (Spécialité Mathématiques) :** Entraînement standard sur le cœur du programme.
- **Classe de Terminale :** Feuille de "calculs réflexes" et remise à niveau.

## 🌟 Fonctionnalités actuelles
- **Équations du second degré :** Génération d'équations avec des racines entières pour privilégier la compréhension de la méthode plutôt que le calcul calculatoire lourd.
- **Dérivation :** Génération de fonctions polynomiales aléatoires et calcul formel de leurs dérivées.
- **Rigueur mathématique :** Utilisation systématique des quantificateurs ($\forall x \in \mathbb{R}$) et des ensembles de solutions ($S = \{...\}$).
- **Résolution exacte :** Les calculs sont effectués de manière exacte grâce à la bibliothèque de calcul formel `SymPy`.
- **Export LaTeX :** Génération d'un fichier `.tex` complet, prêt à être compilé en PDF (idéal pour un rendu professionnel de type "sujet de concours").

## 🛠️ Prérequis et Installation

Vous devez avoir Python installé sur votre machine, ainsi que la bibliothèque `SymPy`.

```bash
# Installer la dépendance SymPy
pip install sympy
