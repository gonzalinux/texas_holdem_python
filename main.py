# This is a sample Python script.
import random

palos = ("Corazones", "Picas", "Diamantes", "Treboles")
numeros = {1: "AS", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "J", 11: "Q", 12: "K"}


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo
        self.numeroescrito = numeros.get(numero)


def sacar_cartas(numeroasacar):
    x = 0
    cartasmesa = set()
    while len(cartasmesa) != numeroasacar:
        aux = cartas[random.randint(0, len(cartas) - 1)]
        cartasmesa.add(aux)
        cartas.remove(aux)

    # for cartat in cartasmesa:
    #    print(cartat.numeroescrito + " de " + cartat.palo)
    return cartasmesa


def inicio():
    entrada = input("Escriba sus decisiones:\n"
                    "Jugar Salir\n")
    if entrada == "Salir":
        print("Hasta la proxima")
        exit(0)
    elif entrada != "Salir" and entrada != "Jugar":
        print("por favor escoja una opcion correcta")
        inicio()
    elif entrada == "Jugar":
        return 1


def apostar():
    print("Sigue?")
    entrada = input("Escriba sus decisiones:\n"
                    "Subir la apuesta | Pasar | Retirarse\n")
    if entrada == "Subir la apuesta":
        return 2
    elif entrada == "Pasar":
        return 1
    elif entrada == "Retirarse":
        print("Hasta la proxima")
        exit(0)
    else:
        print("por favor escoja una opcion correcta")
        apostar()


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.palos
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global cartas
    cartas = list()
    for i in range(0, 4):
        for j in range(1, 13):
            cartas.append(Carta(j, palos[i]))
    cartasdelpc = sacar_cartas(2)
    cartasdeluser = sacar_cartas(2)
    print("Bienvenido a tu juego favorito de TEXAS HOLDEM \n"
          "que os apeteceria hacer hoy?")
    inicio()
    print("De acuerdo, Primera ronda\n"
          "Aqui estan tus cartas\n")
    for carta in cartasdeluser:
        print(carta.numeroescrito + " de " + carta.palo)
    print("\n")
    seguir = apostar()
    if seguir == 1:
        
