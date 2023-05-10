class NoArvoreBinaria:
    
    def __init__(self, info, esq, dir):
        self.info = info
        self.esq = None
        self.dir = None

        if esq != None:
            self.esq = esq

        if dir != None:
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
    
    def alturaAux(self, nodo):
        if nodo == None:
            return 0
        return 1 + max(nodo.alturaAux(nodo.getSae()), nodo.alturaAux(nodo.getSad()))

    def folhasAux(self, nodo):
        if ((nodo.getSae() == None) and (nodo.getSad() == None)):
            return 1
        return nodo.numNosAux(nodo.getSae()) + nodo.numNosAux(nodo.getSad())
    
    def numNosAux(self, nodo):
        if nodo == None:
            return 0
        return 1 + nodo.numNosAux(nodo.getSae()) + nodo.numNosAux(nodo.getSad())
    
    def paresAux(self, nodo):
        if nodo == None:
            return 0
        if ((nodo.getInfo() % 2) == 0):
            return 1 + nodo.paresAux(nodo.getSae()) + nodo.paresAux(nodo.getSad())
        else:
           return nodo.paresAux(nodo.getSae()) + nodo.paresAux(nodo.getSad()) 
    
    def imprimir(self, nodo):
        if self.info == None:
            return ""
        saida = ""
        saida += str(self.info) + " "
        saida += self.imprimir(nodo.esq)
        saida += self.imprimir(nodo.dir)
        return saida