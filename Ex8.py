#import cProfile
n = int(input("Donner un nombre n: "))

#def func():
somme = 0
for i in range(0, n + 1):
    somme += 10 ** i

#def func():
#    somme = "1"
#    somme = somme * n
#    return somme

#cProfile.run("func()")

print(somme)