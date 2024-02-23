import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusaculas(self):
        palabra = "Hola don Corleone"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Hola Don Corleone")


if __name__ == '__main__':
    unittest.main()
