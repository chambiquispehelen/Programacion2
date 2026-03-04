from Ejercicio4 import Estadistica

datos = []

print("Ingrese 10 números:")

for i in range(10):
    num = float(input("Número: "))
    datos.append(num)

est = Estadistica(datos)

print("El promedio es:", est.promedio())
print("La desviación estándar es:", est.desviacion())