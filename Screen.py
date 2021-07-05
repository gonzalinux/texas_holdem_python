import tkinter
import random
import pathlib
from tkinter import *
from tkinter import messagebox
from Jugador import Jugador
import time
import Jugadas
from Carta import Carta
from PIL import ImageTk, Image

nombres = ["Knekro", "Politécnico", "Mandarino", "Patato", "Guacamole", "Yutask", "Alet", "UwU", "Rayo", "Francesco",
           "Xafer", "Jean", "Mr"]
apellidos = ["el Capo", "", "", "Politécnico", "The fallen", "Son of udyr", "Sugar Daddy", "the emo", "7u7",
             "Quchau", "Virgolini", "tilted", "sinonimo de gilipollas", "De Arco", "Descole"]
apodos = ["\"El tonto\"", "", "", "", "", "", "", '"el tikismikis"', '"el tercero del mundo"', '"el moñas"']
path=str(pathlib.Path(__file__).parent.absolute())

class Screen(Frame):
    def __init__(self, master):
        self.probabilidadapuesta = 0.2
        super().__init__(master)
        self.parent = master
        self.callback = self.fase3cartas
        self.player = Jugador(1000, "", None)
        self.maquina = Jugador(1000, self.getRandomName(), None)
        # if random.random()< 0.5:
        self.player.apuesta = 5
        # else:
        #    self.maquina.apuesta=5
        self.place(x=self.parent.winfo_width() / 2, y=self.parent.winfo_height() / 3)
        self.place(relwidth=1, relheight=1)
        self["bg"] = master["bg"]
        self.pack(fill="none", expand=True)
        self.tienenombre = False

    def clear_frame(self):
        for widgets in self.parent.winfo_children():
            widgets.destroy()

    def inicio(self):
        self.preguntainicio = Label(self, font=("Arial", 24), relief=RAISED, bg=self.parent["bg"], fg='#C69F89',
                                    borderwidth=0)
        self.preguntainicio["text"] = "HOLA! QUIERES JUGAR AL TEXAS HOLDEM?"
        self.botonsi = Button(self, font=("Arial", 12), bg=self.parent["bg"], fg=self.preguntainicio["fg"], text="SI",
                              highlightbackground='red',
                              command=lambda: self.selecionasi())
        self.preguntainicio.place(x=self.parent.winfo_width() / 2, y=self.parent.winfo_height() / 3)

        self.preguntainicio.pack()

        self.botonsi.pack()

    def sustituirtexto(self, objeto, nuevotexto):
        if type(objeto) is Label:
            objeto["text"] = nuevotexto
        else:
            objeto.delete(0, END)
            objeto.insert(INSERT, nuevotexto)

    def selecionasi(self):
        if not self.tienenombre:
            self.sustituirtexto(self.preguntainicio, "Introduce tu nombre")
            self.botonsi.pack_forget()
            self.introduceName = Entry(self, font=("Arial", 20), text=self.getRandomName(), bg="white", width=200)
            self.introduceName.pack()
            self.introduceName.bind('<Return>', lambda e: self.selecionasi())
            self.botonsi["text"] = "Aceptar"
            self.botonsi.pack()

            self.tienenombre = True

            return
        self.player.nombre = self.introduceName.get()
        self.clear_frame()
        pantalla = self.parent
        pantalla.geometry("1000x800")
        pantalla.title("Juego en curso")
        pantalla.resizable(False, False)
        pantalla.config(cursor="cross")
        pantalla.config(bg="white")
        for i in range(18):
            self.parent.columnconfigure(i, minsize=50)
            self.parent.columnconfigure(i, weight=1)
        for i in range(6):
            self.parent.rowconfigure(i, minsize=150)
            self.parent.columnconfigure(i, weight=1)

        self.frameNombreMaquina = Frame(pantalla)
        self.frameNombreMaquina["bg"] = "red"
        self.frameNombreMaquina.place(width=700, height=300)
        self.nombreMaquina = Label(self.frameNombreMaquina, font=("Arial", 20), relief=RAISED, bg="white",
                                   fg='#C69F89',
                                   borderwidth=0)
        self.nombreMaquina["text"] = self.maquina.nombre
        self.nombreMaquina.pack(fill=BOTH)
        self.frameNombreMaquina.grid(row=0, column=2, columnspan=15)

        self.imagenpoker = Image.open(path+"\\assets\\ficha_negra.png")
        self.imagenpoker = self.imagenpoker.resize((100, 100))
        self.imagenpoker = ImageTk.PhotoImage(self.imagenpoker)
        self.canvasApuestaMaquina = Canvas(pantalla, bg="white", width=100, height=100, borderwidth=0,
                                           highlightthickness=0)

        self.canvasApuestaMaquina.create_image((0, 0), image=self.imagenpoker, anchor='nw')
        self.idtextApuestaMaquina = self.canvasApuestaMaquina.create_text((50, 50), text=str(self.maquina.apuesta),
                                                                          fill="red",
                                                                          font=("Arial", 16))
        self.canvasApuestaMaquina.grid(row=0, column=0, columnspan=2)
        self.canvasApuestaMaquina.update()
        self.canvasFichasMaquina = Canvas(pantalla, bg="white", width=100, height=100, highlightthickness=0)
        self.canvasFichasMaquina.create_image((0, 0), image=self.imagenpoker, anchor='nw')
        self.idtextFichasMaquina = self.canvasFichasMaquina.create_text((50, 50), text=str(self.maquina.fichas),
                                                                        fill="green", font=("Arial", 16))
        self.canvasFichasMaquina.grid(row=0, column=17, columnspan=2)

        self.frameCartas = Frame(pantalla)

        self.frameCartas.place(width=1000, height=300)
        # self.frameCartas.grid_propagate(False)
        for i in range(10):
            self.frameCartas.columnconfigure(i, minsize=50)

        self.frameCartas.grid(column=0, row=1, rowspan=3, columnspan=18, sticky="nsew")
        self.cartasMaquinaCanvases = [Canvas(self.frameCartas, bg="red", width="100", height=150),
                                      Canvas(self.frameCartas, bg="red", width="100", height=150)]
        var = 6
        for i in self.cartasMaquinaCanvases:
            i.grid(row=0, column=var, columnspan=2, padx=20)
            var += 2

        self.cartasMesaCanvases = [Canvas(self.frameCartas, bg="red", width="100", height=150) for b in range(5)]
        var = 3
        for i in self.cartasMesaCanvases:
            i.grid(row=1, column=var, columnspan=2, padx=20)
            var += 2

        self.cartasPlayerCanvases = [Canvas(self.frameCartas, bg="red", width="100", height=150),
                                     Canvas(self.frameCartas, bg="red", width="100", height=150)]
        var = 6
        for i in self.cartasPlayerCanvases:
            i.grid(row=2, column=var, columnspan=2, padx=20)
            var += 2

        self.frameNombrePlayer = Frame(pantalla)
        self.frameNombrePlayer["bg"] = "red"
        self.frameNombrePlayer.place(width=700, height=300)
        self.nombrePlayer = Label(self.frameNombrePlayer, font=("Arial", 20, "bold"), relief=RAISED, bg="white",
                                  fg='#C69F89',
                                  borderwidth=0)

        self.nombrePlayer["text"] = self.player.nombre
        self.nombrePlayer.pack(fill=BOTH)
        self.frameNombrePlayer.grid(row=4, column=2, columnspan=15)

        self.canvasApuestaPlayer = Canvas(pantalla, bg="white", width=100, height=100, borderwidth=0,
                                          highlightthickness=0)

        self.canvasApuestaPlayer.create_image((0, 0), image=self.imagenpoker, anchor='nw')
        self.idtextApuestaPlayer = self.canvasApuestaPlayer.create_text((50, 50), text=str(self.player.apuesta),
                                                                        fill="red",
                                                                        font=("Arial", 16))
        self.canvasApuestaPlayer.grid(row=4, column=0, columnspan=2)
        self.canvasApuestaPlayer.update()
        self.canvasFichasPlayer = Canvas(pantalla, bg="white", width=100, height=100, highlightthickness=0)
        self.canvasFichasPlayer.create_image((0, 0), image=self.imagenpoker, anchor='nw')
        self.idtextFichasPlayer = self.canvasFichasPlayer.create_text((50, 50), text=str(self.player.fichas),
                                                                      fill="green", font=("Arial", 16))
        self.canvasFichasPlayer.grid(row=4, column=17, columnspan=2)
        self.iniciaJuego()

        self.imagenesCartasPlayer = []
        self.mostrarCartas(self.cartasPlayerCanvases, self.player.cartas, 2, self.imagenesCartasPlayer)

        self.imagenesCartasMesa = []
        self.imagenesCartasMaquina = []

        self.parent.after(2000, lambda: prueba())

        def prueba():
            self.faseCiega()

    def iniciaJuego(self):
        self.baraja = []
        for i in range(0, 4):
            for j in range(1, 13):
                self.baraja.append(Carta(j, i))
        self.cartasmesa = self.sacar_cartas(5)
        self.player.cartas = self.sacar_cartas(2)
        self.maquina.cartas = self.sacar_cartas(2)

    def sacar_cartas(self, numeroasacar):

        cartasmesa = set()
        while len(cartasmesa) != numeroasacar:
            aux = self.baraja[random.randint(0, len(self.baraja) - 1)]
            cartasmesa.add(aux)
            self.baraja.remove(aux)

        return list(cartasmesa)

    def getRandomName(self):
        return nombres[random.randint(0, len(nombres) - 1)] + " " + apodos[random.randint(0, len(apodos) - 1)] + " " + \
               apellidos[random.randint(0, len(apellidos) - 1)]

    def subirApuestaMaquina(self):
        numero = random.random()
        prob = self.probabilidadapuesta + (0.2 * Jugadas.jugada_ganadora(self.cartasmesa, self.maquina.cartas)[0])
        print(numero)
        print(prob)
        if numero < prob:

            cantidadSubir = self.player.apuesta - self.maquina.apuesta
            if numero > self.probabilidadapuesta:
                cantidadSubir = cantidadSubir + 5 * round(10 * (prob + 0.1))
            if cantidadSubir > self.maquina.fichas:
                cantidadSubir = self.maquina.fichas
            self.maquina.apuesta += cantidadSubir
            self.canvasApuestaMaquina.itemconfig(self.idtextApuestaMaquina, text=self.maquina.apuesta)

            self.maquina.fichas -= cantidadSubir
            self.canvasFichasMaquina.itemconfig(self.idtextFichasMaquina, text=self.maquina.fichas)
        else:
            self.ganaElPlayer()

    def subirApuestaPlayer(self, cantidad):

        if self.maquina.apuesta > (self.player.apuesta + cantidad):
            cantidad = self.maquina.apuesta - self.player.apuesta
        if cantidad > self.player.fichas:
            cantidad = self.player.fichas
        self.player.apuesta += cantidad
        self.player.fichas -= cantidad
        self.canvasApuestaPlayer.itemconfig(self.idtextApuestaPlayer, text=self.player.apuesta)
        self.canvasFichasPlayer.itemconfig(self.idtextFichasPlayer, text=self.player.fichas)

    def ganaElPlayer(self):
        self.parent["bg"] = "green"

    def mostrarCartas(self, arraycanvas, arraycartas, num, listimagenes):
        listimagenes.clear()
        for i in range(num):
            arraycanvas[i]["bg"] = "white"
            arraycanvas[i].create_text((50, 30), text=arraycartas[i].numeroescrito,
                                       font=("Arial", 24),
                                       fill=arraycartas[i].color)
            listimagenes.append(Image.open(path+arraycartas[i].imgpalo))
            listimagenes[i] = listimagenes[i].resize((50, 50))
            listimagenes[i] = ImageTk.PhotoImage(listimagenes[i])
            arraycanvas[i].create_image((25, 75), image=listimagenes[i], anchor='nw')

    def faseCiega(self):
        self.frameApuesta = Frame(self.parent)
        self.frameApuesta.grid(column=1, row=3, rowspan=2, columnspan=4, sticky="nw")
        self.labelApuesta = Label(self.frameApuesta, text="APUESTA", font=("Arial", 25))
        self.imagenFlechaArriba = Image.open(path+"\\assets\\f_arriba.png")
        self.imagenFlechaArriba = self.imagenFlechaArriba.resize((50, 50))
        self.imagenFlechaArriba = ImageTk.PhotoImage(self.imagenFlechaArriba)

        self.imagenFlechaArribaOn = Image.open(path+"\\assets\\f_arriba_on.png")
        self.imagenFlechaArribaOn = self.imagenFlechaArribaOn.resize((50, 50))
        self.imagenFlechaArribaOn = ImageTk.PhotoImage(self.imagenFlechaArribaOn)
        self.botonsubir = Label(self.frameApuesta, image=self.imagenFlechaArriba)
        self.imagenFlechaAbajo = Image.open(path+"\\assets\\f_abajo.png")
        self.imagenFlechaAbajo = self.imagenFlechaAbajo.resize((50, 50))
        self.imagenFlechaAbajo = ImageTk.PhotoImage(self.imagenFlechaAbajo)
        self.imagenFlechaAbajoOn = Image.open(path+"\\assets\\f_abajo_on.png")
        self.imagenFlechaAbajoOn = self.imagenFlechaAbajoOn.resize((50, 50))
        self.imagenFlechaAbajoOn = ImageTk.PhotoImage(self.imagenFlechaAbajoOn)

        self.imagenTick = Image.open(path+"\\assets\\tick.png")
        self.imagenTick = self.imagenTick.resize((50, 50))
        self.imagenTick = ImageTk.PhotoImage(self.imagenTick)

        self.imagenTickOn = Image.open(path+"\\assets\\tick.png")
        self.imagenTickOn = self.imagenTickOn.resize((50, 50))
        self.imagenTickOn = ImageTk.PhotoImage(self.imagenTickOn)
        self.imagenCruz = Image.open(path+"\\assets\\cruz.png")
        self.imagenCruz = self.imagenCruz.resize((50, 50))
        self.imagenCruz = ImageTk.PhotoImage(self.imagenCruz)
        self.imagenCruzOn = Image.open(path+"\\assets\\cruz_on.png")
        self.imagenCruzOn = self.imagenCruzOn.resize((50, 50))
        self.imagenCruzOn = ImageTk.PhotoImage(self.imagenCruzOn)

        self.botonbajar = Label(self.frameApuesta, image=self.imagenFlechaAbajo)
        self.botonAceptar = Label(self.frameApuesta, image=self.imagenTick)
        self.botonCancelar = Label(self.frameApuesta, image=self.imagenCruz)

        self.botonsubir.bind("<Button-1>", lambda e: self.iluminarbotonsubir())
        self.botonbajar.bind("<Button-1>", lambda e: self.iluminarbotonbajar())
        self.botonCancelar.bind("<Button-1>", lambda e: self.iluminarbotoncanc())
        self.botonAceptar.bind("<Button-1>", lambda e: self.iluminarbotonacept())
        self.labelApuesta.pack(side="top", anchor=NW)
        self.botonsubir.pack(side="left")
        self.botonbajar.pack(side="left")
        self.botonAceptar.pack(side=LEFT)
        self.botonCancelar.pack(side=LEFT)

    def pierdeElPlayer(self, razon):
        self.frameHasPerdido = Frame(self.parent, bg="red")
        self.labelHasPerdido = Label(self.frameHasPerdido, text="HAS PERDIDO", font=("Arial", 40), fg="black",
                                     bg=self.frameHasPerdido["bg"])
        self.labelexplica = Label(self.frameHasPerdido, text=razon, font=("Arial", 30), fg="black",
                                  bg=self.frameHasPerdido["bg"])
        self.frameHasPerdido.grid(column=0, row=0, columnspan=18, rowspan=6, sticky="news")
        self.labelHasPerdido.pack(expand=True, fill=BOTH)
        self.labelexplica.pack(expand=True, fill=BOTH)

    def apuesta(self):
        if self.player.apuesta < self.maquina.apuesta:
            self.error = Label(self.parent, text="No puedes apostar menos que el rival", font=("Arial", 20, 'bold'),
                               fg="red")
            self.error.grid(column=6, row=3, columnspan=10)
            self.error.after(500, lambda: self.error.grid_forget())
            return
        if self.player.apuesta == self.maquina.apuesta:
            self.callback()
            return
        antes = self.maquina.apuesta
        self.subirApuestaMaquina()
        if antes == self.maquina.apuesta:
            self.callback()

    def iluminarbotonacept(self):
        self.apuesta()
        self.botonAceptar["image"] = self.imagenTickOn
        self.botonAceptar.after(400, lambda: self.botonAceptar.config(image=self.imagenTick))

    def iluminarbotonsubir(self):
        self.subirApuestaPlayer(5)
        self.botonsubir["image"] = self.imagenFlechaArribaOn
        self.botonsubir.after(400, lambda: self.botonsubir.config(image=self.imagenFlechaArriba))

    def iluminarbotonbajar(self):
        self.subirApuestaPlayer(-5)
        self.botonbajar["image"] = self.imagenFlechaAbajoOn
        self.botonbajar.after(400, lambda: self.botonbajar.config(image=self.imagenFlechaAbajo))

    def iluminarbotoncanc(self):
        self.pierdeElPlayer("Te has retirado")
        self.botonCancelar["image"] = self.imagenCruzOn
        self.botonCancelar.after(400, lambda: self.botonCancelar.config(image=self.imagenCruz))

    def fase3cartas(self):
        self.subirApuestaMaquina()
        self.mostrarCartas(self.cartasMesaCanvases, self.cartasmesa, 3, self.imagenesCartasMesa)
        self.callback = self.fase4cartas

    def fase4cartas(self):
        self.subirApuestaMaquina()
        self.mostrarCartas(self.cartasMesaCanvases, self.cartasmesa, 4, self.imagenesCartasMesa)
        self.callback = self.fase5cartas

    def fase5cartas(self):

        self.subirApuestaMaquina()
        self.mostrarCartas(self.cartasMesaCanvases, self.cartasmesa, 5, self.imagenesCartasMesa)
        self.callback = self.termina

    def termina(self):
        print("termina")
        self.mostrarCartas(self.cartasMaquinaCanvases, self.maquina.cartas, 2, self.imagenesCartasMaquina)

        puntuacionMquina = Jugadas.jugada_ganadora(self.cartasmesa, self.maquina.cartas)
        puntuacionJugador = Jugadas.jugada_ganadora(self.cartasmesa, self.player.cartas)

        if puntuacionJugador[0] > puntuacionMquina[0]:
            self.ganaElPlayer()
        elif puntuacionMquina[0] > puntuacionJugador[0]:
            self.pierdeElPlayer(
                "tiene la puntuacion mas baja " + str(puntuacionJugador[0]) + " comparada a la maquina " + str(
                    puntuacionMquina[0]))
        elif puntuacionMquina[1].numero > puntuacionJugador[1].numero:
            self.pierdeElPlayer(
                "tiene la carta mas baja " + str(puntuacionJugador[1].encadena) + " comparada a la maquina " + str(
                    puntuacionMquina[1].encadena))
        elif puntuacionMquina[1].numero < puntuacionJugador[1].numero:
            self.ganaElPlayer()
