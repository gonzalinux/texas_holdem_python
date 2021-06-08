from tkinter import *

palos = {0: ["Corazones", "♥"], 1: ["Picas", "♠"], 2: ["Diamantes", "♦"], 3: ["Treboles", "♣"]}
numeros = {1: "AS", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "J", 11: "Q", 12: "K"}


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palos.get(palo)[0]
        self.numeroescrito = numeros.get(numero)
        self.palocaracter = palos.get(palo)[1]



