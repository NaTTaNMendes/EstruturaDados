from Lista import Lista


lista = Lista()

lista.insere("batata")
lista.insere("cebola")
lista.insere("chuveiro")

lista.retira("cebola")

lista.imprime()

lista.libera()

lista.imprime()

lista.insereFim("ovo")

lista.imprime()

lista2 = Lista()
lista2.insere("ovo")

print(lista.igual(lista2))