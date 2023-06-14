from NoArvoreBinaria import NoArvoreBinaria


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def busca(self, v):
        return self.busca_recursiva(self.raiz, v)

    def busca_recursiva(self, a, v):
        if a is None or a.info == v:
            return a
        if v < a.info:
            return self.busca_recursiva(a.esq, v)
        else:
            return self.busca_recursiva(a.dir, v)

    def insere(self, v):
        self.raiz = self.insere_recursiva(self.raiz, v)

    def insere_recursiva(self, a, v):
        if a is None:
            novo_no = NoArvoreBinaria(v)
            return novo_no
        if v < a.info:
            a.esq = self.insere_recursiva(a.esq, v)
        else:
            a.dir = self.insere_recursiva(a.dir, v)
        return a

    def retira(self, v):
        self.raiz = self.retira_recursiva(self.raiz, v)

    def retira_recursiva(self, a, v):
        if a is None:
            return a
        if v < a.info:
            a.esq = self.retira_recursiva(a.esq, v)
        elif v > a.info:
            a.dir = self.retira_recursiva(a.dir, v)
        else:
            if a.esq is None:
                return a.dir
            elif a.dir is None:
                return a.esq
            else:
                a.info = self.menor_valor(a.dir)
                a.dir = self.retira_recursiva(a.dir, a.info)
        return a

    def menor_valor(self, a):
        while a.esq is not None:
            a = a.esq
        return a.info
    
    def somaFolhas(self):
        return self.somaFolhasRecursivo(self.raiz)

    def somaFolhasRecursivo(self, no):
        if no is None:
            return 0
        
        if no.esq is None and no.dir is None:
            return no.info
        
        return self.somaFolhasRecursivo(no.esq) + self.somaFolhasRecursivo(no.dir)

    def maioresX(self, x):
        return self.maioresXRecursivo(self.raiz, x)

    def maioresXRecursivo(self, no, x):
        if no is None:
            return 0
        
        count = 0

        if no.info > x:
            count += 1

        count += self.maioresXRecursivo(no.esq, x)
        count += self.maioresXRecursivo(no.dir, x)

        return count

    def toString(self):
        return self.imprimePre(self.raiz)

    def imprimePre(self, nodo):
        saida = ""
        saida += "<"

        if nodo is not None:
            saida += ' ' + str(nodo.info) + ' '
            if nodo.esq is not None:
                saida += self.imprimePre(nodo.esq)
            if nodo.dir is not None:
                saida += self.imprimePre(nodo.dir)

        saida += ">"

        return saida