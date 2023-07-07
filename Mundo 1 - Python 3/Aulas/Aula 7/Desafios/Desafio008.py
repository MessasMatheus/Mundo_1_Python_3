# Faça um algoritimo que leia o preço de um produto e mostre seu valor novo com 5% de desconto.

print('----- Vasos da Betina -----')
preco = float(input('Digite o preço do vaso escolhido : '))

desconto = (preco * 5)/100

print('Hoje os vasos estão com 5% de desconto. Preço original: R${:.2f}, desconto: R${:.2f}'.format(preco, desconto))

precofinal = preco - desconto

print('Valor do seu vaso ficará R${:.2f}!'.format(precofinal))
print('Obrigado por comprar conosco! Dirija-se ao pacote para pegar seu vaso')
