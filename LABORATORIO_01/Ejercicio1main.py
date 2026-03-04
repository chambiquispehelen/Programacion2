from Ejercicio1 import Cronometro
import random

# crear lista vacía
numeros = []

# generar 100000 números aleatorios
for i in range(100000):
    numeros.append(random.randint(1,100000))

# crear objeto cronómetro
crono = Cronometro()

# iniciar medición
crono.inicia()

# ORDENACIÓN POR SELECCIÓN
n = len(numeros)

for i in range(n):

    minimo = i

    for j in range(i+1, n):

        if numeros[j] < numeros[minimo]:
            minimo = j

    aux = numeros[i]
    numeros[i] = numeros[minimo]
    numeros[minimo] = aux

# detener cronómetro
crono.detener()

# mostrar tiempo
print("Tiempo de ejecución:",
      crono.lapsoDeTiempo(),
      "milisegundos")