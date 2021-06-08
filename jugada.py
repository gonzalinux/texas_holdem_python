__name__ = "jugada"


def cmprroyal(cartas):
    if cmprescolor(cartas) is None:
        return None
    for i in range(len(cartas) - 4):
        if cartas[i].numero == cartas[i + 1].numero + 1 == cartas[i + 2].numero + 2 == cartas[i + 3].numero + 3 == \
                cartas[i + 4].numero + 4 and cartas[i].palo == cartas[i + 1].palo == \
                cartas[i + 2].palo == cartas[i + 3].palo == cartas[i + 4].palo:
            return cartas[i:i + 4]


def cmprescolor(cartas):
    tupla = {"Corazones": 0, "Diamantes": 0, "Treboles": 1, "Picas": 1}
    escalera = cmpresc(cartas)
    if escalera == None:
        return None
    for i in range(len(cartas) - 4):
        if cartas[i].numero == cartas[i + 1].numero + 1 == cartas[i + 2].numero + 2 == cartas[i + 3].numero + 3 == \
                cartas[i + 4].numero + 4 and tupla.get(cartas[i].palo) == tupla.get(cartas[i + 1].palo) == \
                tupla.get(cartas[i + 2].palo) == tupla.get(cartas[i + 3].palo) == tupla.get(cartas[i + 4].palo):
            return cartas[i:i + 4]


def cmpr4(cartas):
    for i in range(len(cartas) - 3):
        if cartas[i].numero == cartas[i + 1].numero == cartas[i + 2].numero == cartas[i + 3].numero:
            return cartas[i:i + 3]
    return None


def cmprfull(cartas):
    nuevoconj = list(cartas).copy()
    trio = cmpr3(nuevoconj)
    if trio is None:
        return None
    full = trio.copy()
    nuevoconj.remove(trio[0])
    nuevoconj.remove(trio[1])
    nuevoconj.remove(trio[2])
    trio = cmpr2(nuevoconj)
    if trio is None:
        return None
    full.extend(trio)
    return trio


def cmpresc(cartas):
    for i in range(len(cartas) - 4):
        if cartas[i].numero == cartas[i + 1].numero + 1 == cartas[i + 2].numero + 2 == cartas[i + 3].numero + 3 == \
                cartas[i + 4].numero + 4:
            return cartas[i:i + 4]
    return None


def cmpr3(cartas):
    for i in range(len(cartas) - 2):
        if cartas[i].numero == cartas[i + 1].numero == cartas[i + 2].numero:
            return cartas[i:i + 3]
    return None


def cmpr22(cartas):
    nuevoconj = list(cartas).copy()
    pareja = cmpr2(nuevoconj)
    if pareja == None:
        return None
    doble = pareja.copy()
    nuevoconj.remove(pareja[0])
    nuevoconj.remove(pareja[1])
    pareja = cmpr2(nuevoconj)
    if pareja is None:
        return None
    doble.extend(pareja)
    return doble


def cmpr2(cartas):
    for i in range(len(cartas) - 1):
        if cartas[i].numero == cartas[i + 1].numero:
            return cartas[i:i + 2]
    return None


def cmprmasalta(cartas):
    return cartas[0]


def ordenarcartas(cartas):
    cartasordenadas = list(cartas)
    while True:
        seordena = False
        for i in range(len(cartas) - 1):
            j = i + 1
            if cartasordenadas[i].numero > cartasordenadas[j].numero:
                aux = cartasordenadas[i]
                cartasordenadas[i] = cartasordenadas[j]
                cartasordenadas[j] = aux
                seordena = True
        if not seordena:
            break

    return cartasordenadas


def jugada_ganadora(cartasmesa, cartasjugador):
    cartasmesa.update(cartasjugador)
    cartas = ordenarcartas(cartasmesa)
    jugadas = list()
    jugadas.append(cmprroyal(cartas))
    jugadas.append(cmprescolor(cartas))
    jugadas.append(cmpr4(cartas))
    jugadas.append(cmprfull(cartas))
    jugadas.append(cmpresc(cartas))
    jugadas.append(cmpr3(cartas))
    jugadas.append(cmpr22(cartas))
    jugadas.append(cmpr2(cartas))

    for i in range(len(jugadas)):
        if jugadas[i] is not None:
            return [i, jugadas[i]]

    return [12 - cmprmasalta(ordenarcartas(cartasjugador)).numero]
