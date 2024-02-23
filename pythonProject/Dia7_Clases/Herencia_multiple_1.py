class Padre:
    def hablar(self):
        print('Hola, desde clase Padre')


class Madre:
    def reir(self):
        print('jajaja')
    def hablar(self):
        print('Hola, desde clase Madre')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)
