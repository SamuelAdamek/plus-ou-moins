print("Bienvenue, Veuillez choisir un chiffre.\n\n")
chiffrechoisi = int(input("Veuillez choisir un chiffre compris entre 1 et 9 : "))
while chiffrechoisi < 1 or chiffrechoisi > 9:
    print("\nErreur le chiffre donner est incorrect. \n\n")
    chiffrechoisi = int(input("Veuillez choisir un chiffre entre 1 et 9 : \n"))
tableau = []

for compteur in range(11) :
    tableau.append(chiffrechoisi * compteur) 
    
    if tableau[compteur] % 3 == 0 :
        tableau[compteur] = str(tableau[compteur]) + '*'

print(f'Tableau  : {tableau}\n')