class MakeSeries():
    def __init__(self):
        self.serie = [(0,1), (1,1)]
    def makeSerie(self, n:int):
        for i in range(0, n-1): 
            self.iteracionSerie(n)
    def iteracionSerie(self, n:int):
        tmp = self.serie
        for i in range(0, len(self.serie)):
            numerador = self.serie[i][0] + self.serie[i+1][0]
            denominador = self.serie[i][1] + self.serie[i+1][1]
            if numerador/denominador < 1 and numerador <= n and denominador <= n: 
                tmp.insert(i+1,(numerador, denominador))
        self.serie = tmp
    def reiniciarLista(self):
        self.serie = [(0,1),(1,1)]
