# Exercicios

#8.1 Voce trabalha para uma empresa de mobilias e tem de enviar os moveis para todo o pais . é necessasario encher o seu caminhao com caixa e todas as caixa sao de tamanhos diferentes  voce esta tentando maximizar o espaço que consegue usar em cada caminhao. comoescolheria as caixas para maximizar o espaço? proponha uma solução gulosa . ela lhe dara a solução ideal?

#Uma estrategia gulosa seria escolher a maior caixa que cabe no espaço restante , repetindo ate que nao seja mais possivel colocar nenhuma caixa. Não a solução ideal não sera alcançada.

#8.2 voce esta viajando para a europa e tem sete dias para visitar o maior numero de lugares. para cada lugar voce atribui um valor (o quanto deseja ver) e estima quanto tempo demora. como maximizar o total de pontos (passar por todos os lugares que realmente quer ver)  durante sua estadia? proponha uma solução gulosa. ela lhe dara a solução ideal?

# continuar escolhendo a atividade com a maior pontuação possivel que voce ainda consegue fazer com o tempo que sobra, não , isto não lhe dara a solução ideal

#Problema da cobertura de conjuntos

estados_abranger = set(["mt","wa","or","id","nv","ut","ca","az"])


estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"]) 
estacoes["kdois"] = set(["wa", "id", "mt"]) 
estacoes["ktres"] = set(["or","nv","ca"]) 
estacoes["kquatro"] = set(["nv","ut"]) 
estacoes["kcinco"] = set(["ca","az"])

estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()

    for estacao, estados_por_estcao in estacoes.items():
        cobertos = estados_abranger & estados_por_estcao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estacoes_finais.add(melhor_estacao)
    estados_abranger -= estados_cobertos
    
print(estacoes_finais)

#Exercicios 
#para cada um desses algoritmos diga se ele é um algoritmo guloso ou não

#8.3 Quicksort
# Não

#8.4 Pesquisa em largura
# Não

#8.5 Algoritmo de Djikstra
# Sim

#Problema NP-completos

#indicativos de um problema np-completo (como caixeiro-viajante)

#seu algoritmo roda rapido para laguns itens mas fica muito lento com o aumento de itens.

#todas as combinações de x geralmente significam um problema np-completo

#voce tem de calcular cada possivel versao de x porque não pode dividir em subproblemas menores? talvez seja um problema np-completo

#se o seu problema envolve uma sequencia (como uma sequencia de cidades , como o problem do caixeiro-viajante) e é dificil de resolver , pode ser um problema np-completo

#se o seu problema envolve um conjunto (como um conjunto de estações de radio)e é dificil de resolver , pode ser um np-completo

#voce pode reescrever o seu problema como o problem a de cobertura minima de conjuntos ou o problema do caixeiro-viajante? entao seu problema definitivamente é NP-completo.

#Exercicios 

#8.6 um carteiro deve entregar correspondecnias para vinte casas ele deve encontrar a rota mais curta que passe por todas as vinte casa esse problema é np-completo?

# Sim 

#8.7 encontrar o maior clique em um conjunto de pessoas (um clique, para este exemplo , é um conjunto de pessoas que todos se conhecem) isso é um problema NP-completo?

#Sim 

#8.8 você esta fazendo um mapa dos estados unidos e precisa colorir estados adjacentes com cores diferentes. para isso deve encontrar o numero minimo de cores para que não existam dois estados adjacentes com a mesma cor. isso é um problema np-completo?

#Sim


# para resolver um problema np-completo , o melhor a fazer e usar um algoritmo de aproximação

#algoritmos gulosos são faceis de escrever e tem tempo de execução baixo , portanto eles sao bons algoritmos de aproximação