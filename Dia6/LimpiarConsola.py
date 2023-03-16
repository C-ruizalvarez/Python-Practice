from os import system
from pathlib import Path

"""
Configuracion necesaria para hacerlo en pycharm
Run -> Debug -> Edit Configurations -> Emulate terminal in output console
"""

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('clear')

print(f"Tu nombre es {nombre} y tienes {edad} años")

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'

carpeta = ruta.parents[3]

print(carpeta)

