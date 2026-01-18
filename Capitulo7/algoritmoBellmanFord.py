def bellman_ford(grafo, origem):
    # 1. Inicialização
    distancias = {no: float('inf') for no in grafo}
    distancias[origem] = 0
    
    # 2. Relaxar as arestas (V - 1) vezes
    for _ in range(len(grafo) - 1):
        for u in grafo:
            for v, peso in grafo[u].items():
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso

    # 3. Verificação de ciclos negativos
    for u in grafo:
        for v, peso in grafo[u].items():
            if distancias[u] + peso < distancias[v]:
                print("Atenção: O grafo contém um ciclo de peso negativo!")
                return None

    return distancias

# Exemplo de uso:
meu_grafo = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}

resultado = bellman_ford(meu_grafo, "inicio")
print(f"Distâncias finais: {resultado}")