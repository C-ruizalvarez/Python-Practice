"""
Programa preguntar nombre y luego decir que tiene 8 intentos para adivinar un num entre 1 y 100

consignas:
- si usuario elige un numero menor a 1 o superior a 100 va a decir que no esta permitido
- si el usuario eligio un numero menor al que penso el programa le va a decir que esta mal y que el numero que escogio es menor
- si el usuario eligio un numero mayor al que penso el programa le va a decir que esta mal y que el numero que escogio es mayor
- si el usuario acerto se le informa que ha ganado y cuantos intentos le tomo lograrlo
"""
from random import randint

print("============================")
print("Adivina el numero secreto!!!")
print("============================")

nombre_usuario = input("\nComo te llamas?: ")

print(f"\nHola! {nombre_usuario} bienvenido! \nTienes 8 intentos para adivinar el numero secreto (esta entre 1 y 100 :O)..... \nPREPARADO???\n")

intentos, num_secreto = 1, randint(1,100)

while intentos <= 8:
    num_usuario = int(input("Que numero vas a escoger?: "))

    if num_usuario > 100 or num_usuario < 1:
        print("El numero que escogiste esta por fuera del rango de juego!!!")
    elif num_usuario > num_secreto:
        print("El numero que escogiste es mayor que el numero secreto...")
    elif num_usuario < num_secreto:
        print("El numero que escogiste es menor que el numero secreto...")
    else:
        mensaje = f"Has ganado {nombre_usuario}!!! encontraste el numero secreto ({num_secreto}) en {intentos} intentos!"
        delimitador = "="*len(mensaje)

        print(delimitador)
        print(mensaje)
        print(delimitador)

        break

    intentos += 1
else:
    print("\n===================================")
    print("Te quedaste sin intentos, GAME OVER")
    print("===================================")
