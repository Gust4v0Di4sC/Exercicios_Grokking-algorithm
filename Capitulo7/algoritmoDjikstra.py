# exemplo 
grafo = {}

grafo["inicio"] = {}

grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

print(grafo["inicio"].keys())

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito


pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None


#manter o registro de todos os vertices processados
processados = []


#enquanto houver grafos a serem processados
    #pegue o vertice que esta mais proximo do inicio
    #atualize o custo dos vizinhos
        #se qualquer um dos custos dos vizinhos for atualizado, atualize também o pai
#Marque o vertice como processado

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)
    
#Algoritmo de djikstra so funciona quando todos os pesos sao positivos
#Para pesos negativos utilize o algoritmo de bellman-ford
    
# Exercicio

#7.1 em cada um dos grafos qual o peso do caminho minimo do inicio ao fim

# A = 8
# B = 60
# C = Nenhum caminho minimo é possivel (Ciclo de peso negativo)