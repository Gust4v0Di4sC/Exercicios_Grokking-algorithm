## Exercicios

# 9.1 Imagine que voce consegue roubar outro item um mp3 player ele pesa 1kg e vale 1000 você deveria rouba-lo ? 

# na bolsa de 3kg ele valerá a pena mas  nao na de 4kg

# na programação dinamica não existe metade de um item , é tudo ou nada

# 9.2 Suponha que você esteja indo acampar  e que sua mochila tenha capacidade para 6 quilos. Sendo assim você pode escolher entre os itens abaixo para levar. Cada item tem um valor e quanto mais alto este valor , mais importante p item é

# Agua 3kg , 10
# Livro 1kg, 3
# Comida 2kg , 9
# Casaco 2kg, 5
# Câmera, 1kg , 6

# Comida , Camera e Agua

if palavra_a[i] == palavra_b[j]:
    celula[i][j] = celula[i-1][j-1] + 1
else:
    celula[i][j] = 0
    

if palavra_a[i] == palavra_b[j]:
    celula[i][j] = celula[i-1][j-1] + 1
else:
    celula[i][j] = max(celula[i-1][j], celula[i][j-1])
    
# 9.3 Desenhe e preencha uma tabela para calcular a maior substring comum entre blue e clues

# a maior substring entre blue e clues é 3