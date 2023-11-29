from tkinter import * 
from tkinter import ttk

class Vista():
    def changePoligono(self):
        print("Aqui se debe cambiar la ventana")
    def changePuntosVisibles(self):
        print("Aqui se debe cambiar la ventana")
    def changeTriangulo(self):
        print("Aqui se debe cambiar la ventana")
    def getSucesion(self):
        print("Aqui se debe imprimir la sucesion")
    def __init__(self):
        self.ventana = Tk() #instancia de una ventana 
        self.ventana.title("Sucesiones de Farey")
        self.changeSize(500,300)
        self.frame= ttk.Frame(self.ventana)
        self.makeLabel()
        self.makeBotones()
        self.frame.pack()
        self.ventana.mainloop()
        
    def makeLabel(self):
        #Metodo que genera nuestros reccuadros de texto y los posiciona dentro de nuestra ventana
        self.labelTittle = Label(self.frame, 
                                 text="Sucesiones de Farey", 
                                 font=('Arial', 20, 'bold'))
        self.labelTittle.grid(row = 0, column = 2, columnspan = 2)
        self.labelIngresa = Label(self.frame, 
                                  text="Ingresa la n de tu sucesion", 
                                  font=('Arial', 11))
        self.labelIngresa.grid(row = 1, column = 0, columnspan = 2, sticky='w', padx = 10, pady = 10)
    def makeBotones(self):
        #Metodo que crea los botones y los posiciona dentro de nuestra ventana 
        self.poligonoButton = Button(self.frame, 
                                     text="Poligono de Farey",
                                     command= self.changePoligono, 
                                     font=("Comic Sans",11))
        self.puntosVisiblesButton = Button(self.frame, 
                                     text="Puntos visibles", 
                                     command=self.changePuntosVisibles, 
                                     font=("Comic Sans", 11))
        self.trianguloButton = Button(self.frame, 
                                      text="Triangulo", 
                                      command=self.changeTriangulo, 
                                      font=("Comic Sans", 11))
        self.sucesionButton = Button(self.frame,
                                     text="Obtener Sucesion", 
                                     command=self.getSucesion,
                                     font=("Comic Sans", 11))
        self.poligonoButton.grid(row=2, column = 0, padx = 10, pady=10)
        self.puntosVisiblesButton.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.trianguloButton.grid(row=2, column = 2, padx = 10, pady = 10)
        self.sucesionButton.grid(row=2, column = 3, padx = 10, pady = 10)
        self.poligonoButton.grid(row=2, column = 4, padx = 10, pady = 10)

    def changeSize(self, ventanaX:int, ventanaY:int):
        # Metodo encargado del cambio de tamaño de la ventana 
        # Posiciona la ventana de forma relativa al centro de la pantalla
        posX = round(self.ventana.winfo_screenwidth()/2 - ventanaX/2)
        posY = round(self.ventana.winfo_screenheight()/2 - ventanaY/2)
        self.ventana.geometry(str(ventanaX) + "x" + str(ventanaY) + "+" + str(posX) + "+" + str(posY))


