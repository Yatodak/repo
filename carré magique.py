# Fonction qui retourne une matrice nulle (n,p)
def matrice_nul(n, p):
    """retourne une matrice nulle de n lignes et p colonnes"""
    mat_nul = []
    for i in range(n):
        ligne = []
        for j in range(p):
            ligne.append(0)
        mat_nul.append(ligne)
    return mat_nul


# fonction permettant la saisie d'une matrice de dimension quelconque n lignes et p colonnes
def mat_saisie(n, p):
    """ Permet de saisir les termes d’une matrice de n lignes et p colonnes, puis la retourne"""
    mat = matrice_nul(n, p)
    print(mat)
    # Appel d’une matrice nulle de même dimension
    # Remplissage de la matrice par les termes de la matrice.
    for i in range(n):
        for j in range(p):
            print("Donnez l'élément", i+1, j+1)
            mat[i][j] = int(input())
            # Affichage de la matrice saisie
            print("La matrice saisie est : ")
            for ligne in range(n):
                print(mat[ligne])
                # renvoi de la matrice saisie
    return mat


def somme_ligne(m1, n, p):
    somme = 0
    ligne = []
    print("Ligne :")
    for i in range(n):
        for j in range(p):
            somme += m1[i][j]
        ligne.append(somme)
        somme = 0
    print(ligne)
    return ligne


def somme_colonne(m1, n, p):
    somme = 0
    colonne = []
    print("colonne :")
    for i in range(p):
        for j in range(n):
            somme += m1[i][j]
        colonne.append(somme)
        somme = 0
    print(colonne)
    return colonne


def somme_diag1(m1, n):
    somme = 0
    print("Diagonale 1 :")
    for i in range(n):
        somme += m1[i][i]
    print(somme)
    return somme


def somme_diag2(m1, n, p):
    somme = 0
    j = 0
    print("Diagonale 2 :")
    for i in range(p-1, -1, -1):
        somme += m1[j][i]
        j += 1
    print(somme)
    return somme


def carre_magique(som_ligne, som_colonne, som_diag1, som_diag2, n, p):
    # On teste si toutes les valeurs sont égales
    if som_ligne == som_colonne and som_ligne[0] == som_diag1 == som_diag2:
        # On crée un tableau qui contient le nombre de case de la matrice, de 1 à x
        test = []
        for i in range(n*p):
            test.append(i+1)
        tableau = []
        # On crée un tableau contenant tout les nombres de la matrices.
        for i in range(n):
            for j in range(p):
                if matrice1[i][j] not in tableau:
                    tableau.append(matrice1[i][j])
        # On range le tableau par ordre croissant
        tableau.sort()
        # On regarde si les valeurs correspondent
        if test == tableau:
            print("Le carré est magique !!")
        else:
            print("le carré n'est pas magique !!")
    else:
        print("le carré n'est pas magique !!")


if __name__ == '__main__':
    # Programme principal
    # Saisie des dimensions de la matrice
    n_lignes = int(input("Entrez le nombre n de lignes de la matrice1 :"))
    p_colonnes = int(input("Entrez le nombre p de colonnes de la matrice1 :"))
    # Saisie des éléments de la matrice en faisant appel à la fonction mat_saisie du programme matrice_saisie
    # On teste si la matrice est une matrice carrée
    if n_lignes == p_colonnes:
        matrice1 = mat_saisie(n_lignes, p_colonnes)
        ligne = somme_ligne(matrice1, n_lignes, p_colonnes)
        colonne = somme_colonne(matrice1, n_lignes, p_colonnes)
        diag1 = somme_diag1(matrice1, n_lignes)
        diag2 = somme_diag2(matrice1, n_lignes, p_colonnes)
        carre_magique(ligne, colonne, diag1, diag2, n_lignes, p_colonnes)
