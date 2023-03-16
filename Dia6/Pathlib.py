from pathlib import Path
from pathlib import PureWindowsPath

carpeta = Path("/Users/camilo.ruiz/PycharmProjects/UDEMY-Python/venv/Dia6/Prueba.txt")

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial!! existe")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)