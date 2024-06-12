import unittest
import cambia_texto
# import pytest


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusaculas(self):
        palabra = "Hola don Corleone"
        resultado = cambia_texto.todo_mayusculas(palabra)
        # self.assertEqual(resultado, "Hola Don Corleone")
        self.assertEqual(resultado, "HOLA DON CORLEONE")


if __name__ == '__main__':
    unittest.main()
