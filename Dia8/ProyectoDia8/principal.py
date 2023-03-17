from turnos import *
from os import system
from time import sleep

def pedir_turno():
    farmacia = turnos_farmacia()
    perfumeria = turnos_perfumeria()
    cosmeticos = turnos_cosmeticos()

    while True:
        try:
            system('cls')
            print("Bienvenido a la farmacia!!")
            print("Que servicio necesita?")
            numero = int(input("\n\nIngrese 1 para farmacia \nIngrese 2 para perfumeria \nIngrese 3 para cosmeticos "
                               "\nIngrese 0 para terminar programa \n"))

            if numero > 3:
                raise Exception
        except:
            system('cls')
            print("La opcion seleccionada no existe")
            sleep(1)
        else:

            @decorador_turnos
            def turno_farmacia():
                print(next(farmacia))

            @decorador_turnos
            def turno_perfumeria():
                print(next(perfumeria))

            @decorador_turnos
            def turno_cosmeticos():
                print(next(cosmeticos))

            if numero == 1:
                turno_farmacia()
            elif numero == 2:
                turno_perfumeria()
            elif numero == 3:
                turno_cosmeticos()
            elif numero == 0:
                print("ADIOS")
                break


pedir_turno()
