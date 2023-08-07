from modelo.punto import Punto

mostrar = Punto()
print("Las coordenadas del punto en el plano cartesiano son: ", mostrar.coordenadas)

mover = Punto()
import random
mover.coordenada1 = random.randint(0,10)
mover.coordenada2 = random.randint(0,10)
mover.coordenadas = mover.coordenada1, mover.coordenada2
print("Las coordenadas del nuevo punto son: ", mover.coordenadas)

calcular_distancia = Punto()
calcular_distancia.coordenada1 = mostrar.coordenada1 - mover.coordenada1
calcular_distancia.coordenada2 = mostrar.coordenada2 - mover.coordenada2
calcular_distancia.coordenadas = calcular_distancia.coordenada1, calcular_distancia.coordenada2
print("La distancia entre los dos puntos es de: ", calcular_distancia.coordenadas)


