class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

# Métodos de instancia
    def piar(self):
        print('Pio, pio, pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'¿Tengo alas? -> {self.alas}')
        print(f'He volado {metros} metros.')

# Métodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Este pájaro puso {cantidad} huevos.')
        Pajaro.alas = False
        print(f'¿Tengo alas? -> {cls.alas}')

# Métodos estáticos

    @staticmethod
    def mirar():
        print('El pájaro mira su comida.')


piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(45)

Pajaro.poner_huevos(5)
Pajaro.mirar()


class Perro:

    def ladrar(self):
        print('Guau!')


perro = Perro()
perro.ladrar()


class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


a = Alarma()
a.postergar(5)


class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


p = Personaje(10)
p.lanzar_flecha()


