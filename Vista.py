from tkinter import * 
from tkinter import messagebox
from MakeSeries import MakeSeries

class Vista():
    def changePoligono(self):
        self.frameImagen.config(bg="blue")
        print("Aqui se debe cambiar la ventana")
    def changePuntosVisibles(self):
        self.frameImagen.config(bg="red")
        print("Aqui se debe cambiar la ventana")
    def changeTriangulo(self):
        self.frameImagen.config(bg="green")
        print("Aqui se debe cambiar la ventana")
    def getSucesion(self):
        self.makeSucesion()
        self.var.set(str(self.sucesion))

    def __init__(self):
        self.ventana = Tk() #instancia de una ventana 
        self.ventana.title("Sucesiones de Farey")
        self.changeSize(1000,300)
        self.frameBotones = Frame(self.ventana, height=300)
        self.frameDatos = Frame(self.ventana)
        self.frameImagen = Frame(self.ventana, height=500)
        self.frameImagen.config(bg='black')
        self.sucesion = []
        self.var = StringVar()
        self.var.set("")
        self.makeLabel()
        self.makeEntry()
        self.makeBotones()
        self.frameBotones.pack()
        self.frameDatos.pack()
        self.frameImagen.pack()
        self.ventana.mainloop()
        


    def makeSucesion(self):
        if self.entradaPosicion.get() == "":
            messagebox.showinfo(title="Error", message="Ingresa un numero")
            return
        indice = int(self.entradaPosicion.get())
        makerSucesion = MakeSeries()
        makerSucesion.makeSerie(indice)
        self.sucesion = makerSucesion.serie
        
    def makeLabel(self):
        #Metodo que genera nuestros reccuadros de texto y los posiciona dentro de nuestra ventana
        labelTittle = Label(self.ventana, 
                                 text="Sucesiones de Farey", 
                                 font=('Arial', 20, 'bold'))
        labelTittle.pack()
        labelIngresa = Label(self.frameBotones, 
                                  text="Ingresa la n de tu sucesion", 
                                  font=('Arial', 11))
        labelIngresa.grid(row = 1, column = 0, columnspan = 2, sticky='w', padx = 10, pady = 10)
        labelNumeros = Label(self.frameDatos, 
                             textvariable=self.var, 
                             font=('Arial', 20))
        labelNumeros.pack()
    def makeBotones(self):
        #Metodo que crea los botones y los posiciona dentro de nuestra ventana 
        poligonoButton = Button(self.frameBotones, 
                                     text="Poligono de Farey",
                                     command= self.changePoligono, 
                                     font=("Comic Sans",11))
        puntosVisiblesButton = Button(self.frameBotones, 
                                     text="Puntos visibles", 
                                     command=self.changePuntosVisibles, 
                                     font=("Comic Sans", 11))
        trianguloButton = Button(self.frameBotones, 
                                      text="Triangulo", 
                                      command=self.changeTriangulo, 
                                      font=("Comic Sans", 11))
        sucesionButton = Button(self.frameBotones,
                                     text="Obtener Sucesion", 
                                     command=self.getSucesion,
                                     font=("Comic Sans", 11))
        poligonoButton.grid(row=2, column = 0, padx = 10, pady=10)
        puntosVisiblesButton.grid(row = 2, column = 1, padx = 10, pady = 10)
        trianguloButton.grid(row=2, column = 2, padx = 10, pady = 10)
        sucesionButton.grid(row=2, column = 3, padx = 10, pady = 10)
        poligonoButton.grid(row=2, column = 4, padx = 10, pady = 10)

    def makeEntry(self):
        self.entradaPosicion = Entry(self.frameBotones, text = "Ingresa un numero")
        self.entradaPosicion.grid(row = 1, column = 2, columnspan = 2)
    def changeSize(self, ventanaX:int, ventanaY:int):
        # Metodo encargado del cambio de tamaño de la ventana 
        # Posiciona la ventana de forma relativa al centro de la pantalla
        posX = round(self.ventana.winfo_screenwidth()/2 - ventanaX/2)
        posY = round(self.ventana.winfo_screenheight()/2 - ventanaY/2)
        self.ventana.geometry(str(ventanaX) + "x" + str(ventanaY) + "+" + str(posX) + "+" + str(posY))


