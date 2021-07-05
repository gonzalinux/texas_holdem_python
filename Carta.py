from tkinter import *

palos = {0: ["Corazones", "♥", "\\assets\\palos\\heart.png"], 1: ["Picas", "♠", "\\assets\\palos\\pica.png"],
         2: ["Diamantes", "♦", "\\assets\\palos\\diamond.png"], 3: ["Treboles", "♣", "\\assets\\palos\\trebol.png"]}
numeros = {1: "AS", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "J", 11: "Q", 12: "K", 13: "AS"}


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo
        self.numeroescrito = numeros.get(numero)
        self.palocaracter = palos.get(palo)[1]
        self.nombrepalo = palos.get(palo)[0]
        self.imgpalo=palos.get(palo)[2]
        if numero>0:
            self.encadena=self.numeroescrito+' de '+self.palocaracter
        if palo == 0 or palo == 2:

            self.color = "red"
        else:
            self.color = "black"
