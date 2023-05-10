from ArvoreBinaria import ArvoreBinaria
from NoArvoreBinaria import NoArvoreBinaria

arvore = ArvoreBinaria()

n2 = NoArvoreBinaria(8, None, None)
n3 = NoArvoreBinaria(2, None, None)
n1 = NoArvoreBinaria(4, n2, n3)

arvore.insere(n1.getInfo(), n1.getSae(), n1.getSad())

print(arvore)
print(arvore.folhas())
