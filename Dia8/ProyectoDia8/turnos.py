from os import system
from time import sleep


def decorador_turnos(function):

    def style_adder():
        system('cls')
        print("\nSu turno es: ")
        function()
        print("Pronto sera atendido.\n")
        sleep(2)

    return style_adder


def turnos_perfumeria():
    turn = 1

    while True:
        if turn > 50:
            turn = 1
        yield f"P - {turn}"
        turn += 1


def turnos_farmacia():
    turn = 1

    while True:
        if turn > 50:
            turn = 1
        yield f"F - {turn}"
        turn += 1


def turnos_cosmeticos():
    turn = 1

    while True:
        if turn > 50:
            turn = 1
        yield f"C - {turn}"
        turn += 1

