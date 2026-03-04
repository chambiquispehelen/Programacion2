from EcuacionCuadratica import EcuacionCuadratica

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# validar ecuación cuadrática
if a == 0:
    print("No es una ecuación cuadrática")
else:
    ecuacion = EcuacionCuadratica(a, b, c)

    d = ecuacion.getDiscriminante()

    if d > 0:
        print("La ecuación tiene dos raíces",
              f"{ecuacion.getRaiz1():.6f}",
              "y",
              f"{ecuacion.getRaiz2():.6f}")

    elif d == 0:
        print("La ecuación tiene una raíz",
              f"{ecuacion.getRaiz1():.6f}")

    else:
        print("La ecuación no tiene raíces reales")