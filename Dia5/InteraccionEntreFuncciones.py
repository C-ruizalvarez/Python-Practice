from random import shuffle
from random import randint
from random import choice

#Lista inicial
palitos = ['-', '--', '---', '----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedir intento al usuari
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

#Comprobar intento
def chequear_intento(lista, intento):

    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)

    return dado1, dado2

def evaluar_jugada(dado1, dado2):

    suma_dados = dado1 + dado2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))

def reducir_lista(lista):

    lista.remove(max(lista))

    lista_limpia = []

    for num in lista:
        if num not in lista_limpia:
            lista_limpia.append(num)

    return lista_limpia

def promedio(lista):

    suma = 0

    for num in lista:
        suma += num

    return suma / len(lista)

lista_numeros = [1,2,3,4,5,2]

print(promedio(reducir_lista(lista_numeros)))

def lanzar_moneda():
    caras_moneda = ["Cara", "Cruz"]

    return choice(caras_moneda)

def probar_suerte(resultado, lista_numeros):

    if resultado == "Cara":
        lista_numeros.clear()
        print("La lista se autodestruirá")
        return lista_numeros
    elif resultado == "Cruz":
        print("La lista fue salvada")
        return lista_numeros

lista_numeros = [10,2,30,55,32]

probar_suerte(lanzar_moneda(), lista_numeros)