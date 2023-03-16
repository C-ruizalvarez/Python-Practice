def suma(*args):

    total = 0

    for arg in args:
        total += arg

    return total

print(suma(4,5))

def suma_cuadrados(*args):

    total = 0

    for arg in args:
        total += arg**2

    return total

def suma_absolutos(*args):

    total = 0

    for arg in args:
        total += abs(arg)

    return total

def numeros_persona(nombre, *args):
    return f"{nombre}, la suma de tus números es {sum(args)}"