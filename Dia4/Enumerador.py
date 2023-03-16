lista = ["a", "b", "c"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

for indice, item in enumerate(lista):
    print(indice, item)

mis_tuples = list(enumerate(lista))

print(mis_tuples)

"python".star