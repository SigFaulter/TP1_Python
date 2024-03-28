age = int(input("Donner votre age: "))

while True:
    sexe = input("Donner votre sexe (H, F): ").lower()
    if sexe not in ("h", "f"):
        print("Erreur")
    else:
        break

if (sexe == "h" and age > 20) or (sexe == "f" and age >= 18 and age <= 35):
    print("payer l'impot")
else:
    print("pas d'import a payer")