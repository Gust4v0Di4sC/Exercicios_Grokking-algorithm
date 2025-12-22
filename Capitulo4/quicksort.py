# [1:] slicing para fazer subarray do segundo indice em diante [[0] -> ,1,2,3,4]

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i<= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    

print(quicksort([10,5,2,3]))

def mergesort(array):
    if len(array) > 1:
        meio = len(array) // 2
        
        esquerda = array[:meio]
        direita =  array[meio:]
        
        mergesort(esquerda)
        mergesort(direita)
        
        i = j = k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i+= 1
            else:
                array[k] = direita[j]
                j+= 1
            k+= 1
        
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1
        
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

minha_lista = [38,27,43,3,9,10]
mergesort(minha_lista)
print(minha_lista)
                

#Exercicio  4.5 imprimir o valor de cada elemento em um array

#levaria  O(n)  pois demandaria uma iteração um por um
def eachItem(array):
    for item in array:
        print(item)

eachItem([2,3,4,5,6])

#Exercicio 4.6 duplicar o valor de cada elemento em um array

#levaria O(n)

#Exercicio 4.7 duplicar o valor apenas do primeiro elemento em um array

# levaria O(1)

#Exercicio 4.8 criar tabela de multiplicação com todos os elementos do array

#levaria O(n²)