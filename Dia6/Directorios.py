import os
from pathlib import Path

ruta = os.getcwd()

ruta2 = os.chdir("/Users/camilo.ruiz/Desktop/Alternativo")

archivo = open("Otro_archivo.txt")

ruta = os.makedirs("/Users/camilo.ruiz/Desktop/Alternativo/otra")

print(ruta)
print(ruta2)

archivo.close()

ruta = '/Users/camilo.ruiz/PycharmProjects/UDEMY-Python/venv/Dia6/Prueba.txt'

elemento = os.path.basename(ruta)
elemento2 = os.path.dirname(ruta)
elemento3 = os.path.split(ruta)

print(elemento)
print(elemento2)
print(elemento3)

os.rmdir("/Users/camilo.ruiz/Desktop/Alternativo/otra")

otro_archivo = open("/Users/camilo.ruiz/Desktop/Alternativo/Otro_archivo.txt")
print(otro_archivo.read())

carpeta = Path("/Users/camilo.ruiz/Desktop/Alternativo")
archivo = carpeta / "Otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())

otro_archivo.close()
mi_archivo.close()