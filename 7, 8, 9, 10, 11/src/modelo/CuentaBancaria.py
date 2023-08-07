#NOTA: Se agregó un campo nuevo para ver que accion quiere tomar el cliente
class CuentaBancaria():
    def __init__(self, numero_cuenta, propietarios, balance, accion):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        self.accion = accion