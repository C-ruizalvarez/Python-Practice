def organizador_palabras(palabra):

    letras = []

    for letra in palabra.lower():
        if letra not in letras:
            letras.append(letra)

    letras.sort()
    return letras

print(organizador_palabras("Camilooo"))