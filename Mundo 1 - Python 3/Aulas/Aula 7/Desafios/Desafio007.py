# Faça um programa que leia a Largura e a Altura de uma parede em metros, calcule sua Área e a quantidade
# nescessária de tinta para pinta-la. Considere 1 litro (tinta) = 2 metros quadrados (pintados).

print('Loja de Tintas do Edu! Bem Vindo!')

altura = float(input('Qual é a altura da parede? : '))
largura = float(input('Qual é a largura da parede? : '))

area = largura * altura
tinta = area/2
galao = tinta/10

print('Sua parede tem {:.2f} m²'.format(area))
print('Você irá precisar de {:.2f} l de tinta'.format(tinta))
print('Você precisará de {:.2f} Latas de tinta!'.format(galao))

print('Tinta separada, dirija-se ao caixa, e logo após retire sua tinta no guiche 4')
print('Aconselhamos sempre a comprar uma lata extra pois as cores podem variar na mistura!')
print('Obrigado!')
