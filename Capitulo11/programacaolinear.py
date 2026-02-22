from scipy.optimize import linprog

# 1. Definição da Função Objetivo (Lucro)
# Queremos maximizar 3x + 2y -> Minimizamos -3x - 2y
c = [-3, -2]

# 2. Definição das Restrições de Lado Esquerdo (Coeficientes)
# 2x + 0y <= 10 (Peças)
# 1x + 3y <= 15 (Tempo)
A = [
    [2, 0], 
    [1, 3]
]

# 3. Definição das Restrições de Lado Direito (Limites)
b = [10, 15]

# 4. Limites das variáveis (x e y não podem ser negativos)
x_bounds = (0, None)
y_bounds = (0, None)

# 5. Executando o Simplex
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# --- Resultados ---
print(f"Quantidade ideal de Carrinhos (x): {res.x[0]}")
print(f"Quantidade ideal de Bonecos (y): {res.x[1]}")
print(f"Lucro Máximo Estimado: R$ {-res.fun:.2f}")


# Como o Simplex funciona visualmente?

#     Região Viável: As restrições criam um polígono no gráfico (uma área onde todas as regras são obedecidas).

#     Vértices: O Simplex sabe matematicamente que a solução ideal sempre está em um dos cantos (vértices) dessa área.

#     A Caminhada: * Ele começa na origem (0,0).

#         Ele testa os vizinhos: "Se eu me mover para este canto, o lucro aumenta?".

#         Ele pula de canto em canto até que nenhum vizinho ofereça um lucro maior.

# Aplicações Reais

#     Logística: Como o iFood decide qual entregador pega qual pedido para minimizar o tempo total?

#     Refinarias: Qual a mistura exata de petróleo bruto para gerar o máximo de gasolina e diesel com o menor custo?

#     Dieta: Qual a combinação de alimentos que atende a todos os nutrientes necessários gastando o mínimo de dinheiro? (Este foi o primeiro problema resolvido pelo criador do Simplex, George Dantzig).

# A Programação Linear é o que faz as grandes empresas economizarem bilhões operando na "beirada" da eficiência máxima.