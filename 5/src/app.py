from modelo.circulo import Circulo

area = Circulo(radio=8, punto1=2, punto2=5, centro=(2,5))
print("El area del circulo es de: ", (area.radio * area.radio) * 3.1416)

punto_perteneciente = Circulo(radio=8, punto1=2, punto2=5, centro=(2,5))
import random
punto_perteneciente.punto1 = random.randint(0,20)
punto_perteneciente.punto2 = random.randint(0,20)
if ((punto_perteneciente.punto1 - area.punto1)**2) + ((punto_perteneciente.punto2 - area.punto2)**2) < ((punto_perteneciente.radio)**2):
    print("El punto: ", punto_perteneciente.punto1, ",", punto_perteneciente.punto2, " si pertenece a la circunferencia")
else:
    print("El punto: ", punto_perteneciente.punto1, ",", punto_perteneciente.punto2, " no pertenece a la circunferencia")