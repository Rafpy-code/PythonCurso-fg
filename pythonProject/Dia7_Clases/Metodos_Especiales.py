class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor} contiene {self.canciones} canciones'

    def __len__(self):
        # return f'Este album contiene {self.canciones}'
        return self.canciones

    def __del__(self):
        print(f'El cd se ha eliminado correctamente.')


cd1 = CD('Pink Floyd', 'The Wall', 24)
print(cd1)
print(len(cd1))

cd2: CD = CD('Corazon de chancho', 'Tu cogiste y mataste a la puerca', 5)
print(cd2)
print(len(cd2))
