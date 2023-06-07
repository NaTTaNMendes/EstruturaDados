from random import shuffle
import time

def buscaLinear(vetor, objetivo):
    for index, item in enumerate(vetor):
        if item == objetivo:
            return index
    return -1

def buscaBinariaRecursiva(vetor, objetivo, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if vetor[meio] == objetivo:
        return meio
    elif vetor[meio] < objetivo:
        return buscaBinariaRecursiva(vetor, objetivo, meio + 1, fim)
    else:
        return buscaBinariaRecursiva(vetor, objetivo, inicio, meio - 1)

def criaVetorEmbaralhado(tamanho):
    vetor = []*tamanho
    for numero in range(tamanho):
        vetor.append(numero)
    shuffle(vetor)
    return vetor

def calcularLinear(vetor, valor, tipo):
    inicio = time.time()
    print(buscaLinear(vetor, valor))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print(f'tempo linear {tipo}: {tempo_decorrido}')

def calcularBinario(vetor, valor, tipo):
    inicio = time.time()
    print(buscaBinariaRecursiva(vetor, valor))
    fim = time.time()
    tempo_decorrido = fim - inicio
    print(f'tempo binario {tipo}: {tempo_decorrido}')    

vetor_pequeno = criaVetorEmbaralhado(10**1)
vetor_medio = criaVetorEmbaralhado(10**2)
vetor_grande = criaVetorEmbaralhado(10**3)
vetor_gigante = criaVetorEmbaralhado(10**4)
vetor_gigantesco = criaVetorEmbaralhado(10**5)

calcularLinear(vetor_pequeno, 6, 'pequeno')
calcularLinear(vetor_medio, 53, 'medio')
calcularLinear(vetor_grande, 456, 'grande')
calcularLinear(vetor_gigante, 4124, 'gigante')
calcularLinear(vetor_gigantesco, 85329, 'gigantesco')

vetor_pequeno.sort()
vetor_medio.sort()
vetor_grande.sort()
vetor_gigante.sort()
vetor_gigantesco.sort()

calcularBinario(vetor_medio, 53, 'medio')
calcularBinario(vetor_grande, 456, 'grande')
calcularBinario(vetor_gigante, 4124, 'gigante')
calcularBinario(vetor_gigantesco, 85329, 'gigantesco')