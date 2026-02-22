import numpy as np

def dft_simples(sinal):
    """
    Uma implementação manual (e lenta, mas didática) da 
    Transformada Discreta de Fourier.
    """
    N = len(sinal)
    X = []
    
    # Para cada frequência 'k' que queremos testar
    for k in range(N):
        soma = 0
        # Comparamos com cada ponto 'n' do nosso sinal original
        for n in range(N):
            # A "mágica" de Euler: cossenos e senos
            angulo = 2 * np.pi * k * n / N
            exponencial_complexa = np.complex128(np.cos(angulo) - 1j * np.sin(angulo))
            soma += sinal[n] * exponencial_complexa
        X.append(soma)
        
    return np.array(X)

# --- Criando nossos dados ---
# Vamos misturar uma onda de 5Hz e uma de 20Hz
taxa_amostragem = 100 # pontos por segundo
t = np.linspace(0, 1, taxa_amostragem)
sinal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# --- Executando a Transformada ---
frequencias_encontradas = dft_simples(sinal)
magnitudes = np.abs(frequencias_encontradas) # Pega a "força" de cada frequência

# Exibindo resultados (Simplificado)
for i in range(len(magnitudes) // 2): # Olhamos só a primeira metade (simetria)
    if magnitudes[i] > 10: # Filtro simples para mostrar o que é relevante
        print(f"Frequência detectada: {i}Hz com intensidade {magnitudes[i]:.2f}")
        
# Por que isso é importante?

#     Filtros de Áudio: Se você quer remover um ruído agudo, você aplica a Fourier, "zera" as frequências altas e reconstrói o som.

#     Compressão JPEG: A imagem é dividida em frequências visuais; as que o olho humano não percebe são descartadas para diminuir o tamanho do arquivo.