from Ejercicio1 import Cronometro
import random

# lista vacía
numeros = []

# generar números aleatorios
for i in range(2000):
    numeros.append(random.randint(1,100000))
# crear objeto cronómetro
crono = Cronometro()
# iniciar tiempo
crono.inicia()

# ORDENAMIENTO POR SELECCIÓN
n = len(numeros)
for i in range(n):
    minimo = i
    for j in range(i+1, n):

        if numeros[j] < numeros[minimo]:
            minimo = j

    aux = numeros[i]
    numeros[i] = numeros[minimo]
    numeros[minimo] = aux

# detener tiempo
crono.detener()
# mostrar tiempo
print("Tiempo de ejecución:",
      crono.lapsoDeTiempo(),
      "milisegundos")
