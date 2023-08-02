# Faça um algoritimo que leia o salário de um funcionário e faça o acréscimo de 15%.

print('--- Acrécimo de 15% de Salário!')

salario = float(input('Insira o salário atual : '))

acrescimo = (salario * 15)/100

print('O valor atual do salário é de R${:.2f}, e terá um acréscimo de R${:.2f}'.format(salario, acrescimo))

salariofinal = salario + acrescimo

print('Pronto o valor foi ajustado para R${:.2f}'.format(salariofinal))
print('Obrigado!')
