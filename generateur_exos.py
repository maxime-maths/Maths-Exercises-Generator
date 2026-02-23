import random
import sympy as sp

def generer_equation_second_degre():
    """Génère une équation du second degré avec des racines entières pour que ce soit 'sympa'."""
    x = sp.Symbol('x')
    # On choisit deux racines aléatoires entre -5 et 5
    r1 = random.randint(-5, 5)
    r2 = random.randint(-5, 5)
    
    # On construit l'expression (x - r1)(x - r2) et on la développe
    expression = sp.expand((x - r1) * (x - r2))
    
    # On crée l'équation expr = 0
    equation = sp.Eq(expression, 0)
    
    # SymPy résout l'équation
    solutions = sp.solve(equation, x)
    
    # --- LA CORRECTION EST ICI ---
    # On convertit chaque solution en LaTeX séparément, et on les joint avec ", "
    sol_latex = ", ".join([sp.latex(s) for s in solutions])
    
    return sp.latex(equation), sol_latex

def generer_derivee():
    """Génère une fonction polynôme et calcule sa dérivée."""
    x = sp.Symbol('x')
    # On génère un polynôme du type ax^3 + bx^2 + cx + d
    a, b, c, d = [random.randint(-5, 5) for _ in range(4)]
    fonction = a*x**3 + b*x**2 + c*x + d
    
    # SymPy calcule la dérivée par rapport à x !
    derivee = sp.diff(fonction, x)
    
    # On renvoie la fonction et sa dérivée au format LaTeX
    return sp.latex(fonction), sp.latex(derivee)

def creer_feuille_exercices(nb_exos):
    """Génère un fichier Markdown contenant les exercices et les corrigés."""
    nom_fichier = "Feuille_Exercices.md"
    
    enonces = []
    corriges = []
    
    # Génération des équations du second degré
    enonces.append("### Exercice 1 : Résoudre les équations suivantes dans $\\mathbb{R}$ \n")
    corriges.append("### Corrigé Exercice 1 \n")
    for i in range(1, nb_exos + 1):
        eq_latex, sol_latex = generer_equation_second_degre()
        enonces.append(f"{i}) $\\quad {eq_latex}$ \n")
        # On garde la formulation ensembliste très propre pour la solution
        corriges.append(f"{i}) L'ensemble des solutions est : $\\quad S = \\{{{sol_latex}\\}}$ \n")
        
    # Génération des calculs de dérivées
    enonces.append("\n### Exercice 2 : Dériver les fonctions suivantes (définies et dérivables sur $\\mathbb{R}$) \n")
    corriges.append("\n### Corrigé Exercice 2 \n")
    for i in range(1, nb_exos + 1):
        f_latex, df_latex = generer_derivee()
        # AJOUT DU FORALL X IN R ICI
        enonces.append(f"{i}) $\\quad \\forall x \\in \\mathbb{{R}}, \\quad f(x) = {f_latex}$ \n")
        corriges.append(f"{i}) $\\quad \\forall x \\in \\mathbb{{R}}, \\quad f'(x) = {df_latex}$ \n")
        
    # Écriture dans le fichier
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write("# 📝 Feuille d'entraînement - Mathématiques\n\n")
        fichier.writelines(enonces)
        fichier.write("\n---\n\n# Corrigés\n\n")
        fichier.writelines(corriges)
        
    print(f"🎉 Le fichier '{nom_fichier}' a été généré avec succès !")

# Lancement du programme
if __name__ == "__main__":
    creer_feuille_exercices(nb_exos=4)