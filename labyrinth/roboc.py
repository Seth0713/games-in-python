# -*- coding: utf-8 -*-

game = ""
fichier = []
countX = 0
nb = 0
posOld=" "
posMem=" "
nbCol = 0
nbMem = 0
fLine = True

def nbLine():
    global nbCol, nbMem
    for k in fichier:
        global fLine
        nbCol+=1
        if k=="\n" and fLine==True:           
           
           nbMem = nbCol
           fLine=False

def Move(nbdep):
    global nb, posMem, nbCol, nbMem, countX, game
    
    for j in fichier:
        nb+=1
        if j=="X":
            countX=nb-1            
    nb=0        
    posOld=posMem
    fichier[countX]=posOld
    posMem = fichier[countX+nbdep]

    print ("posMem",posMem)
    print("countX",countX)
    print("posOld",posOld)
    if posMem!="O":
        fichier[countX+nbdep]="X"
        print (("").join(fichier))
    if posMem=="U":
        fichier[countX+nbdep]="X"
        print (("").join(fichier))
        print ("BRAVO !!!!")
        game="off"
        print (game)
    
    
print ("\nLABYRINTHES EXISTANTS :")
print ("1 - facile.")
print ("2 - prison.")

check_save = open("cartes/save.txt", "r")


if check_save.read() != "":
    
    print (check_save.read())
    save_ok = input ("\nVous avez une partie en cours, voulez vous la continuer ? (Y or N) : \n>> ")

#else:
   # choix = input ("\nEntrez un numéro de labyrinthe pour commencer à jouer : \n>> ")

if save_ok == 'Y':
    carte = "cartes/save.txt"
    titre = "PARTI SAUVEGARDE"
else:
    choix = input ("\nEntrez un numéro de labyrinthe pour commencer à jouer : \n>> ")

    # Récupération de la carte choisie
    if choix=='1':
        carte = "cartes/facile.txt"
        titre = "LABYRINTHES N°1 - FACILE"
        game="on"
        
    elif choix=='2':
        carte = "cartes/prison.txt"
        titre = "LABYRINTHES N°2 - PRISON"
        
    else :
        choix = input ("\nChoix non valide, choisissez la carte 1 ou 2 pour commencer à jouer : \n>> ")


active_carte = open(carte, "r")
f = active_carte.read()



# Création d'un tableau avec les données de la carte   
for i in f:
    fichier.append(i)  
print (titre,"\n\nBut du jeu : Déplacez X sur l'emplacement U\n")
print ("Pour vous déplacer utilisez les commandes suivantes :\ng=gauche, d= droite, h=haut, b=bas, q=quitter\n")
print (("").join(fichier))

# Routine du jeu    

while game=="on":      
 
    mouvement = input(">> ")

# mouvement

    if mouvement=="d":                   
        Move(+1)
        print (game)
    elif mouvement=="g":
        Move(-1)
    elif mouvement=="h":
        nbLine()
        Move(-nbMem)        
    elif mouvement=="b":
        nbLine()
        Move(+nbMem)
    else:
        print ("\nUtilisez une commance autorisée : g, d, h, b, q")
        
