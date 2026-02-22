from collections import defaultdict

def mapper(documento):
    """Transforma o texto em pares (palavra, 1)"""
    pares = []
    for palavra in documento.lower().split():
        pares.append((palavra, 1))
    return pares

def reducer(palavra, contagens):
    """Soma todas as ocorrências de uma palavra específica"""
    return (palavra, sum(contagens))

# --- Execução ---

# Nossos dados (Poderiam ser petabytes de logs)
dados = [
    "Python é legal",
    "MapReduce é potente",
    "Python Python Python"
]

# 1. ETAPA MAP (Pode rodar em computadores diferentes ao mesmo tempo)
resultados_map = []
for doc in dados:
    resultados_map.extend(mapper(doc))

# 2. ETAPA SHUFFLE (Agrupar por chave)
# No mundo real, o framework (Hadoop/Spark) faz isso sozinho
agrupado = defaultdict(list)
for palavra, contagem in resultados_map:
    agrupado[palavra].append(contagem)

# 3. ETAPA REDUCE (Consolidar resultados)
resultado_final = {}
for palavra, lista_contagens in agrupado.items():
    palavra, total = reducer(palavra, lista_contagens)
    resultado_final[palavra] = total

print("Resultado Final:", resultado_final)


# Por que isso mudou o mundo?

# Antes do MapReduce, se você tivesse um arquivo de 10TB, precisaria de um supercomputador caríssimo para processá-lo. Com o MapReduce:

#     Escalabilidade Horizontal: Você pode usar 1.000 computadores baratos ("comuns") em vez de um supercomputador.

#     Tolerância a Falhas: Se um computador quebrar durante o "Map", o sistema simplesmente manda aquela pequena tarefa para outro computador, sem precisar recomeçar do zero.

#     Localidade de Dados: Em vez de mover 10TB de dados pela rede (lento), você envia o código (alguns KB) para onde os dados já estão armazenados.