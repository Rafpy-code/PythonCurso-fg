from typing import Dict, List

diccionario = {'valor1': 4, 'valor2': "carro"}
print(diccionario)
print(type(diccionario))

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 200, 's2': {'a': "uno", 'b': "dos", 'c': "tres"}, 's3': 600}}
print(f"Claves: {dic.keys()}")
print(f"Valores: {dic.values()}")
print("dic.items() devuelve en tuplas el contenido del diccionario")
print(f"Diccionario: {dic.items()}")
print("dic['c2']")
print(dic['c2'])
print("dic['c2'][1]")
print(dic['c2'][1])
print("dic['c3']")
print(dic['c3'])
print("dic['c3']['s2']")
print(dic['c3']['s2'])
print("dic['c3']['s2']['b']")
print(dic['c3']['s2']['b'])

# nombre: Karen
# apellido: Jurgens
# edad: 35
# ocupacion: Periodista
mi_dic = {'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 35, 'ocupacion': 'Periodista'}
print(mi_dic)

mi_dict: dict[str, dict[str, list[int] | int] | dict[str, int]] = {"valores_1": {"v1": 3, "v2": 6},
                                                                   "puntos": {"points1": 9, "points2": [10, 300, 15]}}
print(mi_dict['puntos']['points2'][1])

mi_dic: dict[str, str | int] = {"nombre": "Karen", "apellido": "Jurgens", "edad": 35, "ocupacion": "Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Ecuador'
print(mi_dic)
