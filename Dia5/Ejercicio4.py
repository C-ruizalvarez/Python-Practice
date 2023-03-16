def es_primo(num):
    evaluador = None

    for i in range(2,num):
        if num % i == 0:
            evaluador = 1
            break

    evaluador = True if evaluador is None else False

    return evaluador

def contar_primos(num):

    contador_primos = 0

    for i in range(2, num):
        eval = es_primo(i)

        if eval:
            print(f"El numero {i} es primo")
            contador_primos += 1

    if es_primo(num):
        print(f"El numero {num} es primo")
        contador_primos += 1

    return contador_primos

print(contar_primos(17))