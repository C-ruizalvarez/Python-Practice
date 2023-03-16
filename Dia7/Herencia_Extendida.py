# class Animal:
#
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
#
#     def nacer(self):
#         print("Este animal ha nacido")
#
#     def hablar(self):
#         print("Este animal emite un sonido")
#
# class Pajaro(Animal):
#
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo
#
#     def hablar(self):
#         print("Pio")
#
#     def volar(self, metros):
#         print(f"El pajaro vuela {metros} metros")
#
# piolin = Pajaro(3, 'Amarillo', 60)
# mi_animal = Animal(5, 'Negro')
#
# piolin.hablar()
# piolin.volar(100)

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja ja")

    def hablar(self):
        print("Que tal?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()