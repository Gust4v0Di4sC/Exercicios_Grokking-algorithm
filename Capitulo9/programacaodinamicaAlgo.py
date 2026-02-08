def fibonacci_dinamico(n):
    # Caso base
    if n <= 1:
        return n
    
    # Criamos uma tabela para armazenar os resultados
    # dp[i] irá guardar o valor de fibonacci de i
    dp = [0] * (n + 1)
    
    dp[0] = 0
    dp[1] = 1
    
    # Preenchemos a tabela iterativamente
    for i in range(2, n + 1):
        # A fórmula é: F(i) = F(i-1) + F(i-2)
        # Como já calculamos i-1 e i-2 antes, é só somar (acesso O(1))
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

# Teste
print(f"Fibonacci de 10: {fibonacci_dinamico(10)}") # Saída: 55


def menor_numero_moedas(moedas, valor_total):
    """
    :param moedas: Lista de valores das moedas disponíveis (ex: [1, 3, 4])
    :param valor_total: O valor que queremos alcançar (ex: 6)
    :return: Número mínimo de moedas ou -1 se não for possível
    """
    
    # Criamos um array preenchido com um valor "infinito"
    # O índice do array representa o valor a ser trocado (de 0 a valor_total)
    # dp[i] será o número mínimo de moedas para fazer o valor 'i'
    dp = [float('inf')] * (valor_total + 1)
    
    # Para fazer o valor 0, precisamos de 0 moedas
    dp[0] = 0
    
    # Iteramos por todos os valores de 1 até o valor_total
    for i in range(1, valor_total + 1):
        # Para cada valor, testamos todas as moedas disponíveis
        for moeda in moedas:
            # Se a moeda for menor ou igual ao valor atual 'i'
            if i - moeda >= 0:
                # A decisão é: O mínimo entre o que já temos OU
                # (o valor restante 'i - moeda' que já calculamos) + 1 nova moeda
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    
    # Se o valor final ainda for infinito, significa que não há combinação possível
    if dp[valor_total] == float('inf'):
        return -1
        
    return dp[valor_total]

# --- Testando o Algoritmo ---
moedas_disponiveis = [1, 3, 4]
alvo = 6

resultado = menor_numero_moedas(moedas_disponiveis, alvo)

print(f"Moedas disponíveis: {moedas_disponiveis}")
print(f"Valor alvo: {alvo}")
print(f"Mínimo de moedas necessárias: {resultado}") 
# Saída esperada: 2 (pois 3 + 3 = 6)