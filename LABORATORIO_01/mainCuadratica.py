from EcuacionCuadratica import EcuacionCuadratica

# entrada de datos
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

ecuacion = EcuacionCuadratica(a, b, c)

d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuación tiene dos raíces",
          ecuacion.getRaiz1(), "y",
          ecuacion.getRaiz2())

elif d == 0:
    print("La ecuación tiene una raíz",
          ecuacion.getRaiz1())

else:
    print("La ecuación no tiene raíces reales")