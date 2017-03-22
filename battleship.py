from random import randint

plateau = []

for x in range(0, 5):
    plateau.append(["O"] * 5)

def afficher_plateau(plateau):
    for ligne in plateau:
        print " ".join(ligne)

afficher_plateau(plateau)

def alea_ligne(plateau):
    return randint(0, len(plateau) - 1)

def alea_col(plateau):
    return randint(0, len(plateau[0]) - 1)

bateau_x = alea_ligne(plateau)
bateau_y = alea_col(plateau)
print bateau_x 
print bateau_y 

# A partir d'ici tout le reste doit etre dans votre boucle for !
# N'oubliez pas l'indentation !
for tour in range(0,4):
    tir_x = int(raw_input("Quelle ligne ?"))
    tir_y = int(raw_input("Quelle colonne ?"))

    if tour == 3:
        print "Game Over"
    elif  tir_x == bateau_x and tir_y == bateau_y:
        print "Bravo ! Vous avez eu mon bateau !"
        afficher_plateau(plateau)
    elif tir_x < 0 or tir_x > 4 or tir_y < 0 or tir_y > 4:
        print "Oups ! Vous devez viser l'ocean."
        afficher_plateau(plateau)
    elif(plateau[tir_x][tir_y] == "X"):
        print "Cette case est deja decouverte."
        afficher_plateau(plateau)
    else:
        print "Dommage !"
        plateau[tir_x][tir_y] = "X"
        print tour + 1
        afficher_plateau(plateau) 
