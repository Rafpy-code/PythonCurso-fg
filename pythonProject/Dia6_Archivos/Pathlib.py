from pathlib import Path, PureWindowsPath

carpeta = Path('D:/PROGRAMACION/PythonCursoFedericoGaray/pythonProject/Dia6_Archivos/archivo1.txt')
print(f'carpeta.name => {carpeta.name}')
print(f'carpeta.stem => {carpeta.stem}')
print(f'carpeta.suffix => {carpeta.suffix}')
print(f'carpeta.read_text() =>\n{carpeta.read_text()}')

if not carpeta.exists():
    print('if not carpeta.exists(): => El archivo no existe.')
else:
    print(f'carpeta.lstat() => {carpeta.lstat()}')

# Importar PureWindowsPath
ruta_windows = PureWindowsPath(carpeta)
print(f'ruta_windows => {ruta_windows}')
