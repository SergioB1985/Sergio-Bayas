print("PROGRAMA QUE CREA UNA ARCHIVO .TXT")
print("Vamos a ingresar tres lineas de texto")
l1 = input(print(
    "Ingrese la primera linea de texto"))  # permite ingresar desde el teclado linea a linea el texto para el archivo
l2 = input(print("Ingrese la segunda segunda de texto"))
l3 = input(print("Ingrese la tercera linea de texto"))
with open("my_notes.txt", "w") as archivo:  # abre el archivo my_notes.txt
    archivo.write(l1 + "\n")  # permite escribir en el archivo por linea
    archivo.write(l2 + "\n")
    archivo.write(l3 + ".")
    print("las tres lineas de texto fueron guardas con exito en el archivo.txt")
archivo.close()  # cerramos el archivo
print("PRIMERA FORMA DE MOSTRAR O IMPRIMIR LASLINEAS DEL ARCHIVO.TXT")
with open("my_notes.txt", "r") as archivo:  # abrimos el archivo
    for linea in archivo:  # iteramos de linea a linea por el archivo
        print(linea, end='')  # imprimimos cada linea  con un salo
archivo.close()
print("")
print("SEGUNDA FORMA DE MOSTRAR O IMPRIMIR LASLINEAS DEL ARCHIVO.TXT")
with open("my_notes.txt", "r") as archivo:
    todas_lineas = archivo.readlines()  # lee todas las lineas
    print(todas_lineas)
archivo.close()
print("TERCERA FORMA DE MOSTRAR O IMPRIMIR LASLINEAS DEL ARCHIVO.TXT")
with open("my_notes.txt", "r") as archivo:
    lin1 = archivo.readline()  # lee linea a linea
    print(lin1)
    lin2 = archivo.readline()
    print(lin2)
    lin3 = archivo.readline()
    print(lin3)
archivo.close()
print("VULEVE PRONTO")
print("REALIZADO POR: SERGIO BAYAS")
