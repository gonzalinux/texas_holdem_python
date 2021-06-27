from Carta import Carta


def cmprrescolor(cartas):
    cartasaux = eliminar_repes(cartas)
    contador = 1
    cartanterior = cartasaux[0]
    for carta in cartasaux:
        if carta.numero - 1 == cartanterior.numero and carta.palo == cartanterior.palo:
            contador += 1
        elif contador >= 5:
            break
        else:
            contador = 1
        cartanterior = carta
    if contador >= 5:
        return [11, cartanterior]
    else:
        return None


def cmpr4(cartas):
    contador = 0
    cartanterior = cartas[-1]
    for carta in cartas:

        if cartanterior != None and carta.numero == cartanterior.numero and carta.numero != 1:
            contador += 1
        elif contador >= 4:
            break
        else:
            contador = 0
        cartanterior = carta

    if contador >= 4:
        return [10, cartanterior]
    else:
        return None


def cmprfull(cartas):
    contador = 0
    cartanterior = cartas[-1]
    cartasaux = list(cartas)
    cartastrio = []
    cartasaux.reverse()
    for carta in cartasaux:
        if carta.numero == cartanterior.numero and carta.numero != 1:
            contador += 1
        elif contador >= 3:
            cartastrio.append(cartasaux[cartasaux.index(carta) - 1])
            cartastrio.append(cartasaux[cartasaux.index(carta) - 2])
            cartastrio.append(cartasaux[cartasaux.index(carta) - 3])
            break
        else:
            contador = 0
        cartanterior = carta

    if contador >= 3:
        if len(cartastrio) == 0:
            cartastrio.append(cartasaux[- 1])
            cartastrio.append(cartasaux[- 2])
            cartastrio.append(cartasaux[- 3])
        for carta in cartastrio:
            cartasaux.remove(carta)
        respuesta = cmpr2(cartasaux)
        if respuesta is None:
            return None

        print(respuesta[1].numero)
        return [9, getmasalta([cartanterior, respuesta[1]])]
    else:
        return None


def cmprcolor(cartas):
    palos = [0, 0, 0, 0]

    for carta in cartas:
        palos[carta.palo] += 1

    for p in palos:

        if p >= 5:
            masaltaa = Carta(0, 0)
            for carta in cartas:
                if carta.palo == p and carta.numero > masaltaa.numero:
                    masaltaa = carta

            return [8, masaltaa]

    return None


def cmpresc(cartas):
    cartasaux = eliminar_repes(cartas)
    contador = 1
    cartanterior = cartasaux[0]
    for carta in cartasaux:
        if carta.numero - 1 == cartanterior.numero:
            contador += 1
        elif contador >= 5:
            break
        else:
            contador = 1
        cartanterior = carta
    if contador >= 5:
        return [7, cartanterior]
    else:
        return None


def cmpr3(cartas):
    contador = 1
    cartanterior =Carta(0,0)
    cartasaux = list(cartas)
    cartasaux.reverse()
    for carta in cartasaux:
        if carta.numero == cartanterior.numero and carta.numero != 1:
            contador += 1
        elif contador >= 3:

            break
        else:
            contador = 1
        cartanterior = carta
    if contador >= 3:
        return [6, cartanterior]
    else:
        return None


def cmpr22(cartas):
    contador = 1
    cartanterior = Carta(0,0)
    cartasaux = list(cartas)
    cartasduo = []
    cartasaux.reverse()
    for carta in cartasaux:
        if carta.numero == cartanterior.numero and carta.numero != 1:
            contador += 1
        elif contador >= 2:
            cartasduo.append(cartasaux[cartasaux.index(carta) - 1])
            cartasduo.append(cartasaux[cartasaux.index(carta) - 2])
            break
        else:
            contador = 1
        cartanterior = carta

    if contador >= 2:
        if len(cartasduo) == 0:
            cartasduo.append(cartasaux[- 1])
            cartasduo.append(cartasaux[- 2])
        for carta in cartasduo:
            cartasaux.remove(carta)
        respuesta = cmpr2(cartasaux)
        if respuesta is None:
            return None

        return [5, getmasalta([cartanterior, respuesta[1]])]
    else:
        return None


def cmpr2(cartas):
    contador = 1
    cartanterior = Carta(0,0)
    cartasaux = list(cartas)
    cartasaux.reverse()
    for carta in cartasaux:
        if carta.numero == cartanterior.numero and carta.numero != 1:
            contador += 1
        elif contador >= 2:
            break
        else:
            contador = 1
        cartanterior = carta

    if contador >= 2:
        return [4, cartanterior]
    else:
        return None


def getmasalta(cartas):
    cartasord = ordenarcartas(cartas)
    return cartasord[-1]


def ordenarcartas(cartas):
    cartasordenadas = list(cartas)
    ordenada = False
    ases = []
    while not ordenada:
        ordenada = True
        for i in range(len(cartasordenadas) - 1):

            if cartasordenadas[i].numero > cartasordenadas[i + 1].numero:
                aux = cartasordenadas[i + 1]
                cartasordenadas[i + 1] = cartasordenadas[i]
                cartasordenadas[i] = aux
                ordenada = False

    for carta in cartasordenadas:
        if carta.numero == 1:
            ases.append(Carta(13, carta.palo))
        else:
            break
    cartasordenadas+=ases
    return cartasordenadas


def eliminar_repes(cartas):
    cartasaux = list(cartas)
    for i in range(len(cartas) - 1):
        if cartas[i].numero == cartas[i + 1].numero:
            cartasaux.remove(cartas[i + 1])
    return cartasaux


def jugada_ganadora(cartasmesa, cartasjugador):

    cartasmesa += cartasjugador
    cartas = ordenarcartas(cartasmesa)
    jugadas = list()
    print("aqui se ha invertido")
    jugadas.append(cmprrescolor(cartas))
    jugadas.append(cmpr4(cartas))
    jugadas.append(cmprfull(cartas))
    jugadas.append(cmprcolor(cartas))
    jugadas.append(cmpresc(cartas))
    jugadas.append(cmpr3(cartas))
    jugadas.append(cmpr22(cartas))
    jugadas.append(cmpr2(cartas))
    for i in jugadas:
        if i is not None:
            return i

    return [0, getmasalta(cartas)]


if __name__ == '__main__':
    cartas = [Carta(1, 0), Carta(1, 3), Carta(6, 2), Carta(3, 1), Carta(9, 1)]
    cartas2 = [Carta(2, 1), Carta(12, 1)]
    print(jugada_ganadora(cartas, cartas2)[0])
