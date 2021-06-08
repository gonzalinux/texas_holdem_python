__name__="__main__"

import tkinter

import Partida
import jugada
from tkinter import *
import Screen
import Carta

def sacar_cartas(numeroasacar):
  x = 0

  for i in range(0, 4):
    for j in range(1, 13):
      cartas.append(Carta(j, i))
  cartasmesa = set()
  while len(cartasmesa) != numeroasacar:
    aux = cartas[random.randint(0, len(cartas) - 1)]
    cartasmesa.add(aux)
    cartas.remove(aux)

  return cartasmesa




if __name__ == '__main__':
  pantalla=tkinter.Tk()
  pantalla.geometry("700x700")
  pantalla.title("TEXAS HOLD'EM")
  pantalla.resizable(False,False)
  pantalla.config(cursor="cross")
  pantalla.config(bg="#93032E")

  scre=Screen.Screen(master=pantalla)
  scre.inicio()
  scre.mainloop()