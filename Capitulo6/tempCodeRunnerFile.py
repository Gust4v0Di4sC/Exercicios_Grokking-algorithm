def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

def pesquisa_largura(nome):
    fila_de_pesquisa = deque(grafo[nome])
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + "é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

pesquisa_largura("você")