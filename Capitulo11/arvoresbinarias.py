class NoB:
    def __init__(self, folha=False):
        self.folha = folha
        self.chaves = []  # Lista de números (dados)
        self.filhos = []  # Lista de outros Nós B (ponteiros)

class ArvoreB:
    def __init__(self, grau_minimo):
        self.raiz = NoB(folha=True)
        self.t = grau_minimo  # Define o grau (t).
        # Nota: Um nó pode ter no máximo (2*t - 1) chaves.
        # Se t=2, máx chaves = 3. Se t=3, máx chaves = 5.

    def inserir(self, k):
        raiz = self.raiz
        # Verifica se a raiz está cheia (número máximo de chaves atingido)
        if len(raiz.chaves) == (2 * self.t) - 1:
            # Se a raiz estiver cheia, a árvore precisa crescer em altura
            nova_raiz = NoB(folha=False)
            nova_raiz.filhos.append(self.raiz)
            self.dividir_filho(nova_raiz, 0)
            self.raiz = nova_raiz
            self.inserir_nao_cheio(nova_raiz, k)
        else:
            self.inserir_nao_cheio(raiz, k)

    def inserir_nao_cheio(self, x, k):
        # x é o nó atual, k é o valor a ser inserido
        i = len(x.chaves) - 1
        
        if x.folha:
            # Se é folha, apenas encontramos a posição e inserimos
            x.chaves.append(0) # Espaço temporário
            while i >= 0 and k < x.chaves[i]:
                x.chaves[i + 1] = x.chaves[i]
                i -= 1
            x.chaves[i + 1] = k
        else:
            # Se não é folha, precisamos encontrar qual filho descer
            while i >= 0 and k < x.chaves[i]:
                i -= 1
            i += 1
            
            # Verifica se o filho onde vamos descer está cheio
            if len(x.filhos[i].chaves) == (2 * self.t) - 1:
                self.dividir_filho(x, i)
                # Após dividir, verificamos se o valor k é maior que o valor que subiu
                if k > x.chaves[i]:
                    i += 1
            
            self.inserir_nao_cheio(x.filhos[i], k)

    def dividir_filho(self, pai, i):
        # Esta função divide um filho cheio em dois e sobe o elemento do meio
        t = self.t
        y = pai.filhos[i]         # O filho cheio
        z = NoB(folha=y.folha)    # O novo irmão do filho cheio
        
        # O novo nó (z) recebe as chaves da metade superior de (y)
        # (t-1) é o ponto de corte para chaves restantes
        z.chaves = y.chaves[t:]
        
        # Se (y) não for folha, (z) também recebe os filhos correspondentes
        if not y.folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t] # Corta os filhos de y

        # A chave mediana sobe para o pai
        chave_mediana = y.chaves[t-1]
        
        # Ajusta as chaves de y (ficam apenas as da primeira metade)
        y.chaves = y.chaves[:t-1]

        # Insere o novo nó z como filho do pai
        pai.filhos.insert(i + 1, z)
        
        # Insere a chave mediana no pai
        pai.chaves.insert(i, chave_mediana)

    def imprimir_arvore(self, x, nivel=0):
        print(f"Nível {nivel}: {x.chaves}")
        if len(x.filhos) > 0:
            for filho in x.filhos:
                self.imprimir_arvore(filho, nivel + 1)

# --- EXECUÇÃO DO EXEMPLO ---

# Criamos uma árvore com grau mínimo 2.
# Isso significa que cada nó pode ter até 3 chaves (2*2 - 1).
# (Para simular estritamente o exemplo anterior de máx 2 chaves, 
# a lógica seria um pouco diferente, chamada Árvore 2-3, mas a B-Tree padrão é mais flexível).
b = ArvoreB(grau_minimo=2)

numeros = [10, 20, 5, 6, 12, 30, 7, 17]

print("--- Inserindo valores ---")
for n in numeros:
    print(f"Inserindo {n}...")
    b.inserir(n)

print("\n--- Estrutura Final da Árvore ---")
b.imprimir_arvore(b.raiz)


# As 4 Regras de Ouro

# Para uma árvore ser Rubro-Negra, ela deve seguir estas regras restritas:

#     Todo nó é Vermelho ou Preto.

#     A Raiz é sempre Preta.

#     Não existem dois vermelhos seguidos (um nó vermelho não pode ter filho vermelho).

#     Todo caminho da raiz até as folhas nulas deve ter o mesmo número de nós pretos.


class No:
    def __init__(self, dado, cor="VERMELHO"):
        self.dado = dado
        self.cor = cor  # Todo nó novo nasce Vermelho
        self.esq = None
        self.dir = None
        self.pai = None

