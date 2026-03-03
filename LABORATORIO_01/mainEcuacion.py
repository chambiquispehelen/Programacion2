from EcuacionLineal import EcuacionLineal

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():

    print("x =", ecuacion.getX())
    print("y =", ecuacion.getY())

else:

    print("La ecuación no tiene solución")