array = []

for i in range(0, 10):
    n = int(input(f"Saisier le nombre n{i+1}: "))
    array.append(n)

def estTri(table):
    if(table[0] >table[9]):
        print("table non tristris")
        return
    else:
        for i in range(1, 9):
            if table[i] > table[i+1]:
                print("table non tris")
                return
    print('table est tris')


estTri(array)

