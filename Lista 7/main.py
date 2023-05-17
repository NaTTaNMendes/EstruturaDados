from Arvore import Arvore
from NoArvore import NoArvore

arvore = Arvore()
arvore2 = Arvore()

no_7 = NoArvore(7, [])
no_6 = NoArvore(6, [])
no_5 = NoArvore(5, [])
no_4 = NoArvore(4, [no_5, no_6])
no_3 = NoArvore(3, [])
no_2 = NoArvore(2, [no_7])
no_1 = NoArvore(1, [no_2, no_3, no_4])

no_7a = NoArvore(7, [])
no_6a = NoArvore(6, [])
no_5a = NoArvore(5, [])
no_4a = NoArvore(4, [no_5a, no_6a])
no_3a = NoArvore(3, [])
no_2a = NoArvore(2, [no_7a])
no_1a = NoArvore(1, [no_2a, no_3a, no_4a])

arvore.insere(no_1.informacao, no_1.filhos)
arvore2.insere(no_1a.informacao, no_1a.filhos)

print(arvore)
print(arvore.pertence(4))
print(arvore.altura())
print(arvore.pares())
print(arvore.folhas())
print(arvore.quantidadeItens())
print(arvore.igual(arvore2))
arvore2 = arvore.copia()
print(arvore2)
