def suma(**kwargs):
    print(type(kwargs))

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(suma(x=3, y=5, z=2))

def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,20,100,200,300,400, x = 'uno', y = 'dos', z = 'tres')

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args,**kwargs)

def cantidad_atributos(**kwargs):
    return len(kwargs.items())

print(cantidad_atributos(**kwargs))

def lista_atributos(**kwargs):
    valores = []

    for key, value in kwargs.items():
        valores.append(value)

    return valores

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")