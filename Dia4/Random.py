from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = round(uniform(1,5),3)
print(aleatorio2)

aleatorio3 = round(random(),5)
print(aleatorio3)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)