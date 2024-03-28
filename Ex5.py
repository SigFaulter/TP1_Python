def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: division par zéro"
    elif op == '*':
        return num1 * num2
    else:
        return "Opérateur non valide"

def get_input(prompt):
    return float(input(prompt))

num1 = int(input("Entrez le premier nombre: "))
num2 = int(input("Entrez le deuxième nombre: "))
op = input("Entrez l'opérateur (+, -, /, *): ")

result = calc(num1, num2, op)

print("Le résultat est:", result)
