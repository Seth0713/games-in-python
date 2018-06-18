# -*- coding: utf-8 -*-

game = "on"
fichier = []
countX = 0
nb = 0
posOld=" "
posMem=" "

def Move(nbdep):
    global posMem
    posOld=posMem
    fichier[countX]=posOld
    posMem = fichier[countX+nbdep]
    fichier[countX+nbdep]="X"
    

print ("Labyrinthes existants :")
print ("1 - facile.")
print ("2 - prison.")

check_save = open("cartes/save.txt", "r")
if check_save is not None:
    save_ok = input ("\nVous avez une partie en cours, voulez vous la continuer ? (Y or N) :") 
    if save_ok == 'Y':
        carte = open("cartes/save.txt", "r")
        print("\n"+carte.read())
    else:
       pass
                     
choix = input ("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")

# Récupération de la carte choisie
if choix=='1':
    carte = "cartes/facile.txt"
else:
    carte = "cartes/prison.txt"

active_carte = open(carte, "r")

f = active_carte.read()

# Création d'un tableau avec les données de la carte   
for i in f:
    fichier.append(i)
    
print (("").join(fichier))

# Routine du jeu    
while game=="on":      
 
    mouvement = input("\n>> ")

# mouvement

    if mouvement=="d":
        print ("aller à droite")

        for j in fichier:
            nb+=1
            if j=="X":
                countX=nb-1
        nb=0
        
        print (countX)
        Move(+1)        

        #posOld=posMem
        #fichier[countX]=posOld
        #posMem=fichier[countX+1]
        #fichier[countX+1]="X"
       
        print (("").join(fichier))
        
# mouvement à gauche
        
    elif mouvement=="g":
        print ("aller à gauche")
        
