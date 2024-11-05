import os
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
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Numero de cuenta: {self.numero_cuenta}
        Balance: ${self.balance}"""

    def depositar(self):
        deposito = int(input("Ingresa la cantidad que quieres depositar:\n$"))
        return deposito

    def retirar(self):
        retiro = int(input("Ingresa la cantidad que quieres retirar:\n$"))
        return retiro

def crear_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu numero de cuenta: ")
    balance = int(input("Ingresa tu balance: "))

    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

def inicio():
    cliente = crear_cliente()
    print(cliente)
    eleccion = "a"

    while eleccion != 3:
        eleccion = int(input("""
    -Presiona [1] para depositar
    -Presiona [2] para retirar
    -Presiona [3] para salir
    """))
        if eleccion == 1:

            cliente.balance += cliente.depositar()
            print("Deposito exitoso")

        elif eleccion == 2:
            if cliente.balance == 0:
                print("Cuenta en 0, no puedes retirar")
            else:

                retiro = cliente.retirar()

                while cliente.balance < retiro:
                    print("Saldo insuficiente. Intente de nuevo")
                    retiro = cliente.retirar()
                    if cliente.balance == retiro:
                        pass

                cliente.balance -= retiro
                print("Retiro exitoso")

        os.system('cls')
        print(cliente)

    return True
inicio()

