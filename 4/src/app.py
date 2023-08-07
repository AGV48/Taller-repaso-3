from modelo.rectangulo import Rectangulo

puntos = Rectangulo()
puntos.punto1 = int(input("Ingrese un lado de rectangulo: "))
puntos.punto2 = int(input("Ingrese el otro lado del rectangulo: "))

print("")

figura = Rectangulo()
if puntos.punto1 == puntos.punto2:
    print("La figura es un cuadrado")
else:
    print("La figura es un rectangulo")

perimetro = Rectangulo()
if puntos.punto1 == puntos.punto2:
    print("El perimetro del cuadrado es de: ", puntos.punto1 + puntos.punto2)
else:
    print("El perimetro del rectangulo es de: ", puntos.punto1 + puntos.punto2)

area = Rectangulo()
if puntos.punto1 == puntos.punto2:
    print("El area del cuadrado es de: ", puntos.punto1 * puntos.punto2)
else:
    print("El area del rectangulo es de: ", puntos.punto1 * puntos.punto2)
