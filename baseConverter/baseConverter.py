#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Programa CLI para convertir números entre distintas bases"""


from helpers.helpers import clear, getChar
from controllers.operation import Operation

__author__      = "Julio Aguilar Carmona"
__copyright__   = "Copyleft 2020, Julio Aguilar Carmona"
__license__     = "GPL v3"
__version__     = "0.0.1"
__maintainer__  = "Julio Aguilar Carmona"
__email__       = "julio.aguilarc@gmail.com"
__status__      = "Development"

class Ui:
    """Capa de Interfaz"""

    def __init__(self):
        pass

    def renderBaseMenuOptions(self, discard = "X"):
        """Muestra las opciones del menú para seleccionar el sistema numérico base origen/destino
        descartando, para el caso del destino, la opción seleccionada en el origen"""

        if discard != "B" and discard != "b":
            print("\t(B)inario")
        if discard != "O" and discard != "o":
            print("\t(O)ctal")
        if discard != "D" and discard != "d":
            print("\t(D)ecimal")
        if discard != "H" and discard != "h":
            print("\t(H)exadecimal")
        print("\t-------------")
        if discard != "X":
            print("\t(R)egresar")
        print("\t(S)alir\n")

        opt = getChar()

        if opt == "S" or opt == "s":
            exit()
        if opt == "R" or opt == "r":
            # del self.ui
            # del self.operation
            main()

        return opt

    def renderBaseMenu(self):
        """Muestra en pantalla los menús necesarios para seleccionar el sistema numérico base origen/destino"""

        clear()

        print("BaseConverter es una herramienta para convertir números entre distintas bases de sistemas numéricos." +
            "\n\nSeleccione el sistema numérico base del número que desea convertir (origen): \n")
        origin = self.renderBaseMenuOptions()

        print("\n\nSeleccione la base del sistema numérico al que desea convertir el número (destino): \n")
        destination = self.renderBaseMenuOptions(origin)

        number = input("\n\tIngrese el número a cambiar de base: ")

        return {'origin': origin, 'destination': destination, 'number': number}

def main():
    ui = Ui()
    data = ui.renderBaseMenu()

    operation = Operation(data["origin"], data["destination"])

    if data["origin"] == "D" or data["origin"] == "d":
        resultList = operation.convertDecToBase(int(data["number"]))
    elif data["destination"] == "D" or data["destination"] == "d":
        resultList = operation.convertBaseToDec(data["number"])
    else:
        resultList = operation.convertBaseToBase(data["number"])
        pass

    s = [str(i) for i in resultList]
    result = "".join(s)

    print("\n\t    El resultado es: " + result)
    out = input("\n\tDesea realizar otra conversión?\n\tPresione 'n' para salir o cualquier otra tecla para continuar: ")
    if out == "n":
        exit()
    else:
        main()
    # clear()

if __name__ == '__main__':
    main()
