def chequear_3_cifras(numero):
    return numero in range(100, 1000)

suma = 586 + 402

resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras_lista(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

resultado = chequear_3_cifras_lista([55,99,6000])
print(resultado)

resultado2 = chequear_3_cifras_lista([555,99,6000])
print(resultado2)

resultado3 = chequear_3_cifras_lista([55,99,600])
print(resultado3)

def chequear_3_cifras_lista2(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

    return False

resultado4 = chequear_3_cifras_lista2([55,99,6000])
print(resultado4)

def chequear_3_cifras_lista3(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado5 = chequear_3_cifras_lista3([555,99,600])
print(resultado5)