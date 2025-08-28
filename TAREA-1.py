#FUNCIÓN QUE BUSCA UN DATO DENTRO DE UNA MATRIZ
def buscar_dato_matriz (matriz, n):
    for fila_inx, fila in enumerate(matriz):  # Recore sobre cada fila
        for col_idx, elemento in enumerate(fila):  # Recore sobre cada elemento de la fila
            if elemento == n:  # Compara el elemento con el dato buscado
                return (fila_inx, col_idx) # devuelve la fila y columna donde encontro el dato


# PROGRAMA
print ("UNIVERSIDAD ESTATAL AMAZONICA")
print("FUNDAMENTOS DE PROGRAMACIÓN")
print("PROGRAMA QUE BUSCA UN DATO DENTRO DE UNA MATRIZ DE 3X3")
print("MATRIZ DE 3X3")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
n = int(input("Que dato desea buscar: "))
posicion = buscar_dato_matriz(matriz, n)
if posicion:
    print(f"El datos {n} se encontro en la posición: {posicion}")
else:
    print(f"El dato {n} no se encontro en la matriz")
print("REALIZADO POR: SERGIO HUMBERTO BAYAS ")
print("GRACIAS POR USAR MI PROGRAMA VUELVA PRONTO ")