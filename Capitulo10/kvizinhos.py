#10.1

# pode ser usado normalização nesse caso , observamos as avaliações media para cada pessoa  e usuamos este valor como escala para as avaliações . por exemplo a maioria das avaliaçõs de pinky  é 3 , enuqnato o valor médio de yogi é 3,5. portanto você aumenta um pouco as avaliações de pinky ate que sua media tambem seja 3,5 ai entao é possivel comparar as avaliações na mesma escala

#10.2

# daria maior peso para as avaliações dos influenciadores usando algoritmo dos k-vizinhos imagine que você tenha três vizinhos : joe ,dave e we anderson (influenciador). eles avaliaram clube dos pilantras como 3, 4 e 5 respectivamente . em vez de calcular a média das avaliações (3+4+5/3 = 4), você poderia dar maior peso para a avaliação de wes anderson: 3+4+5+5+5/5 = 4,4 


#classificação = classificar em grupos
#regressão = advinhar uma resposta ( como um número )

#Caracteristicas certas a serem comparadas :

#Caracteristicas diretamente correlacionadas aos filmes que você está tentando recomendar.

#Caracteristicas imparciais (se as unicas opções fornecidas aos usuarios forem filmes de comedia , esta avaliação nao fornecera nenhuma informação util sobre o gosto dos usuarios em relação a filmes de ação por exemplo)

#10.3 
# baixo demais se você olhar para menos vizinhos, haverá uma chance maior de que o resultado seja tendencioso. uma boa regra éa seguinte : se você tem N usuarios deve considerar sqrt(n) vizinhos