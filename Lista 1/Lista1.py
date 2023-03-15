from random import shuffle
import sys
import time

def bubbleSort(vetor):
    troca = True
    while troca:
        troca = False
        for i in range(len(vetor) - 1):
            if vetor[i] > vetor[i + 1]:
                temp = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = temp
                troca = True
    return vetor

def quickSort(vetor, a, b):
    if a < b:
        indicePivo = particiona(vetor, a, b)
        quickSort(vetor, a, indicePivo-1)
        quickSort(vetor, indicePivo + 1, b)    
    return vetor

def particiona(vetor, a, b):
    x = vetor[a]
    while a < b:
        while vetor[a] < x:
            a += 1
        while vetor[b] > x:
            b -= 1
        aux = vetor[a]
        vetor[a] = vetor[b]
        vetor[b] = aux
    return a

def criaVetorEmbaralhado(tamanho):
    vetor = []*tamanho
    for numero in range(tamanho):
        vetor.append(numero)
    shuffle(vetor)
    return vetor

def merge(vetor, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = vetor[l + i]
 
    for j in range(0, n2):
        R[j] = vetor[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            vetor[k] = L[i]
            i += 1
        else:
            vetor[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        vetor[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        vetor[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(vetor, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(vetor, l, m)
        mergeSort(vetor, m+1, r)
        merge(vetor, l, m, r)
    return vetor

def testaEPrinta(vetor, fim):
    vetorBubble = vetor
    vetorQuick = vetor
    vetorMerge = vetor
    
    inicial = time.time()
    print(bubbleSort(vetorBubble))
    final = time.time()
    print('tempo bubble: ', final-inicial)
    print()
    
    inicial = time.time()
    print(quickSort(vetorQuick, 0, fim))
    final = time.time()
    print('tempo quick: ', final-inicial)
    print()
    
    inicial = time.time()
    print(mergeSort(vetorMerge, 0, fim))
    final = time.time()
    print('tempo merge: ', final-inicial)
    print()  

def main():
    vetorzinho = criaVetorEmbaralhado(10)
    vetorPequeno = criaVetorEmbaralhado(100)
    vetorMedio = criaVetorEmbaralhado(1000)
    vetorGrande = criaVetorEmbaralhado(10000)

    print('Vetorzinho:\n')
    print(vetorzinho)
    testaEPrinta(vetorzinho, 9)
    
    print('Vetor pequeno:\n')
    print(vetorPequeno)
    testaEPrinta(vetorPequeno, 99)
    
    print('Vetor medio:\n')
    print(vetorMedio)
    testaEPrinta(vetorMedio, 999)
    
    print('Vetor grande:\n')
    print(vetorGrande)
    testaEPrinta(vetorGrande, 9999)
    
    
    # A FUNÇÃO DE TESTAEPRINTA ESTÁ BUGADA, ENTRETANTO AS FUNÇÕES DE MERGE E QUICKSORT ESTÃO FUNCIONANDO PARA VALORES MUITO GRANDES.
    # BASTA UTILIZA-LAS DE FORMA DIRETA, NO CASO DESSE FONTE NÃO ESTOU CHAMANDO-AS DIRETAMENTE POR CONTA DO EXERCICIO 3 
    
if __name__=="__main__":
    main()
        
