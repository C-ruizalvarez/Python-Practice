def cero_repetido(*args):

    validador = None

    for index, value in enumerate(args):
        if value == 0 and args.count(value) >= 2 and len(args) - 1 > index > 0:
            validador = True if args[index - 1] == 0 or args[index + 1] == 0 else False
        elif value == 0 and args.count(value) >= 2 and index == 0:
            validador = True if args[index + 1] == 0 else False
        elif value == 0 and args.count(value) >= 2 and index == len(args) - 1:
            validador = True if args[index - 1] == 0 else False

        if validador: break

    return validador

lista = [0,1,2,0,3,4,5,0,6,67]

print(cero_repetido(0,1,5,0,6,0,67,0))