class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):

        # a) Atributos privados
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    # c) Método que verifica si tiene solución
    def tienSolucion(self):
        determ = self.__a * self.__d - self.__b * self.__c

        if determ != 0:
            return True
        else:
            return False
    # d) Método para calcular X
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        return x

    # d) Método para calcular Y
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        return y