num = int(input("Donner un nombre entier: "))

limit = num + 10
print("En utilisant boucle for: ")
for i in range(num + 1, limit + 1):
    print(i)
    
print("En utilisant boucle while: ")
while num < limit:
    num += 1
    print(num)
