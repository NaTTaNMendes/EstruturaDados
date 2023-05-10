from NoArvoreBinaria import NoArvoreBinaria

class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def vazia(self):
        return self.raiz == None
    
    def insere(self, valor, esq, dir):
        nova_arvore = NoArvoreBinaria(valor, esq, dir)
        self.raiz = nova_arvore
        return nova_arvore

    def pertence(self, info):
        return self.pertenceAux(self.raiz, info)               
    
    def pertenceAux(self, nodo, info):
        if nodo == None:
            return False
        else:
            return ((nodo.getInfo() == info) or (self.pertenceAux(nodo.getSae(), info)) or (self.pertenceAux(nodo.getSad(), info)))

    def altura(self):
        if self.vazia():
            return 0
        return self.raiz.alturaAux(self.raiz) 
    
    def folhas(self):
        if self.vazia():
            return 0
        return self.raiz.folhasAux(self.raiz) 
    
    def pares(self):
        if self.vazia():
            return 0
        return self.raiz.paresAux(self.raiz)
    
    def numNos(self):
        if self.vazia():
            return 0
        return self.raiz.numNosAux(self.raiz)   

    def imprimePre(self, nodo):
        saida = ""
        saida += "<"
        if (nodo != None):
            saida += str(nodo.getInfo())
            saida += self.imprimePre(nodo.getSae())
            saida += self.imprimePre(nodo.getSad())
        saida += ">"
        return saida

    def __str__(self):
        return self.imprimePre(self.raiz)