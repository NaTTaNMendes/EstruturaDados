from ArvoreBinaria import ArvoreBinaria
from NoArvoreBinaria import NoArvoreBinaria

arvore = ArvoreBinaria()

n4 = NoArvoreBinaria(10, None, None)
n2 = NoArvoreBinaria(8, None, None)
n3 = NoArvoreBinaria(2, n4, None)
n1 = NoArvoreBinaria(4, n2, n3)

arvore.insere(n1.getInfo(), n1.getSae(), n1.getSad())

print(arvore)
print(arvore.altura())
