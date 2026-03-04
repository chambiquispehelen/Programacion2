import time

# Clase Cronometro
class Cronometro:

    # Constructor
    def __init__(self):
        # guarda tiempo inicial
        self.__inicio = 0

        # guarda tiempo final
        self.__fin = 0


    # inicia medición del tiempo
    def inicia(self):
        self.__inicio = time.time()


    # detiene medición
    def detener(self):
        self.__fin = time.time()


    # calcula tiempo transcurrido
    def lapsoDeTiempo(self):
        return (self.__fin - self.__inicio) * 1000