def cal_desc (monto_total, desc = 100):
    descuento = (monto_total * desc)/100
    return descuento

print ("UNIVERSIDAD ESTATAL AMAZONICA")
print("Realizado por: Sergio Humberto Bayas Paredes")
print("PROGRAMA QUE CALCULA EL DESCUENTO DE UNA COMPRA")
monto_total = int(input(print("Ingrese el monto total de la compra")))
desc = int (input(print("Ingrese el porcentaje de descuento")))
print (" El monto a ser calculado es: $", cal_desc(monto_total))
print (f"Se aplico el {desc}% de descuento que es $:", cal_desc(monto_total, desc))
print ("El total a pagar es: $", monto_total - cal_desc(monto_total, desc))
print ("Gracias por su compra")
print("Vuelva pronto")