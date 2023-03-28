from ListaDupla import ListaDupla

lista  = ListaDupla()
lista2 = ListaDupla()

print(lista.imprime())
print(lista2.imprime())

lista.insere('a')
lista.insere('b')

print(lista.imprime())

print(lista.vazia())

print(lista.busca('a').getInfo())

print(lista.comprimento())

print(lista.ultimo().getInfo())

lista.retira('b')

print(lista.imprime())

lista.insereFim('b')

print(lista.imprime())

lista2.insere('c')
lista2.insere('d')

print(lista.igual(lista2))

lista.merge(lista2)

print(lista.imprime())
