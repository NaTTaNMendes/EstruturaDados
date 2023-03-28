from NoListaDupla import NoListaDupla

class ListaDupla:
    def __init__(self):
        self.prim = NoListaDupla(None, None, None)
    
    def insere(self, v):
        novoValor = NoListaDupla(v, None, None)
        if self.prim.getInfo() == None:
            self.prim = novoValor
            return
        nodo = self.prim
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
        
        nodo.setProx(novoValor)
        novoValor.setAnt(nodo)
    
    def imprime(self):
        saida = '['
        
        nodo = self.prim
        while (nodo.getProx() != None):
            saida = saida + str(nodo.getInfo()) + ','
            nodo = nodo.getProx()
        if nodo.getInfo() != None:
            saida = saida + str(nodo.getInfo()) + ']'
            return saida
        return '[]'
        
    def vazia(self):
        if self.prim.getInfo() == None:
            return True
        return False

    def busca(self, v):
        if self.prim.getInfo() == v:
            return self.prim
        nodo = self.prim
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
            if nodo.getInfo() == v:
                return nodo
    
    def comprimento(self):
        if self.prim.getInfo() == None:
            return 0
        
        comp = 1        
        nodo = self.prim
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
            comp += 1
        return comp
        
    def ultimo(self):
        nodo = self.prim
        while (nodo.getProx() != None):
            nodo = nodo.getProx()
        return nodo
    
    def retira(self, v):
        if self.prim.getInfo() == v:
            self.prim = self.prim.getProx()
            self.prim.setAnt(None)
            return 
        proximo = None
        atual = self.prim
        anterior = atual
        while (atual.getProx() != None):
            anterior = atual
            atual = atual.getProx()
            if atual.getInfo() == v:
                proximo = atual.getProx()
                anterior.setProx(proximo)
                if proximo != None:
                    proximo.setAnt(anterior)
                return
    
    def libera(self):
        self.prim = NoListaDupla(None, None, None)

    def insereFim(self, v):
        if self.vazia():
            self.prim = NoListaDupla(v, None, None)
            return
        ultimo = self.ultimo()
        novoValor = NoListaDupla(v, ultimo.getAnt(), None)
        ultimo.setProx(novoValor)
        
    def igual(self, lista):
        nodoListaEstrangeira = lista.prim
        nodoListaAtual = self.prim
        while True:
            if (nodoListaAtual == None): 
                if (nodoListaEstrangeira == None):
                    return True
                else:
                    return False
            
            if (nodoListaEstrangeira == None): 
                if (nodoListaAtual == None):
                    return True
                else:
                    return False

            if nodoListaAtual.getInfo() != nodoListaEstrangeira.getInfo():
                return False
            nodoListaAtual = nodoListaAtual.getProx()
            nodoListaEstrangeira = nodoListaEstrangeira.getProx()
    
    def merge(self, lista):
        if lista.prim.getInfo() != None:
            ultimo = self.ultimo()
            ultimo.setProx(lista.prim)
            lista.prim.setAnt(ultimo)
        
        
        
        
       
        
        