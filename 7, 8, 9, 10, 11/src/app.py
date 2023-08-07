from modelo.CuentaBancaria import CuentaBancaria

cuenta = CuentaBancaria(numero_cuenta="", propietarios="", balance=0, accion=0)
cuenta.numero_cuenta = input("Ingrese el numero de la cuenta: ")
cuenta.propietarios = input("Ingrese el nombre de el/los propietario/s de la cuenta: ")
cuenta.balance = float(input("Ingrese el saldo de la cuenta: "))

cuenta.accion = int(input("Que desea hacer?, pulse 1 para depositar, 2 para retirar, 3 para ver la cuota de manejo, 4 para ver detalles de la cuenta o 0 para salir: "))
while cuenta.accion != 0:
    if cuenta.accion == 1:
        depositar = CuentaBancaria(numero_cuenta="", propietarios="", balance=0, accion=0)
        depositar.balance = float(input("Ingrese la cantidad que desea depositar: "))
        cuenta.balance = cuenta.balance + depositar.balance
        print("Se han agregado: $", depositar.balance, ", correctamente")
        print("El nuevo saldo es de: $", cuenta.balance)
    else:
        if cuenta.accion == 2:
            retirar = CuentaBancaria(numero_cuenta="", propietarios="", balance=0, accion=0)
            retirar.balance = float(input("Ingrese la cantidad que desea retirar: "))
            if retirar.balance > cuenta.balance:
                print("Saldo insuficiente")
            else:
                cuenta.balance = cuenta.balance - retirar.balance
                print("Se han retirado correctamente: $", retirar.balance)
                print("El nuevo saldo es de: $", cuenta.balance)
        else:
            if cuenta.accion == 3:
                aplicar_cuota_manejo = CuentaBancaria(numero_cuenta="", propietarios="", balance=0, accion=0)
                aplicar_cuota_manejo.balance = (cuenta.balance * 2)/100
                cuenta.balance = cuenta.balance - aplicar_cuota_manejo.balance
                print("Se ha aplicado un 2% de cuota de manejo a la cuenta")
                print("El nuevo saldo es de: $", cuenta.balance)
            else:
                if cuenta.accion == 4:
                    mostrar_detalles = CuentaBancaria(numero_cuenta="", propietarios="", balance=0, accion=0)
                    print("El numero de la cuenta es: ", cuenta.numero_cuenta)
                    print("El/los propietario/s de la cuenta son: ", cuenta.propietarios)
                    print("En la cuenta, actualmente hay: $", cuenta.balance)
                else:
                    print("Accion no registrada")
    cuenta.accion = int(input("Que desea hacer?, pulse 1 para depositar, 2 para retirar, 3 para ver la cuota de manejo, 4 para ver detalles de la cuenta o 0 para salir: "))
            