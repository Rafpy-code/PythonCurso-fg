class Pajaro:
    def __init__(self, color):
        self.color = color


pajaro1 = Pajaro('Azul')

print(pajaro1)
print(type(pajaro1))

pajaro2 = Pajaro('rojo')

print(f'El pájaro 1 es de color {pajaro1.color}')
print(type(pajaro2))

print(f'El pájaro 2 es de color {pajaro2.color}')

