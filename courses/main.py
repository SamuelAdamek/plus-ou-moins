import random
    
print("Bienvenue, Veuillez choisir votre niveau \nFacile(1) : 0 à 10. \nMoyen(2) : 0 à 100. \nDifficile(3) : 0 à 1000.\n\n")
nbressaie = 0
difficulter = input("Veuillez choisir votre difficulté : ")
while difficulter != "Facile" and difficulter != "Moyen" and difficulter != "Difficile" and difficulter != "1" and difficulter !=  "2" and difficulter != "3":
    print("\nErreur la difficulter n'est pas trouver. \nVeuillez choisir une difficulter valide.\n\n")
    difficulter = input("Veuillez choisir votre difficulté : ")
print("Bon jeu !\n")
numeroutilisateur = 0

if difficulter == "Facile" or difficulter == '1' :
    nombre_a_trouver = random.randint(1, 10)
    while nombre_a_trouver != numeroutilisateur :
        try: 
            numeroutilisateur = int(input("Entrer un nombre : "))
            if nombre_a_trouver < numeroutilisateur :
                print("\nLe nombre a trouver est plus petit\n")
            else :
                print("\nLe nombre a trouver est plus grand\n")
            nbressaie = nbressaie + 1
        except ValueError:
            print("Erreur ! Vous devez entrer un nombre Valide.")

elif difficulter == "Moyen" or difficulter == 2 :
    nombre_a_trouver = random.randint(1, 100)
    while nombre_a_trouver != numeroutilisateur :
        try: 
            numeroutilisateur = int(input("Entrer un nombre : "))
            if nombre_a_trouver < numeroutilisateur :
                print("\nLe nombre a trouver est plus petit\n")
            else :
                print("\nLe nombre a trouver est plus grand\n")
            nbressaie = nbressaie + 1
        except ValueError:
            print("Erreur ! Vous devez entrer un nombre Valide.")

elif difficulter == "Difficile" or difficulter == 3 :
    nombre_a_trouver = random.randint(1, 1000)
    while nombre_a_trouver != usernumber :
        try: 
            usernumber = int(input("Entrer un nombre : "))
            if nombre_a_trouver < usernumber :
                print("\nLe nombre a trouver est plus petit\n")
            else :
                print("\nLe nombre a trouver est plus grand\n")
            nbressaie = nbressaie + 1
        except ValueError:
            print("Erreur ! Vous devez entrer un nombre Valide.")

print (f'Bravo, vous avez trouvez en {nbressaie} essaie ')