caderno = dict()

caderno["maçã"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49

print(caderno["maçã"])

#Quais destas funções hash são consistentes
#5.1 f(x) = 1 , Consistente

#5.2 f(x) = rand() ,Inconsistente

#5.3 f(x) = proximo_espaco_vazio() , Inconsistente

#5.4 f(x) = len(x) , Consistente

votaram = {}

valor = votaram.get("tom")

voted = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar!")
        
verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")



cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados


# Suponha que você tem estas quatro funções hash que operam com strings:

# A. Retorne "1" para qualquer entrada

# B. use o comprimento da string como indice

# C. use o primeiro caractere da string como indice. assim todas as strings que iniciam com a letra a são hasheadas juntas e assim por diante.

# D. mapeie cada letra para um numero primo: a=2 , b=3,c=5,d=7,e=11 e assim por diante. para uma string, a função hash é a soma de todos os caracteres-módulo² conforme o tamanho da hash. se o tamanho de sua hash for 10, por exemplo, e a string for "bag" o indice sera (3+2+17) % 10 = 22 % 10 = 2 

#Para cada um desses exemplos qual função hash fornecera uma boa distribuição ? considere que o tamanho da tabela hash fornecerá tenha dez espaços


#5.5 uma lista telefonica em que as chaves sao os nomes e os valores sao os numeros telefonicos. os nomes sao os seguintes : Esther , Ben, Bob e Dan , função C e D

#5.6 um mapeamento do tamanho de baterias e sua devida potencia os tamanhos sao A , AA , AAA e AAAA. Função B e D

#5.7 Um mapeamento de títulos de livros e autores. Os títulos são Maus Fun Home e Watchmen. Função B, C e D