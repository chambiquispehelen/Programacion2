import math

def promedio(datos):

    suma = 0

    # Recorre todos los números de la lista
    for numero in datos:
        suma = suma + numero

    prom = suma / len(datos)

    return prom

def desviacion(datos):

    prom = promedio(datos)

    suma = 0

    # Aplicación de la fórmula estadística
    for numero in datos:
        suma = suma + (numero - prom) ** 2

    des = math.sqrt(suma / (len(datos) - 1))

    return des


datos = []

print("Ingrese 10 números:")

for i in range(10):
    num = float(input("Número: "))
    datos.append(num)

print("El promedio es:", promedio(datos))
print("La desviación estándar es:", desviacion(datos))