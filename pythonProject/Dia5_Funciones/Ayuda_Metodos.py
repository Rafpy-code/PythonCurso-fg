import string
from typing import Tuple, Set


dicc = {'valor1': 432, 'valor2': 537}
print(dicc)
print("a = dicc.popitem()")
a = dicc.popitem()
print(f"a = dicc.popitem() {a}")
print(dicc)

print("\na = \",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#\"\nb = a.strip(' ,: % _# ').replace('%', 'h').replace")
a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
b = a.strip(' ,: % _# ').replace('%', 'h').replace('_', ' ').replace(' ', '', 2)
print(b)

print("\na = ,:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#")
a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(a.lstrip(' ,: % _# '))

print()
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(frutas)
print('frutas.insert(3, "naranja")')
frutas.insert(3, "naranja")
print(frutas)

print()
# Si no se repiten los elementos devuelve True
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei"}
print(marcas_smartphones)
marcas_tv = {"Sony", "Philips", "LG"}
print(marcas_tv)
print("conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)")
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
