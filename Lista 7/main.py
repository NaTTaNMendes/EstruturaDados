from Arvore import Arvore
from NoArvore import NoArvore

arvore = Arvore()

no_7 = NoArvore(7, [])
no_6 = NoArvore(6, [])
no_5 = NoArvore(5, [])
no_4 = NoArvore(4, [no_5, no_6])
no_3 = NoArvore(3, [])
no_2 = NoArvore(2, [no_7])
no_1 = NoArvore(1, [no_2, no_3, no_4])

arvore.insere(no_1.informacao, no_1.filhos)

print(arvore)
print(arvore.pertence(4))
print(arvore.altura())
print(arvore.pares())