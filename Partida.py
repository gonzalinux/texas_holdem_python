# This is a sample Python script.
import random
import jugada
import tkinter

__name__ = "Partida"









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


























   """ entrada = input("Escriba sus decisiones:\n"
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


def partida():
    global cartas
    cartas = list()
    for i in range(0, 4):
        for j in range(1, 13):
            cartas.append(Carta(j, i))

    cartasdelpc = sacar_cartas(2)
    cartasdeluser = sacar_cartas(2)
    print("Bienvenido a tu juego favorito de TEXAS HOLDEM \n"
          "que os apeteceria hacer hoy?")
    inicio()
    print("De acuerdo, Primera ronda\n"
          "Aqui estan tus cartas\n")
    imprimircartas(cartasdeluser)
    print("\n")
    seguir = apostar()
    cartasdelamesa = sacar_cartas(3)
    while len(cartasdelamesa) != 5:
        print("Cartas en la mesa:")
        imprimircartas(cartasdelamesa)
        apostar()
        cartasdelamesa.update(sacar_cartas(1))

    imprimircartas(cartasdelamesa)
    print("Tus cartas son: ")
    imprimircartas(cartasdeluser)
    print("Las cartas de la maquina son: ")
    imprimircartas(cartasdelpc)
    puntuacionuser = jugada.jugada_ganadora(cartasdelamesa, cartasdeluser)
    puntuacionpc = jugada.jugada_ganadora(cartasdelamesa, cartasdelpc)
    if puntuacionpc[0] > puntuacionuser[0]:
        print("gana el user con la jugada:" + str(puntuacionuser[0]))
        imprimircartas(puntuacionuser[1])
    elif puntuacionpc[0] < puntuacionuser[0]:
        print("gana la maquina con la jugada " + str(puntuacionpc[0]) + "y las cartas de la jugada son \n")
        imprimircartas(puntuacionpc[1])
    else:
        print("empate")
"""