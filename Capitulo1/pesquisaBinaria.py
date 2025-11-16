
def pesquisa_binaria(lista, item_buscado):
    baixo = 0
    alto = len(lista) - 1
    etapas = 0
    
    while baixo <= alto:
        etapas += 1
        meio = (baixo+alto) // 2 #divisao inteira 
        chute = lista[meio]
        
        if chute == item_buscado:
            return f"O numero buscado foi encontrado na posicão: {meio} e levou {etapas} etapas para encontra-lo"
        if chute > item_buscado:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None 

minha_lista  = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista,3))