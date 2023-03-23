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
        if self.primeiro == None:
            print("None")
            return
        
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
        if nodo.getInfo() == valor:
            return nodo
        else:
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

    def retira(self, valor):
        if self.vazia():
            return
        if self.busca(valor) == None:
            return
        
        nodo = self.primeiro
        anterior = None

        while (True):
            if nodo == None:
                anterior.setProx(None)
            
            if nodo.getInfo() == valor:
                if anterior == None:
                    self.primeiro = self.primeiro.getProx()
                    return
                else:
                    anterior.setProx(nodo.getProx())
                    return

            if nodo.getProx() != None:
                anterior = nodo         
            nodo = nodo.getProx()
    
    def libera(self):
        self.primeiro = None

    def insereFim(self, valor):
        novo_valor = NoLista(valor, None)
        final = self.ultimo()
        if final == None:
            self.primeiro = self.primeiro = novo_valor
            return
        final.setProx(novo_valor)

    def igual(self, lista):
        nodoListaEstrangeira = lista.primeiro
        nodoListaAtual = self.primeiro
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