from NoLista import NoLista

class Lista:
    
    def __init__(self):
        self.primeiro = NoLista(None, None)
    
    def insere(self, valor):
        novo_valor = NoLista(valor, None)
        if self.primeiro.getInfo() == None:
            self.primeiro = novo_valor
            return
        
        nodo = self.primeiro
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
        
        nodo.setProx(novo_valor)
    
    def imprime(self):
        saida = "["
        inicio = self.primeiro
        
        while (inicio.getProx() != None):
            saida = saida + str(inicio.getInfo()) + ", "
            inicio = inicio.getProx()
        
        saida = saida + str(inicio.getInfo()) + "]"
        
        print(saida)
    
    def vazia(self):
        if self.primeiro.getInfo() == None:
            return True
        return False

    def busca(self, valor):
        nodo = self.primeiro
        while (nodo.getProx() != None):
            if nodo.getInfo() == valor:
                return nodo
            nodo = nodo.getProx()
        return None
        
    def comprimento(self):
        tamanho = 0
        
        nodo = self.primeiro
        while (nodo.getInfo() != None):
            tamanho = tamanho + 1
            nodo = nodo.getProx()
            if nodo == None:
                return tamanho
        else:
            return tamanho
    
    def ultimo(self):
        nodo = self.primeiro
        
        if nodo == None:
            return None
        
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
        return nodo
        
        