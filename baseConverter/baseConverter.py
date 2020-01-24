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
            print("\t\t(B)inario")
        if discard != "O" and discard != "o":
            print("\t\t(O)ctal")
        if discard != "D" and discard != "d":
            print("\t\t(D)ecimal")
        if discard != "H" and discard != "h":
            print("\t\t(H)exadecimal")
        print("\t\t-------------")
        if discard != "X":
            print("\t\t(R)egresar")
        print("\t\t(S)alir")
        print("\n")

        opt = getChar()
        return opt

    def renderBaseMenu(self):
        """Muestra en pantalla los menús necesarios para seleccionar el sistema numérico base origen/destino"""

        clear()
        print("""
            BaseConverter es una herramienta para convertir números entre distintas bases de sistemas numéricos.

            Por favor seleccione el sistema numérico base del número que desea convertir (origen):
            """)

        origin = self.renderBaseMenuOptions()

        print("""
            Ahora seleccione la base del sistema numérico al que desea convertir el número (destino):
            """)

        destination = self.renderBaseMenuOptions(origin)

        return {'origin': origin, 'destination': destination}

    def operationSelector(self, originBase, destinationBase):
        "Permite seleccionar la operación adecuada en base a la información proporcionada"



def main():
    ui = Ui()
    data = ui.renderBaseMenu()

    operation = Operation(data["origin"], data["destination"])

    # clear()

if __name__ == '__main__':
    main()
