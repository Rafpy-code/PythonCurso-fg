"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones.
"""
porcentaje = 0.13

print("\t***CALCULA TU COMISIÓN***")
nombre = input("¿Cuál es tu nombre? ")
ventas = input("¿Cuáto has vendido este mes? ")
comision = round(float(ventas) * porcentaje, 2)
total = round((float(ventas) + comision), 2)
print(f"{nombre} has vendido {ventas}\nobteniendo una comisión de {comision}, \nasí que "
      f"cobrarás un total de {total}")


