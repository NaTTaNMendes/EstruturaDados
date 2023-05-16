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
    
    def __str__(self):
        return self.imprimePre(self.raiz)