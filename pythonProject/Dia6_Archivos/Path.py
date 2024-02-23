from pathlib import Path

base = Path.home()
# guia = Path(base, 'Europa', 'España', 'Madrid', 'Puerta de Toledo.txt')
guia = Path(base, 'Europa', 'España', Path('Madrid', 'Puerta de Toledo.txt'))

print(base)
print(guia)
print(guia.parent)
print(guia.parent.parent)
print(guia.parents)

mi_directorio = 'D:/PROGRAMACION/PythonCursoFedericoGaray/Proyectos/Dia6_Archivos/ruta_archivos'
guia1 = Path(mi_directorio, 'Europa')
for txt in Path(guia1).glob("**/*.txt"):
    print(txt)

guia2 = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
en_europa = guia2.relative_to(Path('Europa'))
en_espania = guia2.relative_to(Path('Europa', 'España'))

print(en_europa)
print(en_espania)
