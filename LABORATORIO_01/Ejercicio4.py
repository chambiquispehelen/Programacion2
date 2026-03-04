import math

class Estadistica:

    # Constructor
    def __init__(self, datos):
        self.__datos = datos

    # Promedio
    def promedio(self):
        suma = 0
        for numero in self.__datos:
            suma = suma + numero
        prom = suma / len(self.__datos)
        return prom

    # Desviación estándar
    def desviacion(self):
        prom = self.promedio()
        suma = 0

        for numero in self.__datos:
            suma = suma + (numero - prom) ** 2

        des = math.sqrt(suma / (len(self.__datos) - 1))
        return des