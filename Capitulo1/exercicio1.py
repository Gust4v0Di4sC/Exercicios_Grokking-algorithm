import math

# exercicio 1.1

def calcular_max_etapas_binaria(lista):
    if lista <= 0:
        return 0
    
    
    logaritmo_lista = math.log2(lista) 
    teto_lista = math.ceil(logaritmo_lista) # garante arredondamento do numero para o inteiro mais proximo 
    max_etapas = teto_lista
    
    
    return max_etapas 

nomes_128 = 128

etapas = calcular_max_etapas_binaria(nomes_128)

print(f"O numero maximo de etapas para encontrar um nome desejado é : {etapas} ")

# exercicio 1.2

def calcular_max_etapas_binaria(lista):
    if lista <= 0:
        return 0
    
    
    logaritmo_lista = math.log2(lista) 
    teto_lista = math.ceil(logaritmo_lista) # garante arredondamento do numero para o inteiro mais proximo 
    max_etapas = teto_lista
    
    
    return max_etapas 

nomes_256 = 256

etapas = calcular_max_etapas_binaria(nomes_256)

print(f"O numero maximo de etapas para encontrar um nome desejado é : {etapas} ")

# 1.3 você tem um nome e deseja encontrar o numero de telefone para esse nome em uma agenda telefonica , qual é o tempo em termos de notação Big O

# O(log n)

def busca_binaria_nome(lista_nomes, nome_procurado):
    """Simula a busca binária para encontrar um nome em O(log n)."""
    
    # É essencial que a lista esteja ordenada
    lista_nomes.sort() 
    
    operacoes = 0
    baixo = 0
    alto = len(lista_nomes) - 1

    while baixo <= alto:
        operacoes += 1
        meio = (baixo + alto) // 2
        
        if lista_nomes[meio] == nome_procurado:
            print(f"  -> Nome '{nome_procurado}' encontrado em {operacoes} operações (O(log n)).")
            return lista_nomes[meio]
        elif lista_nomes[meio] < nome_procurado:
            baixo = meio + 1
        else:
            alto = meio - 1
            
    print(f"  -> Nome '{nome_procurado}' não encontrado em {operacoes} operações.")
    return None

# Exemplo de uso
agenda = {
    "Alice": "1111", "Bob": "2222", "Charlie": "3333", 
    "David": "4444", "Eva": "5555", "Fernando": "6666", 
    "Gina": "7777", "Hugo": "8888", "Inês": "9999", "Jonas": "0000"
}
nomes = list(agenda.keys())
print("--- Busca Binária (O(log n)) ---")
busca_binaria_nome(nomes, "David")
busca_binaria_nome(nomes, "Jonas") # Pior caso logarítmico (depende da árvore)
busca_binaria_nome(nomes, "Xuxa")


# 1.4 você tem um numero de telefone e deseja encontrar o dono dele em uma agenda telefonica (Deve procurar pela agenda inteira)

# O(n)
def busca_linear_numero(agenda, numero_procurado):
    """Simula a busca linear para encontrar o nome pelo número em O(n)."""
    operacoes = 0
    
    for nome, numero in agenda.items():
        operacoes += 1
        if numero == numero_procurado:
            print(f"  -> Dono '{nome}' encontrado para o número {numero_procurado} em {operacoes} operações (O(n)).")
            return nome
            
    print(f"  -> Número {numero_procurado} não encontrado em {operacoes} operações.")
    return None

# Exemplo de uso
agenda = {
    "Alice": "1111", "Bob": "2222", "Charlie": "3333", 
    "David": "4444", "Eva": "5555", "Fernando": "6666", 
    "Gina": "7777", "Hugo": "8888", "Inês": "9999", "Jonas": "0000"
}
print("\n--- Busca Linear pelo Número (O(n)) ---")
busca_linear_numero(agenda, "1111") # Melhor caso (1 operação)
busca_linear_numero(agenda, "0000") # Pior caso (N operações)


# 1.5 você quer ler o numero de cada pessoa da agenda telefônica

# O(n)
def ler_todos_numeros(agenda):
    """Simula a leitura de todas as entradas em O(n)."""
    operacoes = 0
    
    print("  --- Nomes e Números Lidos (O(n)) ---")
    for nome, numero in agenda.items():
        operacoes += 1
        # print(f"  {nome}: {numero}") # Descomente para ver a lista completa
    
    print(f"  -> Total de {operacoes} entradas lidas.")
    return operacoes

# Exemplo de uso
agenda = {
    "Alice": "1111", "Bob": "2222", "Charlie": "3333", 
    "David": "4444", "Eva": "5555", "Fernando": "6666", 
    "Gina": "7777", "Hugo": "8888", "Inês": "9999", "Jonas": "0000"
}
print("\n--- Leitura Completa (O(n)) ---")
ler_todos_numeros(agenda)


# 1.6 você quer ler o numero apenas dos nomes que começam com a letra A

# O(n+26) , O(n-26), O(n*26), O(n/26) === O(n) a constante não altera o resultado o tempo continua sendo O(n)

def ler_nomes_com_a(agenda):
    """Simula a leitura de nomes que começam com 'A' em O(n)."""
    operacoes_busca = 0
    resultados = []
    
    for nome, numero in agenda.items():
        operacoes_busca += 1 # Conta a operação de inspeção/comparação
        if nome.startswith('A'):
            resultados.append((nome, numero))
            
    print(f"  -> {len(resultados)} resultados encontrados em {operacoes_busca} operações de busca/comparação (O(n)).")
    return resultados

# Exemplo de uso
agenda_com_a = {
    "Ana": "1000", "Beto": "2000", "Alice": "3000", 
    "Carlos": "4000", "Amanda": "5000", "Daniel": "6000", 
    "André": "7000", "Eva": "8000"
}
print("\n--- Leitura e Filtragem (O(n)) ---")
ler_nomes_com_a(agenda_com_a)