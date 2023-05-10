from NoArvoreBinaria import NoArvoreBinaria

class NoArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def vazia(self):
        return self.raiz.getInfo() == None
    
    def insere(self, valor, esq, dir):
        nova_arvore = NoArvoreBinaria(valor, esq, dir)
        self.raiz = nova_arvore
        return nova_arvore

    def pertence(self, info):
        return self.pertence(self.raiz, info)
    
    def pertence(self, nodo, info):
        if nodo == None:
            return False
        else:
            return ((nodo.getInfo() == info) or (self.ertence(nodo.getSae(), info)) or (self.pertence(nodo.getSad(), info)))
    
