import hashlib

class FiltroDeBloom:
    def __init__(self, tamanho=100):
        # Criamos um "balde" de bits inicializado com zeros
        self.bit_array = [0] * tamanho
        self.tamanho = tamanho

    def _get_hashes(self, item):
        # Simulamos 3 funções de hash diferentes usando o MD5 e SHA1
        # Isso gera 3 "endereços" diferentes no nosso array de bits
        h1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.tamanho
        h2 = int(hashlib.sha1(item.encode()).hexdigest(), 16) % self.tamanho
        h3 = hash(item) % self.tamanho # Hash nativo do Python
        return [h1, h2, h3]

    def adicionar(self, url):
        for endereco in self._get_hashes(url):
            self.bit_array[endereco] = 1
        print(f"URL '{url}' mapeada nos bits: {self._get_hashes(url)}")

    def verificar(self, url):
        for endereco in self._get_hashes(url):
            # Se QUALQUER um dos bits for 0, a URL com certeza nunca foi vista
            if self.bit_array[endereco] == 0:
                return "Definitivamente NÃO existe"
        
        # Se todos forem 1, PODE ser que exista (ou pode ser uma colisão)
        return "Talvez exista (verificar no Banco de Dados)"

# --- Teste Prático ---
filtro = FiltroDeBloom(tamanho=20)

# 1. Adicionamos algumas URLs conhecidas
filtro.adicionar("bit.ly/python-top")
filtro.adicionar("bit.ly/promo-verao")

print("-" * 30)

# 2. Testamos uma que nunca vimos
print(f"Checando 'bit.ly/fake-url': {filtro.verificar('bit.ly/fake-url')}")

# 3. Testamos uma que já adicionamos
print(f"Checando 'bit.ly/python-top': {filtro.verificar('bit.ly/python-top')}")

# Por que isso é genial para dados massivos?

#     Economia de Espaço Absurda: Você não guarda a URL inteira (que pode ter 200 caracteres). Você guarda apenas alguns bits em um array. Você pode representar 1 bilhão de URLs com apenas alguns centenas de MB de RAM.

#     Velocidade Relâmpago: Operações de hash e acesso a índices de lista são O(1) (tempo constante). Não importa se você tem 10 ou 10 bilhões de itens, a resposta é instantânea.

#     Sem Falsos Negativos: Se o filtro diz que "Não existe", você pode confiar 100%. Isso economiza bilhões de consultas desnecessárias ao banco de dados.

# O "Pulo do Gato": Falsos Positivos

# O único problema é que, como o array de bits tem tamanho finito, duas URLs diferentes podem, por puro azar, acabar marcando os mesmos bits (colisão). Por isso a resposta é "Talvez". Se o filtro der um falso positivo, o sistema apenas faz uma busca lenta no banco e descobre que não estava lá. É um preço pequeno a pagar pela performance absurda no resto do tempo.