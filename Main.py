__name__="__main__"

import tkinter

import Partida
import jugada
from tkinter import *
import Screen
import Carta






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