class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(None, cor="PRETO") # Nó sentinela (folha vazia)
        self.raiz = self.NIL

    def inserir(self, dado):
        # 1. Inserção padrão de Árvore Binária de Busca
        novo_no = No(dado)
        novo_no.esq = self.NIL
        novo_no.dir = self.NIL
        
        pai = None
        atual = self.raiz
        while atual != self.NIL:
            pai = atual
            if novo_no.dado < atual.dado:
                atual = atual.esq
            else:
                atual = atual.dir
        
        novo_no.pai = pai
        if pai is None:
            self.raiz = novo_no
        elif novo_no.dado < pai.dado:
            pai.esq = novo_no
        else:
            pai.dir = novo_no

        # 2. Consertar a árvore para manter as regras
        self.consertar_insercao(novo_no)

    def consertar_insercao(self, k):
        while k.pai and k.pai.cor == "VERMELHO":
            # Se o pai do k é filho esquerdo do avô
            if k.pai == k.pai.pai.esq:
                tio = k.pai.pai.dir
                if tio.cor == "VERMELHO":
                    # CASO 1: O Tio é Vermelho -> Apenas recolorimos
                    tio.cor = "PRETO"
                    k.pai.cor = "PRETO"
                    k.pai.pai.cor = "VERMELHO"
                    k = k.pai.pai # Sobe para verificar o avô
                else:
                    # CASO 2: O Tio é Preto e k é filho da direita -> Rotação à Esquerda
                    if k == k.pai.dir:
                        k = k.pai
                        self.rotar_esquerda(k)
                    # CASO 3: O Tio é Preto e k é filho da esquerda -> Rotação à Direita
                    k.pai.cor = "PRETO"
                    k.pai.pai.cor = "VERMELHO"
                    self.rotar_direita(k.pai.pai)
            else:
                # Lógica espelhada para quando o pai é filho direito
                tio = k.pai.pai.esq
                if tio.cor == "VERMELHO":
                    tio.cor = "PRETO"
                    k.pai.cor = "PRETO"
                    k.pai.pai.cor = "VERMELHO"
                    k = k.pai.pai
                else:
                    if k == k.pai.esq:
                        k = k.pai
                        self.rotar_direita(k)
                    k.pai.cor = "PRETO"
                    k.pai.pai.cor = "VERMELHO"
                    self.rotar_esquerda(k.pai.pai)
            if k == self.raiz: break
        self.raiz.cor = "PRETO"

    def rotar_esquerda(self, x):
        y = x.dir
        x.dir = y.esq
        if y.esq != self.NIL:
            y.esq.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y

    def rotar_direita(self, x):
        y = x.esq
        x.esq = y.dir
        if y.dir != self.NIL:
            y.dir.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.dir:
            x.pai.dir = y
        else:
            x.pai.esq = y
        y.dir = x
        x.pai = y

    def exibir(self, no, indent="", ultimo=True):
        if no != self.NIL:
            print(indent, "R----" if ultimo else "L----", f"{no.dado}({no.cor})", sep="")
            indent += "     "
            self.exibir(no.esq, indent, False)
            self.exibir(no.dir, indent, True)

# --- Teste ---
arn = ArvoreRubroNegra()
for val in [10, 20, 30, 15, 25]:
    arn.inserir(val)

arn.exibir(arn.raiz)


# Em uma Heap, para qualquer posição i no array, você encontra os parentes usando fórmulas simples:

#     Filho da Esquerda: 2i+1

#     Filho da Direita: 2i+2

#     Pai: (i−1)//2

class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        # 1. Adiciona o valor no final da lista
        self.heap.append(valor)
        # 2. Faz o valor "subir" até o lugar certo
        self._subir(len(self.heap) - 1)

    def remover_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # 1. O menor valor é a raiz (índice 0)
        raiz = self.heap[0]
        # 2. Movemos o último elemento para a raiz
        self.heap[0] = self.heap.pop()
        # 3. Fazemos esse elemento "descer" para organizar a casa
        self._descer(0)
        
        return raiz

    def _subir(self, i):
        pai = (i - 1) // 2
        # Se o elemento for menor que o pai, eles trocam de lugar
        if i > 0 and self.heap[i] < self.heap[pai]:
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            self._subir(pai)

    def _descer(self, i):
        esq = 2 * i + 1
        dir = 2 * i + 2
        menor = i

        # Verifica se o filho da esquerda é menor que o atual
        if esq < len(self.heap) and self.heap[esq] < self.heap[menor]:
            menor = esq
        
        # Verifica se o filho da direita é ainda menor
        if dir < len(self.heap) and self.heap[dir] < self.heap[menor]:
            menor = dir

        # Se o menor não for o atual, troca e continua descendo
        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer(menor)

# --- Teste Prático ---
h = MinHeap()
valores = [50, 10, 20, 5, 30]

