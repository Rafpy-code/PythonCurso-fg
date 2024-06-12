lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

palabra: str = "Python"
lista_indices = list(enumerate(palabra))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)

lista = ['a', 'b', 'c']
for indice, item in enumerate(lista):
    print(indice, item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(f'mis_tuples[1][1] -> {mis_tuples[1][1]}')

for indice, item in enumerate(range(70, 81, 2)):
    print(indice, item)
