def criar_indice_invertido(documentos):
    indice = {}

    for doc_id, texto in documentos.items():
        # Normalização simples: letras minúsculas e divide por espaços
        palavras = texto.lower().split()
        
        for palavra in palavras:
            # Se a palavra não está no índice, cria uma lista vazia
            if palavra not in indice:
                indice[palavra] = set() # Usamos set para evitar IDs duplicados
            
            # Adiciona o ID do documento à palavra correspondente
            indice[palavra].add(doc_id)
            
    return indice

def buscar(termo, indice):
    termo = termo.lower()
    return indice.get(termo, "Nenhum resultado encontrado.")

# --- Exemplo de Uso ---

# 1. Nossa "Base de Dados"
meus_documentos = {
    1: "Python é uma linguagem de programação",
    2: "Programação em Python é muito divertida",
    3: "O café está quente hoje",
    4: "Aprender programação ajuda na carreira"
}

# 2. Construindo o índice
meu_indice = criar_indice_invertido(meus_documentos)

# 3. Testando a busca
print(f"Onde aparece 'Python'?: {buscar('Python', meu_indice)}")
print(f"Onde aparece 'programação'?: {buscar('programação', meu_indice)}")
print(f"Onde aparece 'café'?: {buscar('café', meu_indice)}")

# Por que isso é eficiente?

#     Velocidade Incrível: Você não precisa "ler" o texto dos documentos durante a busca. Você apenas consulta uma chave no dicionário (hash table), o que é quase instantâneo.

#     Escalabilidade: Mesmo com milhões de documentos, o tempo de resposta depende mais do número de palavras únicas do que do tamanho total do texto.