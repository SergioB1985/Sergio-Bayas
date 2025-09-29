informacion_personal = {#diccionario de datos personales con 4 claves
    "nombre": "Sergio Humberto Bayas Paredes",
    "edad": "37 años",
     "ciudad": "Quito",
     "profesion": "Policía"
}
print("PROGRAMA QUE PERMITE MODIFICAR DATOS DEL DICCIONARIO")
print("El Diccionario actual es:")
print(informacion_personal)
print("Se va ha cambiar la ciudad del diccionario que se:",informacion_personal["ciudad"])
ciu = input(print("Ingrese la ciudad que desea cambiar"))
informacion_personal["ciudad"] = ciu
print("Vamos agregar el area deonde trabajas")
area = input(print("Ingrese el area que trabja"))
informacion_personal["area"] = area# agregamos la clave valor del area de la profesión
print("Vamos a comprovar si tienes telefono")
for clave in informacion_personal:
    if clave == "telefono":#Permite verificar si existe la clave telefono
        tel = input(print("Ingrese el número telefonico"))
        informacion_personal["telefono"] = tel
    else:# si no existe le agregamos clave con su valor
        print(f"No esxiste la clave telefono, se va agregar")
        tel = input(print("Ingrese el número telefonico"))
        informacion_personal["telefono"] = tel
    break
print("Vamos a eliminar la edad, ya que dicha información no es necesaria")
del informacion_personal["edad"]# eliminamos la clave valor de laedad
print("------------------------************-------------------------")
print("DICCIONARIO:")
for clave, valor in informacion_personal.items():#permite imprimir el diccionario de mejor manera
    print(f"{clave}: {valor}")
    print("---------------------------")
print("Realizado por: Sergio Bayas")
print("Vuleve pronto")
