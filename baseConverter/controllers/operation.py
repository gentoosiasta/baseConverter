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
        """Método para convertir un numero Decimal a una Base dada"""
        base = self.__numericSystemToBase(self.__destination)
        resultList = []
        remainder = number % base

        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"

        resultList.append(remainder)
        number = number / base
        number = int(number)

        while number != 0:
            remainder = number % base

            if remainder == 10:
                remainder = "A"
            if remainder == 11:
                remainder = "B"
            if remainder == 12:
                remainder = "C"
            if remainder == 13:
                remainder = "D"
            if remainder == 14:
                remainder = "E"
            if remainder == 15:
                remainder = "F"

            resultList.append(remainder)
            number = number / base
            number = int(number)

        return reverseList(resultList)

    def convertBaseToDec(self, number):
        """Método para convertir un número de una Base dada a Decimal"""
        base = self.__numericSystemToBase(self.__origin)
        # number = string(number)
        numberList = list(number)
        numberList = reverseList(numberList)
        result = [0]

        for i in range(len(numberList)):
            if numberList[i] == 'A' or numberList[i] == 'a':
                numberList[i] = 10
            if numberList[i] == 'B' or numberList[i] == 'b':
                numberList[i] = 11
            if numberList[i] == 'C' or numberList[i] == 'c':
                numberList[i] = 12
            if numberList[i] == 'D' or numberList[i] == 'd':
                numberList[i] = 13
            if numberList[i] == 'E' or numberList[i] == 'e':
                numberList[i] = 14
            if numberList[i] == 'F' or numberList[i] == 'f':
                numberList[i] = 15

            result[0] += int(numberList[i]) * base ** i

        return result

    def convertBaseToBase(self, number):
        """Método para convertir entre bases distintas de Decimal"""
        baseOrig = self.convertBaseToDec(number)
        s = [str(i) for i in baseOrig]
        result = "".join(s)
        #print(result)
        baseDest = self.convertDecToBase(int(result))

        return baseDest

def reverseList(lst):
    """Invierte el orden de una lista"""
    lst.reverse()
    return lst