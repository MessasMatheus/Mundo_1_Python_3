# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Conversor do sistema métrico!!!')

metros = float(input('Digite a medida em metros : '))

centimetros = metros * 100
milimetros = metros * 1000

print('A medida digitada foi: {: .0f} m'.format(metros))
print('Nessa medida você obtem: {:.0f} cm'.format(centimetros), end=' ')
print(', e: {:.0f} mm'.format(milimetros), end=' ')

print('Obrigado!')
