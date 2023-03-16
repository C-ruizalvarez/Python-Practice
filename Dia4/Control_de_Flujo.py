if 10 > 9:
    print("Es correcto")

if True:
    print("Es true")

x = True

if x:
    print("La variable es True")

if 5 == 2:
    print("Es true")
else:
    print("No es correcto")

mascota = 'perro'

if mascota == 'gato':
    print("Tienes un gato")
elif mascota == 'perro':
    print("Tienes un perro")
elif mascota == 'pez':
    print("Tienes un pez")
else:
    print("No se que animal tienes")

edad = 16
califiacion = 9

if edad < 18:
    print("Eres menor de edad")

    if califiacion >= 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("Eres adulto")