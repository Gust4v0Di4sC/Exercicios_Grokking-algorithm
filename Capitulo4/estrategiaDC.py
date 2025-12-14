arr = [2,4,6]

def soma(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(soma(arr))
    

#Exercicio 4.1 escreva o código da função soma, vista anteriormente

arr = [2,4,6]
def soma_recursiva(lista):
    if lista == []: # <- caso base
        return 0
    else:  
        primeiro_elemento = lista[0]
        resto_lista = lista[1:]
        return primeiro_elemento + soma_recursiva(resto_lista) #  <- caso recursivo

print(soma_recursiva(arr))

# Exercicio 4.2 Escreva uma função recursiva que conte o numero de itens de uma lista

arr2 = [1,2,3,4,5]
def contagem_recursiva(lista):

    if not lista:
        return 0 
    else:
        resto_lista = lista[1:]
        return 1 + contagem_recursiva(resto_lista) 

print(contagem_recursiva(arr2))

# Exercicio 4.3 Encontre o valor mais alto em uma lista

arr3 = [2,3,4,5,6]
def max_value(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return  max_value(lista[1:])
 

print(max_value(arr3))

# Exercicio 4.4 Determinar caso base e caso recursivo da pesquisa binaria

def pesquisa_binaria(lista, item_buscado, inicio , fim):
    # baixo = 0
    # alto = len(lista) - 1
    # etapas = 0
    
    if inicio > fim: # Caso base
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == item_buscado:
        return meio
    elif item_buscado < lista[meio]:
        return pesquisa_binaria(lista, item_buscado, inicio, meio -1) # Caso recursivo lado direito da lista
    else:
        return pesquisa_binaria(lista, item_buscado, meio+1, fim) # Caso recursivo lado esquerdo da lista
    

minha_lista  = [1, 3, 5, 7, 9]
item_procurado = 3

resultado = pesquisa_binaria(minha_lista,item_procurado,0,len(minha_lista)-1)

if resultado != -1:
    print(f"O item {item_procurado} foi encontrado no índice {resultado}")
else:
    print(f"O item {item_procurado} não foi encontrado na lista")