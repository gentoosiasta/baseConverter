#!/usr/bin/env python3

from os import system, name
from time import sleep

def clear():
    """Función para limpiar la terminal"""
    # para windows
    if name == 'nt':
        _ = system('cls')

    # para *nix
    else:
        _ = system('clear')

def getChar():
    """Función para capturar un caracter"""
    inputChar = input("\tOpción: ")
    allowedChars = 'bBoOdDhHsSrR'

    while(len(inputChar) != 1 or inputChar not in allowedChars):
        inputChar = input("\n\tOpción inválida, intente de nuevo\n\t\tOpción: ")
    return inputChar