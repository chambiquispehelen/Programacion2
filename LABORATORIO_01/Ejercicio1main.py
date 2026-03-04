from Ejercicio1 import Cronometro
import random

numeros = []

for i in range(100000):
    numeros.append(random.randint(1, 100000))

crono = Cronometro()

crono.inicia()

n = len(numeros)

for i in range(n):

    minimo = i

    for j in range(i + 1, n):
        if numeros[j] < numeros[minimo]:
            minimo = j

    aux = numeros[i]
    numeros[i] = numeros[minimo]
    numeros[minimo] = aux

crono.detener()

print("Tiempo de ejecución:",
      crono.lapsoDeTiempo(),
      "milisegundos")