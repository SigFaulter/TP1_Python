n = 0
while True:
    n = int(input("Donner un nombre entier superieur a 1: "))
    if n <= 1:
        print("Erreur: nombre pas superieur a 1")
    else:
        break

somme = 0
for i in range(1, n):
    if (n % i == 0):
        somme += i

if somme == n:
    print("Le nombre est parfait")
else:
    print("Le nombre n'est pas parfait")