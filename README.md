# Générateur de feuilles d'exercices de mathématiques

Ce projet consiste en un script Python destiné à la génération automatisée de feuilles d'exercices de mathématiques, systématiquement accompagnées de leurs corrigés détaillés.

Initialement développé pour optimiser la préparation de cours particuliers, cet outil permet de créer un nombre illimité de séries d'entraînement uniques. L'architecture de l'outil met l'accent sur la rigueur des notations mathématiques, afin de répondre aux standards d'exigence du lycée et des classes préparatoires aux grandes écoles (CPGE).

## Niveau visé

* **Classe de Première (Spécialité Mathématiques) :** Entraînement standard portant sur les notions fondamentales du programme.
* **Classe de Terminale :** Création de fiches de « calculs réflexes » et de supports de remise à niveau.

## Fonctionnalités principales

* **Équations du second degré :** Génération d'équations admettant des racines entières. Cette approche privilégie l'assimilation de la méthode de résolution et du raisonnement au détriment de la complexité purement arithmétique.
* **Dérivation :** Génération aléatoire de fonctions polynomiales et réalisation du calcul formel de leurs dérivées associées.
* **Rigueur des notations :** Implémentation systématique du formalisme mathématique, incluant l'usage des quantificateurs ($\forall x \in \mathbb{R}$) et la notation ensembliste rigoureuse pour les solutions ($S = \{...\}$).
* **Calcul exact :** Résolution et simplification exactes des expressions mathématiques grâce à l'intégration de la bibliothèque de calcul formel `SymPy`.
* **Exportation LaTeX :** Génération automatisée d'un fichier `.tex` complet, prêt à être compilé au format PDF. Cette fonctionnalité garantit un rendu typographique de qualité professionnelle, similaire aux sujets de concours officiels.

## Prérequis et installation

L'exécution de ce script nécessite un environnement Python fonctionnel ainsi que l'installation de la bibliothèque de calcul formel `SymPy`.

Pour installer les dépendances nécessaires, exécutez la commande suivante dans votre terminal :

```bash
pip install sympy

```
