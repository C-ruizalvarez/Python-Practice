"""
Va a elegir una palabra secreta y va a mostrrar una serie de guiones cocn el total de palabras
si se equivoca se reducen las vidas, inicica con 6 vidas
"""

from random import choice

def escoger_palabra():
    lista_palabras = ["carro", "python", "esternocleidomastoideo", "hueso", "programacion", "huevo", "ave", "mar",
                      "cosa", "ciudad"]

    return choice(lista_palabras)


def generador_guiones(palabra):
    guion = "_"

    return guion * len(palabra)


def cambiador_guiones_letras(palabra_parcial, palabra_guiones, letra):

    guiones_temp = [n for n in palabra_guiones]

    for index, letra_lista in enumerate(palabra_parcial):
        if letra_lista == letra:
            palabra_parcial[index] = "0"
            guiones_temp[index] = letra

    return palabra_parcial, "".join(guiones_temp)


def juego(palabra):
    palabra_lista = [n for n in palabra]
    palabra_guiones = generador_guiones(palabra)
    vidas = 6
    adivino: bool = False

    while not adivino:
        print(f"Vidas restantes: {vidas}")
        print(f"Palabra para adivinar: {palabra_guiones}")

        letra_adivinar = input("Adivina una letra: ")

        if letra_adivinar not in "abcdefghijklmnopqrstuvxyz" or len(letra_adivinar) > 1:
            print("Lo que acabaste de ingresar no es valido!!!")
            vidas += -1
        elif letra_adivinar not in palabra_lista:
            vidas += -1
        else:
            palabra_lista, palabra_guiones = cambiador_guiones_letras(palabra_lista, palabra_guiones,
                                                                      letra_adivinar)

        if vidas == 0:
            print("Finalizo el juego, te quedaste sin vidas!")
            break
        elif palabra_lista.count("0") == len(palabra_lista):
            print(f"Felicitaciones!! adivinaste la palabra: {palabra} y te quedaron {vidas} vidas")
            break

def iniciador():
    while True:
        print("Bienvenido al juego del ahorcado")
        opcion = input("Estas listo para jugar? s/n ").lower()

        if opcion.__contains__("s"):
            break
        else:
            continue

    juego(escoger_palabra())


iniciador()
