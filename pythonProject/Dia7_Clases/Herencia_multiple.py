class Animal:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


"""
# Atributos propios de animal altura_vuelo
    def __init__(self, nombre, color, edad, altura_vuelo):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.altura_vuelo = altura_vuelo
"""


class Pajaro(Animal):

    def __init__(self, nombre, color, edad, altura_vuelo):
        super().__init__(nombre, color, edad)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio, pio, pio.')

    def volar(self, metros):
        print(f'Este pájaro voló {metros} metros de distancia.')


piolin = Pajaro('Piolin', 'amarillo', 1, 3570)

piolin.nacer()
piolin.hablar()
piolin.volar(56)

print()

# Al heredar de Animal, este no tiene el método volar.
gato = Animal('Gatito', 'gris', 5)
gato.nacer()
gato.hablar()
