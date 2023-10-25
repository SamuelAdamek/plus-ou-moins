import random

print("Bienvenue, Veuillez choisir votre niveau \nFacile : 0 à 10. \nMoyen : 0 à 100. \nDifficile : 0 à 1000.\n\n")

difficulter = input("Veuillez choisir votre difficulté : ")
while difficulter != "Facile" and difficulter != "Moyen" and difficulter != "Difficile":
    print("\nErreur la difficulter n'est pas trouver. \nVeuillez choisir une difficulter valide.\n\n")
    difficulter = input("Veuillez choisir votre difficulté : ")
print("Bon jeu !\n")
if difficulter == "Facile" :
    nombre_a_trouver = random.randint(1, 10)
    usernumber = input("Entrer un nombre : ")
    while usernumber < 0 and usernumber > 11 :
        print("\nErreur, Veuillez entrer un nombre valide.\n")






nombre_a_trouver = random.randint(1, 100)
usernumber = input("Entrer un nombre : ")