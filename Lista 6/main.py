from ArvoreBinaria import ArvoreBinaria
from NoArvoreBinaria import NoArvoreBinaria

arvore = ArvoreBinaria()
arvore2 = ArvoreBinaria()

n4 = NoArvoreBinaria(10, None, None)
n2 = NoArvoreBinaria(8, None, None)
n3 = NoArvoreBinaria(2, n4, None)
n1 = NoArvoreBinaria(4, n2, n3)

arvore.insere(n1.getInfo(), n1.getSae(), n1.getSad())
arvore2.insere(n1.getInfo(), n1.getSae(), n1.getSad())

print(arvore)

print(arvore.vazia())

print(arvore.pertence(10))

print(arvore.pares())

print(arvore.folhas())

print(arvore.numNos())

print(arvore.altura())

print(arvore.igual(arvore2))
