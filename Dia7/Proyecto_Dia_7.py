from random import *
from time import sleep

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):

        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente {self.nombre} {self.apellido} " \
               f"con numero de cuenta {self.numero_cuenta} " \
               f"tiene un balance de {self.balance} pesos."

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance += -cantidad

def crear_cliente(nombre, apellido, numero_cuenta, balance):
    return Cliente(nombre, apellido, numero_cuenta, balance)

def wait_screen():
    sleep(1.5)

def ejecucion():
    print("Bienvenido al banco Camilo POO")

    _opcion_crear_usuario = input("Desea crear un usuario nuevo? si/no. ")

    if _opcion_crear_usuario.lower() == "si":
        _nombre = input("Cual es tu nombre? ")
        _apellido = input("CUal es tu apellido? ")
        _numero_cuenta = randint(100000,999999)
        _balance = 0.0

        cliente = crear_cliente(_nombre, _apellido, _numero_cuenta, _balance)

        print(f"Creacion exitosa \nNombre: {cliente.nombre} {cliente.apellido} \n"
              f"Numero de cuenta: {cliente.numero_cuenta} \nBalance: {cliente.balance} pesos")
        
        _opcion_menu_principal = ""
        
        while _opcion_menu_principal.lower() != "q":
            wait_screen()
            print(cliente)

            _opcion_menu_principal = input("\nPara depositar dinero en su cuenta presione 1 \n"
                                           "Para retirar dinero de su cuenta presione 2 \n"
                                           "Para salir de la aplicacion presione (q) \n"
                                           "")

            if _opcion_menu_principal == "1":
                _cantidad_depositar = float(input("Cuanto dinero desea depositar?: "))

                cliente.depositar(_cantidad_depositar)
            elif _opcion_menu_principal == "2":
                _cantidad_retirar = float(input("Cuanto dinero desea retirar?: "))

                if cliente.balance - _cantidad_retirar < 0:
                    print("No puede retirar esa cantidad de dinero, \nNo cuenta con suficiente dinero en su cuenta.")
                else:
                    cliente.retirar(_cantidad_retirar)
            elif _opcion_menu_principal.lower() == "q":
                print("Muchas gracias por confiar en nosotros \nVuelve pronto!")
            else:
                print("Opcion ingresada no valida, vuelve a intentarlo.")
        else:
            return None


    elif _opcion_crear_usuario.lower() != "si" and _opcion_crear_usuario.lower() != "no":
        print("Opcion ingresada no valida.")
        ejecucion()
    else:
        print("Muchas gracias por confiar en nosotros \nVuelve pronto!")
        return None

ejecucion()
