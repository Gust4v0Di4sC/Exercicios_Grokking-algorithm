import hashlib

def gerar_impressao_digital(texto):
    # 1. Criamos um objeto de hash SHA-256
    sha256 = hashlib.sha256()
    
    # 2. Alimentamos o objeto com os dados (em formato de bytes)
    sha256.update(texto.encode('utf-8'))
    
    # 3. Pegamos o resultado em formato hexadecimal
    return sha256.hexdigest()

# --- Demonstração do Efeito Avalanche ---
entrada1 = "O gato subiu no telhado"
entrada2 = "O gato subiu no telhado." # Apenas um ponto final de diferença

hash1 = gerar_impressao_digital(entrada1)
hash2 = gerar_impressao_digital(entrada2)

print(f"Texto 1: {entrada1}")
print(f"Hash 1 : {hash1}")
print("-" * 20)
print(f"Texto 2: {entrada2}")
print(f"Hash 2 : {hash2}")

# Aplicações Reais (Onde você usa isso sem saber)
# 1. Armazenamento de Senhas

# Sites seguros nunca guardam sua senha real no banco de dados. Eles guardam o SHA dela.

#     Quando você faz login, o site faz o hash do que você digitou e compara com o hash guardado.

#     Se um hacker invadir o banco, ele só verá códigos indecifráveis, não sua senha "123456".

# 2. Verificação de Integridade (Checksum)

# Já baixou um arquivo e viu um código "SHA-256" do lado do link?

#     Você roda o SHA no arquivo baixado.

#     Se o seu código for igual ao do site, o arquivo é seguro. Se for diferente, o arquivo foi corrompido ou alterado por um vírus.

# 3. Blockchain e Bitcoin

# O Bitcoin usa o SHA-256 para o "Proof of Work" (Mineração).

#     Os mineradores precisam encontrar um hash que comece com uma quantidade específica de zeros. Como o SHA é imprevisível, a única forma de fazer isso é na "força bruta", testando bilhões de combinações por segundo.

# Curiosidade: O SHA-1 (uma versão antiga) hoje é considerado "quebrado" porque supercomputadores já conseguem gerar colisões (duas entradas diferentes com o mesmo hash). Por isso, hoje o padrão ouro é o SHA-256 ou SHA-3.