# 1. Importar as bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 2. Carregar o dataset Iris
iris = load_iris()
X = iris.data  # As características (tamanho da pétala, etc.)
y = iris.target # Os rótulos (qual é a espécie da flor)

# 3. Dividir os dados em treino e teste
# 80% para treino e 20% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criar o modelo KNN
# Vamos definir k=3 (olhar para os 3 vizinhos mais próximos)
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# 5. Treinar o modelo
knn.fit(X_train, y_train)

# 6. Fazer previsões
y_pred = knn.predict(X_test)

# 7. Avaliar a precisão
acuracia = accuracy_score(y_test, y_pred)

print(f"Acurácia do modelo com k={k}: {acuracia * 100:.2f}%")

# --- Teste com um exemplo novo e fictício ---
# Digamos que temos uma flor com sépala 5x3cm e pétala 1x0.2cm
nova_flor = [[5.1, 3.5, 1.4, 0.2]] 
previsao = knn.predict(nova_flor)
nome_especie = iris.target_names[previsao][0]

print(f"A nova flor foi classificada como: {nome_especie}")