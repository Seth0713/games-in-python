# -*- coding: utf-8 -*-

game = "on"
fichier = []

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

if choix=='1':
    carte = "cartes/facile.txt"
else:
    carte = "cartes/prison.txt" 
    

while game=="on":
    
    active_carte = open(carte, "r")
    f = active_carte.read()
    print (f)
    for i in f:
        fichier.append(i)
   # print (fichier)
    print (fichier[22])
    
    #print("\n"+active_carte.read())
    mouvement = input("\n>> ")
    
    

