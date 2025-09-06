#FUNCIÓN QUE ORDENA UNA FILA ESPECIFICA DENTRO DE UNA MATRIZ
def bubble_sort(fila_extraida):
    n = len(fila_extraida) # Recorre la lista para asegurar que todos los elementos estén ordenados
    for i in range(n):  # La última i elementos ya están en su lugar
        for j in range(0, n - i - 1):  # Recorre la lista de 0 a n-i-1
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if fila_extraida[j] > fila_extraida[j + 1]:
                fila_extraida[j], fila_extraida[j + 1] = fila_extraida[j + 1], fila_extraida[j] # Intercambio
    return fila_extraida # Retorna la fila o array ordenada


# PROGRAMA
print ("UNIVERSIDAD ESTATAL AMAZONICA")
print("FUNDAMENTOS DE PROGRAMACIÓN")
print("PROGRAMA QUE ORDENA UNA FILA DE FORMA ASCENDENTE DE UNA MATRIZ DE 3X3")
print("MATRIZ DE 3X3")
matriz_org = [
    [10, 5, 0],
    [4, 2, 12],
    [3, 22, 1]
]
matriz_copia = matriz_org
print(matriz_org)
fila = int(input("Tomando en cuanta que las filas va desde el 0, 1, 2, ¿cual fila desea ordenar de forma ascendente?"))
fila_extraida = matriz_copia [fila]
fila_ordenada = bubble_sort (fila_extraida)
matriz_copia[fila] = fila_ordenada
print("Matriz Original:", matriz_org)
print(f"Matriz ordenana:", matriz_copia)
print("REALIZADO POR: SERGIO HUMBERTO BAYAS ")
print("GRACIAS POR USAR MI PROGRAMA VUELVA PRONTO ")


# SERGIO HUMBERTO BAYAS PAREDES