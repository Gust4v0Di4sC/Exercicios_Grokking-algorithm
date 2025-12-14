#Exemplo: Pilha de chamada
# def sauda(nome):
#     print("Olá , "+nome+" !")
#     sauda2(nome)
#     print("preparando para dizer tchau...")
#     tchau()
    
# Exercicio 3.1 Pilha de chamada exemplo 
# |    Sauda2()   |
# |  nome:maggie  |
# |    Sauda()    |
# |  nome:maggie  |
# Quais informações você pode retirar baseando-se apenas nesta pilha de chamada?

# A função Sauda é chamada primeiro como o nome maggie em seguida a funcao sauda2 é chamada também como o nome maggie  , neste ponto a função sauda está em um estado incompleto e suspenso, a chamada atual é sauda2 , apos finalizada sauda será retomada.


#Pilha de chamada com recursão
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

print(fat(3))


#Exercicio 3.2 Suponha que voce acidentalmente escreva uma função recursiva que fique executando  infinitamente. como você viu , seu computador aloca memoria na pilha para cada chamada de função o que acontece com a pilha quando a função recursiva fica executando inifinitamente?

# estoura , não havera mais espaço para continuar executando a recursão , em função disso acontece uma sobrecarga e o codigo para de executar