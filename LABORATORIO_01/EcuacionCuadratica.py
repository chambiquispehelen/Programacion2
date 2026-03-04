class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscrim(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        d = self.getDiscrim()
        if d < 0:
            return 0
        return (-self.__b + d**0.5) / (2*self.__a)

    def getRaiz2(self):
        d = self.getDiscrim()
        if d < 0:
            return 0
        return (-self.__b - d**0.5) / (2*self.__a)