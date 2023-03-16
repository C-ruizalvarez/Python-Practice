#Pedir al usuario un texto, luego pedir 3 letras, 5 analisis
#Cuantas veces aparecec cada letra
#Pasar el texto a minuscculas
#Cuantas palabras hay en todo el texto
#Cual es la primera letra del texto y cual es la ultima
#texto en orden invertido
#Nos va a decir si apareece la palabra python

texto = input("Ingresa un texto: \n").lower()
letra1 = input("Ingresa una letra: \n").lower()
letra2 = input("Ingresa una letra: \n").lower()
letra3 = input("Ingresa una letra: \n").lower()

print(f"La letra {letra1} aparece {texto.count(letra1)} veces en el texto")
print(f"La letra {letra2} aparece {texto.count(letra2)} veces en el texto")
print(f"La letra {letra3} aparece {texto.count(letra3)} veces en el texto")

palabras = texto.split()

print(f"En el texto hay un total de {len(palabras)} palabras")
print(f"La primera letra del texto es {texto[0]} y la ultima {texto[-1]}")
print(f"El texto en orden invertido es: {texto[::-1]}")
print(f"Aparece la palabra python?: {'python' in texto}")