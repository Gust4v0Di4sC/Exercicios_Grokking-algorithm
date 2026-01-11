
# Exercicios 

#6.1 encontre o menor caminho do inicio ao fim

# I-O-F  2 etapas  menor caminho

#6.2 encontre o menor caminho de jato ate gato

# J-G 2 etapas menor caminho

# pequeno grafo em python
grafo = {}
grafo["você"] = ["alice","claire","bob"]


# Grafo maior
grafo = {}
grafo["você"] = ["alice","claire","bob"]
grafo["bob"] = ["anuj","peggy"]
grafo["claire"] = ["thom","jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

#implementação do grafo com fila

from collections import deque


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


#Exercicios

#6.3 segundo as a estrutura de grafos apresentada diga se as listas são validas ou invalidas

#A Inválida 
#B válida
#C Inválida

#6.4 um grafo maior faça uma lista valida para ele
# Acordar
# Praticar Exercicio 
# Tomar banho
# Trocar de roupa
# Escovar os dentes
# Tomar café da manhã
# Embrulhar o lanche

# 6.5 quais desses grafos também são arvores
# A = Arvore
# B = não é um arvore
# C = Arvore