class NoArvoreBinaria:
    
    def __init__(self, info):
        self.info = info
    
    def __init__(self, info, esq, dir):
        self.info = info
        self.esq = esq
        self.dir = dir
        
    def setInfo(self, info):
        self.info = info
    
    def getInfo(self):
        return self.info

    def setSae(self, esq):
        self.esq = esq
        
    def getSae(self):
        return self.esq

    def setSad(self, dir):
        self.dir = dir
    
    def getSad(self):
        return self.dir
    
    def imprimir(self, nodo):
        if self.info == None:
            return ""
        saida = ""
        saida += self.info + " "
        saida += self.imprimir(nodo.esq)
        saida += self.imprimir(nodo.dir)
        return saida