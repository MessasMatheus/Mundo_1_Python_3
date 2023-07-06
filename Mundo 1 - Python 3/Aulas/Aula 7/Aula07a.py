# nome = input('Qual é o seu nome? ')
# Alinhamento de Strings
# print('Prazer em te conheçer {:20}!'.format(nome))  # String escrita com 20 caracteres.
# print('Prazer em te conheçer {:<20}!'.format(nome))  # String escrita com 20 caracteres e alinhada a esquerda.
# print('Prazer em te conheçer {:>20}!'.format(nome))  # String escrita com 20 caracteres e alinhada a direita.
# print('Prazer em te conheçer {:^20}!'.format(nome))  # String escrita com 20 caracteres e alinhada ao centro.
# String escrita com 20 caracteres e alinhada ao centro e entre "=".
# print("Prazer em te conheçer {:=^20}!".format(nome))

n1 = int(input('Digite um Valor : '))
n2 = int(input('Digite outro Valor : '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
# print('A soma entre {} e {} vale : {}'.format(n1, n2, n1+n2))
print('O cálculo entre {} e {} é: Soma: {}, Subtração:, {} Multiplicação: {}, Divisão: {}'.format(n1, n2, s, su, m, d))
print('O resultado entre {} e {} é: Divisão Inteira: {}, Potência: {}, Resto da Divisão: {}'.format(n1, n2, di, e, rd))
# Para colocar um limite de caracteres, dentro das chaves digite: "{:.2f}"(2 casas depois da virgula).
# Para não haver quebra de linha, após o comando .format(), digite: .format(), end=' ', ele da um espaço e ja coloca
# outro print. Se quiser quebrar uma linha no meio do print digite: \n, ele irá pular a linha nesse ponto.