print("Inserindo:", valores)
for v in valores:
    h.inserir(v)

print("Estado do array da Heap:", h.heap)
print("Removendo o menor (prioridade):", h.remover_min())
print("Novo estado da Heap:", h.heap)

# Por que usar Heap?

#     Busca do Menor/Maior: É instantânea (O(1)).

#     Inserção e Remoção: Muito rápidas (O(logn)), mesmo com milhões de itens.

#     Sem Ponteiros: Como usamos uma lista ([]), não gastamos memória extra com objetos "Nó" ou ponteiros de "esquerda/direita".



# 1. O Conceito: A Operação Splay

# O "Splaying" (alargamento) consiste em três tipos de movimentos dependendo da posição do nó em relação ao seu pai e avô:

#     Zig: O nó é filho da raiz. Uma rotação simples resolve.

#     Zig-Zig: O nó e o pai estão na mesma direção (ambos filhos da esquerda ou ambos da direita).

#     Zig-Zag: O nó e o pai estão em direções opostas (um é filho da esquerda e o outro da direita).

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None

class ArvoreSplay:
    def __init__(self):
        self.raiz = None

    def _rotar_direita(self, x):
        y = x.esq
        x.esq = y.dir
        y.dir = x
        return y

    def _rotar_esquerda(self, x):
        y = x.dir
        x.dir = y.esq
        y.esq = x
        return y

    def splay(self, raiz, chave):
        # Caso base: árvore vazia ou a chave já é a raiz
        if raiz is None or raiz.chave == chave:
            return raiz

        # A chave está na subárvore à ESQUERDA
        if chave < raiz.chave:
            if raiz.esq is None: return raiz

            # Caso Zig-Zig (Esquerda-Esquerda)
            if chave < raiz.esq.chave:
                raiz.esq.esq = self.splay(raiz.esq.esq, chave)
                raiz = self._rotar_direita(raiz)
            # Caso Zig-Zag (Esquerda-Direita)
            elif chave > raiz.esq.chave:
                raiz.esq.dir = self.splay(raiz.esq.dir, chave)
                if raiz.esq.dir is not None:
                    raiz.esq = self._rotar_esquerda(raiz.esq)

            return self._rotar_direita(raiz) if raiz.esq else raiz

        # A chave está na subárvore à DIREITA
        else:
            if raiz.dir is None: return raiz

            # Caso Zig-Zag (Direita-Esquerda)
            if chave < raiz.dir.chave:
                raiz.dir.esq = self.splay(raiz.dir.esq, chave)
                if raiz.dir.esq is not None:
                    raiz.dir = self._rotar_direita(raiz.dir)
            # Caso Zig-Zig (Direita-Direita)
            elif chave > raiz.dir.chave:
                raiz.dir.dir = self.splay(raiz.dir.dir, chave)
                raiz = self._rotar_esquerda(raiz)

            return self._rotar_esquerda(raiz) if raiz.dir else raiz

    def buscar(self, chave):
        self.raiz = self.splay(self.raiz, chave)
        if self.raiz and self.raiz.chave == chave:
            return self.raiz
        return None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
            return

        # Traz o nó mais próximo (ou o próprio) para a raiz
        self.raiz = self.splay(self.raiz, chave)

        # Se a chave já existe, não faz nada
        if self.raiz.chave == chave: return

        novo = No(chave)
        if chave < self.raiz.chave:
            novo.dir = self.raiz
            novo.esq = self.raiz.esq
            self.raiz.esq = None
        else:
            novo.esq = self.raiz
            novo.dir = self.raiz.dir
            self.raiz.dir = None
        self.raiz = novo

    def imprimir(self, no, nivel=0, prefixo="Raiz: "):
        if no:
            print(" " * (nivel * 4) + prefixo + str(no.chave))
            if no.esq or no.dir:
                self.imprimir(no.esq, nivel + 1, "E-- ")
                self.imprimir(no.dir, nivel + 1, "D-- ")

# --- Teste Prático ---
splay_tree = ArvoreSplay()
elementos = [10, 20, 30, 40, 50]

for e in elementos:
    splay_tree.inserir(e)

print("Árvore após inserir até 50 (Note que o 50 virou raiz):")
splay_tree.imprimir(splay_tree.raiz)

print("\nBuscando o 20 (Ele deve subir para a raiz):")
splay_tree.buscar(20)
splay_tree.imprimir(splay_tree.raiz)


# Resumo das Árvores que vimos:

#     Árvore B: Para muitos dados no Disco (Bancos de dados).

#     Rubro-Negra: Para garantir tempo estável na Memória (Dicionários/Maps).

#     Heap: Para saber sempre quem é o Próximo (Filas de prioridade).

#     Splay: Para quando os dados mais Recentes são os mais importantes (Caches).