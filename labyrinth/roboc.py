# -*- coding: utf-8 -*-

game = "on"
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
    global nb, posMem, nbCol, nbMem
    
    for j in fichier:
        nb+=1
        if j=="X":
            countX=nb-1            
    nb=0        
    posOld=posMem
    fichier[countX]=posOld
    posMem = fichier[countX+nbdep]
    fichier[countX+nbdep]="X"
    print (("").join(fichier))
    
print ("Labyrinthes existants :")
print ("1 - facile.")
print ("2 - prison.")

#check_save = open("cartes/save.txt", "r")
#if check_save is not None:
#    save_ok = input ("\nVous avez une partie en cours, voulez vous la continuer ? (Y or N) : \n>> ") 
#    if save_ok == 'Y':
#        carte = open("cartes/save.txt", "r")
#        print("\n"+carte.read())
#    else:
#       pass
                     
choix = input ("\nEntrez un numéro de labyrinthe pour commencer à jouer : \n>> ")

# Récupération de la carte choisie
if choix=='1':
    carte = "cartes/facile.txt"
elif choix=='2':
    carte = "cartes/prison.txt"
else :
    choix = input ("\nChoix non valide, choisissez la carte 1 ou 2 pour commencer à jouer : \n>> ")

active_carte = open(carte, "r")
f = active_carte.read()

# Création d'un tableau avec les données de la carte   
for i in f:
    fichier.append(i)  
print ("dddddddddddddddddddddddddddddddddddddddd\n")
print (("").join(fichier))


# Routine du jeu    
while game=="on":      
 
    mouvement = input(">> ")

# mouvement

    if mouvement=="d":                   
        Move(+1)         
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
        
