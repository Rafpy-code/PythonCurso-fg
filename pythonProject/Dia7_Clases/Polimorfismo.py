class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice muuuuuuuu')


class Obeja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice beeeeeeee')


vaca1 = Vaca('Lola')
obeja1 = Obeja('Nube')

print('vaca1.hablar() - obeja1.hablar()')
vaca1.hablar()
obeja1.hablar()

print('animales = [vaca1, obeja1]')
animales = [vaca1, obeja1]
for animal in animales:
    animal.hablar()

print('def animal_habla(animal):')


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(obeja1)
