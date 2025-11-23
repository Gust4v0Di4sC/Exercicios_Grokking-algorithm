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

# 1.4 você tem um numero de telfone e deseja encontrar o dono dele em uma agenda telefonica (Deve procurar pela agenda inteira)

# O(n)

# 1.5 você quer ler o numero de cada pessoa da agenda telefônica

# O(n)

# 1.6 você quer ler o numero apenas dos nomes que começam com a letra A

# O(n+26) , O(n-26), O(n*26), O(n/26) === O(n) a constante não altera o resultado o tempo continua sendo O(n)