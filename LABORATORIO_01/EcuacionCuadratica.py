import math
class EcuacionCuadratica:

    # b) Constructor
    def __init__(self, a, b, c):

        # a) Atributos privados
        self.__a = a
        self.__b = b
        self.__c = c

    # c) Método que calcula el discriminante
    def getDiscriminante(self):
        d = self.__b**2 - 4*self.__a*self.__c
        return d

    # d) Método para la primera raíz
    def getRaiz1(self):
        d = self.getDiscriminante()

        if d >= 0:
            r1 = (-self.__b + math.sqrt(d)) / (2*self.__a)
            return r1
        else:
            return 0

    # d) Méodo para la segunda raíz
    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            r2 = (-self.__b - math.sqrt(d)) / (2*self.__a)
            return r2
        else:
            return 0