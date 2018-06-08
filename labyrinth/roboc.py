print ("Labyrinthes existants :")
print ("1 - facile.")
print ("2 - prison.")

choix = input ("\nEntrez un numéro de labyrinthe pour commencer à jouer : ")

if choix=='1':
    carte = open("cartes/facile.txt", "r")
    print("\n"+carte.read())
else:
    carte = open("cartes/prison.txt", "r")   
    print("\n"+carte.read())

mouvement = input("\n>> ")
    
