num = 0
while True:
    num = int(input("donner un nombre entier non nul: "))
    if num != 0:
        break
    else:
        print("Erreur: nombre est nul")

somme = 0
for i in range(1, num + 1):
    somme += i ** 2

print(f"le resultat est: {somme}")