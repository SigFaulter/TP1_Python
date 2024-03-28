from math import sqrt

def delta(a, b, c):
    delta = b**2 - (4 * a * c)
    return delta


def solve(delta, a, b, c):
    if delta < 0:
        print("Pas de solution")
    elif delta == 0:
        calc = - (b / 2 * a)
        print("l'equation admet une seule solution")
        print(f"X = {calc}")
    else:
        root = sqrt(delta)
        calc1 = (- b + root) / 2 * a
        calc2 = (- b - root) / 2 * a

        print("l'equation admet deux solutions")
        print(f"X1 = {calc1}")
        print(f"X2 = {calc2}")

a = float(input("Donner le premier cofficient: "))
b = float(input("Donner le deuxieme cofficient: "))
c = float(input("Donner le troisieme cofficient: "))

delta = delta(a, b, c)
solve(delta, a, b, c)
