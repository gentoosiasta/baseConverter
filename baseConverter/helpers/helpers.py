#!/usr/bin/env python3

from os import system, name
from time import sleep

def clear():
    # para windows
    if name == 'nt':
        _ = system('cls')

    # para *nix
    else:
        _ = system('clear')

def getChar():
    inputChar = input("\t\tOpción: ")
    allowedChars = 'bBoOdDhHsSrR'

    while(len(inputChar) != 1 or inputChar not in allowedChars):
        inputChar = input("\n\t\tOpción inválida, intente de nuevo\n\t\tOpción: ")
    return inputChar