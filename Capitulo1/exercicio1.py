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

