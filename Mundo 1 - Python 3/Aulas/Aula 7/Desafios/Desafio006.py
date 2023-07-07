# Crie um programa que leia quanto dinheiro o usuario possui e mostre na tela quantos dolares ele conseguiria comprar.
# considere o dolar a US$ 1,00 = R$ 4.88 (Pesquisa 07/07/2023)

print('Conversor de Dolar!')
print('Bom dia, bem vindo ao Cambio, "VAMOS VIAJAR" ')

reais = float(input('Quantos reais você possui? : '))

dolar = reais / 4.88

print('Adicionado na conta R${}'.format(reais))
print('Você pode comprar US${:.2f}'.format(dolar))
print('Vá até o caixa da retirada! Obrigado!')