lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista2 = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f'Nombre que no comienza con L: {nombre}')

numeros = [1,2,3,4,5,6]

mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}

for item in dic:
    print(item)


for item in dic.items():
    print(item)


for item in dic.values():
    print(item)


for a,b in dic.items():
    print(a,b)