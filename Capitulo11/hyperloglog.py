import hashlib
import math

class SimpleHyperLogLog:
    def __init__(self, num_buckets=64):
        self.num_buckets = num_buckets
        # Cada balde guarda o MÁXIMO de zeros que já viu
        self.buckets = [0] * num_buckets
        # Quantos bits precisamos para endereçar os baldes (ex: 64 baldes = 6 bits)
        self.bits_indice = int(math.log2(num_buckets))

    def _contar_zeros_iniciais(self, binario):
        """Conta quantos zeros aparecem antes do primeiro '1'"""
        try:
            return binario.index('1') + 1
        except ValueError:
            return len(binario)

    def adicionar(self, item):
        # 1. Cria um hash binário do item
        h = hashlib.md5(item.encode()).hexdigest()
        bin_h = bin(int(h, 16))[2:].zfill(128)
        
        # 2. Usa os primeiros bits para escolher o balde
        indice_balde = int(bin_h[:self.bits_indice], 2)
        
        # 3. Usa o restante para contar os zeros
        resto_do_hash = bin_h[self.bits_indice:]
        zeros = self._contar_zeros_iniciais(resto_do_hash)
        
        # 4. Atualiza o balde se encontrar uma sequência maior de zeros
        self.buckets[indice_balde] = max(self.buckets[indice_balde], zeros)

    def estimar(self):
        # Média harmônica para evitar que valores extremos estraguem a conta
        soma_invertida = sum(2.0 ** -x for x in self.buckets)
        estimativa = (self.num_buckets ** 2) / soma_invertida
        
        # Fator de correção simplificado (o HLL real usa um valor 'alpha' mais complexo)
        alpha = 0.7213 / (1 + 1.079 / self.num_buckets)
        return int(estimativa * alpha)

# --- Teste Prático ---
hll = SimpleHyperLogLog(num_buckets=128)

# Adicionando 10.000 itens (alguns repetidos)
for i in range(10000):
    hll.adicionar(f"usuario_{i}")
    if i % 2 == 0: # Repete alguns usuários
        hll.adicionar(f"usuario_{i}")

print(f"Estimativa de itens únicos: {hll.estimar()}")

# Por que o HyperLogLog é "Mágico"?

#     Memória Irrisória: Para contar 1 bilhão de itens com 2% de erro, o HLL precisa de apenas 1.5 KB de memória. Um set de Python precisaria de mais de 10 GB.

#     Velocidade: O custo de adicionar um item é apenas o tempo de gerar um hash (O(1)).

#     Merge Fácil: Se você tem o HLL de "Segunda-feira" e o de "Terça-feira", você pode combiná-los apenas pegando o valor máximo de cada balde correspondente. Isso é perfeito para sistemas distribuídos (MapReduce).

# Onde ele é usado?

#     Redis: Tem uma implementação nativa de HLL.

#     BigQuery/AWS Redshift: Para contar COUNT(DISTINCT user_id) em tabelas colossais.

#     Análise de Redes: Para detectar ataques de negação de serviço (DDoS) contando quantos IPs diferentes estão acessando um servidor.