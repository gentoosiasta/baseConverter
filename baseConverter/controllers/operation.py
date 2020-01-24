#!/usr/bin/env python3

class Operation:
    """Capa de Modelo de Negocio"""
    def __init__(self, origin, destination):
        self.__origin = origin
        self.__destination = destination

    @property
    def origin(self):
        return self.__origin

    @property
    def destination(self):
        return self.__destination

    @origin.setter
    def origin(self, value):
        self.__origin = value

    @destination.setter
    def destination(self, value):
        self.__destination = value

    def __numericSystemToBase(self, numericSystem):
        if numericSystem == 'b' or numericSystem == 'B':
            return 2
        if numericSystem == 'o' or numericSystem == 'O':
            return 8
        if numericSystem == 'h' or numericSystem == 'H':
            return 16

    def show(self):
        print("Origen: " + self.__origin)
        print("Destino: " + self.__destination)

    def convertDecToBase(self, number):
        base = self.__numericSystemToBase(self.__destination)
        partialResult = number%self.__destination

        while(number != 0):