from tkinter import *
from tkinter import messagebox


class Screen(Frame):
    def __init__(self, master):

        super().__init__(master)
        self.parent = master
        self.place(x=self.parent.winfo_width() / 2, y=self.parent.winfo_height()/3)

        self["bg"]=master["bg"]
        self.pack(fill="none", expand=True)


    def inicio(self):
        self.preguntainicio = Label(self, font=("Arial", 24), relief=RAISED,bg=self.parent["bg"], fg='#C69F89', borderwidth=0)
        self.preguntainicio["text"] = "HOLA! QUIERES JUGAR AL TEXAS HOLDEM?"
        self.botonsi = Button(self, font=("Arial", 12), bg=self.parent["bg"], fg=self.preguntainicio["fg"], text="SI", highlightbackground='red',
                              command=lambda: self.sustituirtexto(self.preguntainicio, "Has selecionado si"))
        self.preguntainicio.place(x=self.parent.winfo_width() / 2, y=self.parent.winfo_height()/3)

        self.preguntainicio.pack()

        self.botonsi.pack()

    def sustituirtexto(self, objeto, nuevotexto):
        if type(objeto) is Label:
            objeto["text"] = nuevotexto
        else:
            objeto.delete(0, END)
            objeto.insert(INSERT, nuevotexto)
