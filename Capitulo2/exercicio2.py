# Exercicio 2.1 Suponha que voce esteja criando um aplicativo para acompanhar suas finanças , todos os dias você devera revisar os seus gastos e resumir quanto gastou. Logo, você terá um monte de inserções e poucas leituras. você devera usar um array ou uma lista para implementar esse aplicativo?

# Para um aplicativo onde eu priorize inserções de registros em detrimento de leituras dos mesmos , devo usar uma lista pois seu tempo de execução é constante na inserção, como sera feita leitura de todos os itens , a lista tambem tera uma boa velocidade de leitura.

# Exercicio 2.2 Suponha que voce esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante. seu aplicativo precisa de uma lista de pedidos. Os garçons adicionam os pedidos a essa lista e os chefes retiram os pedidos da lista. Funciona como uma fila os gaçons colocam os pedidos no final fila e os chefes retiram os pedidos do começo dela para cozinha-los. você usaria um array ou uma lista encadeada para implementar essa lista?

# Usaria a lista encadeada pois o tipo de acesso feito é sequencial , os pedidos novos sempre estaram no final e os que forem executados sempre estarão no inicio da fila.

# Exercicio 2.3 As pessoas acessam o facebook com muita frequência , então existem muitas buscas nessa lista , presuma que o facebook usa a pesquisa binara para procurar um nome na lista , a pesquisa binaria requer acesso aleatorio - voce precisa ser capaz de acessar o meio da lista de nomes instantaneamente , sabendo disso , voce implementaria essa lista como um array ou uma lista encadeada?

# Implementaria como um array ordenado visto que o seu tipo de acesso é aleatorio e isso permite que eu possa acessar qualquer ponto da lista sem precisar passar previamente por outros valores anteriores , que é o caso da lista encadeada.

# Exercicio 2.4 As pessoas se inscrevem no facebook com muita frequencia tambem. suponha que você decida usar um array para armazenar a lista de usuarios. Quais as desvantagens de um array em relação as inserções ?? em particular , imagine que você esta usanda a pesquisa binara para buscar os logins. o que acontece quando você adiciona usuarios em um array?

# Se usar um array para armazenar os usuários o tipo de acesso será linear por conta da necessidade de especificar a posição onde o valor sera inserido tornado a inserção lenta, se usar a pesquia binaria no array para procura nomes , o array devera estar ordenado, visto que um novo registro será inserido no fim , requerendo uma ordenação toda vez que um nome for inserido.

# Exercicio 2.5 Na verdade , o facebook não usa nem arrays nem listas encadeadas para armazenar informações. vamos considerar uma estrutura de dados hibrida  um array de listas encadeadas. você tem um array de 26 slots,  suponha que Adit b se inscreva no facebook e voce queira adiciona-lo a lista voce vai ao slot1 do array a seguir para lista encadeada do slot 1  e, adiciona Adit b no final . agora suponha que voce queira procurar  o Zakhir H. você vai ao slot 26, que aponta par a lista encadeada de todos os nomes começados em Z. entao procura pela lista até encontrar o Zakhir H. É mais lento ou mais rápido fazer inserções e eliminações nesse caso ? 

#Para buscas - mais lenta do que arrays , mais rapida do que listas encadeadas. Para inserções - mais rapida do que arrays mesmo tempo as listas encadeadas. portanto é mais lenta para buscas do que arrays , porém mais rápida ou igual as listas encadeadas para tudo. Os arrays e listas encadeadas são blocos fundamentais para estruturas de dados mais complexas.