def calcular_mix(base, expoente_privado, primo):
    # Calcula (base^expoente) % primo
    return pow(base, expoente_privado, primo)

# --- 1. Acordo Público (Números que todos conhecem) ---
p = 23  # Um número primo (em produção seria um número gigante)
g = 5   # Uma base (gerador)

print(f"Acordo Público: Primo={p}, Base={g}\n")

# --- 2. Segredos Privados (Ninguém mais sabe) ---
segredo_privado_alice = 6
segredo_privado_bob = 15

# --- 3. Troca de Mensagens Públicas ---
# Alice calcula sua "mistura" e envia para Bob
mistura_alice = calcular_mix(g, segredo_privado_alice, p)
print(f"Alice envia publicamente: {mistura_alice}")

# Bob calcula sua "mistura" e envia para Alice
mistura_bob = calcular_mix(g, segredo_privado_bob, p)
print(f"Bob envia publicamente: {mistura_bob}")

print("-" * 30)

# --- 4. Cálculo do Segredo Comum ---
# Alice recebe a mistura do Bob e aplica seu segredo nela
chave_final_alice = calcular_mix(mistura_bob, segredo_privado_alice, p)

# Bob recebe a mistura da Alice e aplica seu segredo nela
chave_final_bob = calcular_mix(mistura_alice, segredo_privado_bob, p)

print(f"Chave Secreta da Alice: {chave_final_alice}")
print(f"Chave Secreta do Bob:   {chave_final_bob}")

# Por que isso é seguro?

# O segredo está no Problema do Logaritmo Discreto.
# É muito fácil calcular 515mod23. Mas, se você for o bisbilhoteiro e souber apenas que o resultado é 19, é extremamente difícil descobrir que o expoente era 15.

# Com números primos gigantes (de centenas de dígitos), nem todos os computadores do mundo hoje conseguiriam reverter esse cálculo.
# Aplicações

#     HTTPS (TLS): Quando você vê o cadeado no navegador, o Diffie-Hellman foi usado nos primeiros milissegundos para que seu PC e o servidor do Google criassem uma chave de criptografia.

#     WhatsApp: O protocolo de criptografia de ponta a ponta utiliza uma variação disso (chamada Elliptic Curve Diffie-Hellman) para garantir que só você e seu contato leiam as mensagens.