nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42, 18]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

uno = ["uno", "um", "one"]
dos = ["dos", "dois", "two"]
tres = ["tres", "três", "three"]
cuatro = ["cuatro", "quatro", "four"]
cinco = ["cinco", "cinco", "five"]

numeros = list(zip(uno,dos,tres,cuatro,cinco))

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))

print(numeros)