# -*- coding: utf-8 -*-

game = "on"

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
    carte = open("cartes/facile.txt", "r")
else:
        carte = open("cartes/prison.txt", "r")   
        print("\n"+carte.read())


while game=="on":
    
    print("\n"+carte.read())
    mouvement = input("\n>> ")
    carte = open("cartes/facile.txt", "r")
    
    

