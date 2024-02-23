from pathlib import Path

ruta_base = Path.home()
print(ruta_base)

ruta = Path("Curso Python", "Día 6", "practicas_path.py")
print(ruta)

relativa = ruta.relative_to(Path('Curso Python', 'Día 6'))
print(relativa)

ruta = Path('/home/evaluator/Curso Python/Día 6/practicas_path.py')

print(ruta)