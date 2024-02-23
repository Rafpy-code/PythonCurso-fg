print("if-elif-else")
serie = 'n-01'

if serie == 'n-01':
    print('Nokia')
elif serie == 'n-02':
    print('Motorola')
elif serie == 'n-03':
    print('Huawei')
else:
    print('No existe el producto')

print("\nmatch")
serie1 = 'n-03'
match serie1:
    case 'n-01':
        print('Nokia')
    case 'n-02':
        print('Motorola')
    case 'n-03':
        print('Huawei')
    case _:
        print('No existe el producto')

# Diccionario
cliente = {
    'nombre': 'Ramón',
    'edad': 49,
    'ocupación': 'aprendiz'
}
pelicula = {
    'titulo': 'Miénteme',
    'ficha_técnica': {
        'protagonista': 'Riahu',
        'director': 'Camrty'
    }
}

# Lista usando los diccionarios
elementos = [cliente, pelicula, 'libro']
print(f"Voy a analizar los elementos {elementos}")

for elemento in elementos:
    match elemento:
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupación': ocupacion
        }:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {
            'titulo': titulo,
            'ficha_técnica': {
                'protagonista': protagonista,
                'director': director
            }
        }:
            print("Es una película")
            print(titulo, protagonista, director)
        case _:
            print()
            print(f"Elemento => '{elemento}' Este elemento no es un cliente ni una película :(")
