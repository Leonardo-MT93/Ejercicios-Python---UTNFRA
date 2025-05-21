""" matriz = [[77, 86, 12, 32],
         [45, 23, 56, 78],
            [12, 34, 56, 78],
            ]

for i in range(len(matriz)):
    print(matriz[i])



 Modificar un valor de la matriz
matriz[1][2] = 66
print(matriz)
 """

matriz_prod = [
    ["Martillo", 23, 5000],
    ["Motosierra", 3, 10000],
    ["Rotomartillo", 5, 50000],
]

for i in range(len(matriz_prod)):
    for j in range(len(matriz_prod[i])):
        if matriz_prod[i][j] == "Motosierra":
            print("El precio de la motosierra es: ", matriz_prod[i][j + 2])
