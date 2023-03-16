archivo = open("Prueba.txt", "w")

archivo.write("hola \n")
archivo.write("mundo \n")

archivo.writelines(["hola", "mundo", "aqui", "estoy \n"])

lista = ["hola", "mundo", "aqui", "estoy"]

for palabra in lista:
    archivo.write(palabra + "\n")

archivo.close()