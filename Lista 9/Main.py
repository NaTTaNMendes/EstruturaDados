from NoArvoreBinaria import NoArvoreBinaria
from ArvoreBinariaBusca import ArvoreBinariaBusca

arvore = ArvoreBinariaBusca()
arvore.insere(5)
arvore.insere(3)
arvore.insere(8)
arvore.insere(2)
arvore.insere(4)
arvore.insere(7)
arvore.insere(9)
arvore.insere(1)
arvore.insere(6)
arvore.insere(10)
arvore.insere(11)

# Testando a função toString
arvore_string = arvore.toString()
print('Imprimindo árvore')
print(arvore_string)  # Imprime a representação em ordem crescente da árvore

# Testando a função busca
print('Procurando o 4')
no_encontrado = arvore.busca(4)
if no_encontrado is not None:
    print("Nó encontrado:", no_encontrado.getInfo())  # Imprime: Nó encontrado: 4
else:
    print("Nó não encontrado")

# Testando a função retira
arvore.retira(6)
print('Retirando o 6')
print(arvore.toString())  # Imprime a árvore modificada

# Testando a função imprimePre
print('Imprimindo árvore')
pre_ordem = arvore.imprimePre(arvore.raiz)
print(pre_ordem)  # Imprime a representação pré-ordem da árvore

# Testando a função somaFolhas
soma_folhas = arvore.somaFolhas()
print("Soma das folhas:", soma_folhas)  # Imprime a soma das folhas da árvore

# Testando a função maioresX
num_maiores = arvore.maioresX(5)
print("Quantidade de nós maiores que 5:", num_maiores)  # Imprime a quantidade de nós maiores que 5 na árvore