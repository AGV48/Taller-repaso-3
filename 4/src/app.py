from modelo.rectangulo import Rectangulo

puntos = Rectangulo()
print("Punto 1:")
puntos.x1 = int(input("Ingrese la coordenada en x del primer punto: "))
puntos.y1 = int(input("Ingrese la coordenada en y del primer punto: "))
print("")
print("Punto 2:")
puntos.x2 = int(input("Ingrese la coordenada en x del segundo punto: "))
puntos.y2 = int(input("Ingrese la coordenada en y del segundo punto: "))

print("")

lados = Rectangulo()
lados.base = puntos.x2 - puntos.x1
lados.altura = puntos.y2 - puntos.y1
print("La medida de la base de la figura es: ", lados.base)
print("La medida de la altura de la figura es: ", lados.altura)

print("")

figura = Rectangulo()
if lados.base == lados.altura:
    print("La figura es un:")
    print("--------------")
    print("   Cuadrado   ")
    print("--------------")
else:
    print("La figura es un:")
    print("----------------------")
    print("      Rectángulo      ")
    print("----------------------")

print("")

perimetro = Rectangulo()
if lados.base == lados.altura:
    print("El perimetro del cuadrado es de: ", lados.base**4)
else:
    print("El perimetro del rectangulo es de: ", ((lados.base**2) + (lados.altura**2)))

area = Rectangulo()
if  lados.base == lados.altura:
    print("El area del cuadrado es de: ", lados.base * lados.altura)
else:
    print("El area del rectangulo es de: ", lados.base * lados.altura)
