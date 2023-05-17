from NoArvore import NoArvore

class Arvore:
    
    def __init__(self):
        self.raiz = None
    
    def vazia(self):
        return self.raiz == None
    
    def insere(self, valor, filhos):
        nova_arvore = NoArvore(valor, filhos)
        self.raiz = nova_arvore
        return nova_arvore

    def imprimePre(self, nodo):
        saida = ""
        saida += "<"

        if (nodo != None):
            saida += ' ' + str(nodo.informacao) + ' '
            for filho in nodo.filhos:
                saida += self.imprimePre(filho)

        saida += ">"
        
        return saida
    
    def pertence(self, nodo):
        return self.pertenceAux(self.raiz, nodo)

    def pertenceAux(self, raiz, nodo):
        resultado = False
        
        if nodo == raiz.informacao:
            resultado = True

        for filho in raiz.filhos:
            resultado = resultado or self.pertenceAux(filho, nodo)

        return resultado

    def altura(self):
        return self.alturaAux(self.raiz)
        
    def alturaAux(self, nodo):
        if nodo == None:
            return 0
                
        resultado = 0
        for filho in nodo.filhos:            
            resultado = max(resultado, self.alturaAux(filho))
            
        return resultado + 1
    
    def pares(self):
        return self.paresAux(self.raiz)
    
    def paresAux(self, nodo):
        contagem = 0
        
        if (nodo.informacao % 2) == 0:
            contagem += 1

        for filho in nodo.filhos:
            contagem += self.paresAux(filho)

        return contagem
    
    def folhas(self):
        return self.folhasAux(self.raiz)
    
    def folhasAux(self, nodo):
        if not nodo.filhos:
            return 1
            
        contagem = 0
        for filho in nodo.filhos:
            contagem += self.folhasAux(filho)

        return contagem

    def igual(self, arvore):
        if self.quantidadeItens() != arvore.quantidadeItens():
            return False        
        return self.igualAux(self.raiz, arvore.raiz)
    
    def igualAux(self, arvoreAtual, arvoreEstrangeira):
        
        if (arvoreAtual.informacao != arvoreEstrangeira.informacao):
            return False
        
        for index, filho in enumerate(arvoreAtual.filhos):
            if not self.igualAux(arvoreAtual.filhos[index], arvoreEstrangeira.filhos[index]):
                return False
        
        return True

    def quantidadeItens(self):
        return self.quantidadeItensAux(self.raiz)        
    
    def quantidadeItensAux(self, arvore):
        if arvore is None:
            return 0
        count = 1  
        for filho in arvore.filhos:
            count += self.quantidadeItensAux(filho) 
        return count
    
    def copia(self):
        raiz = self.copiaAux(self.raiz)
        retorno = Arvore()
        retorno.insere(raiz.informacao, raiz.filhos)
        return retorno
    
    def copiaAux(self, nodo):    
        
        novos_nodos = []
        for filho in nodo.filhos:
            novo_nodo = self.copiaAux(filho)
            novos_nodos.append(novo_nodo)
        
        return NoArvore(nodo.informacao, novos_nodos)
    
    def __str__(self):
        return self.imprimePre(self.raiz)