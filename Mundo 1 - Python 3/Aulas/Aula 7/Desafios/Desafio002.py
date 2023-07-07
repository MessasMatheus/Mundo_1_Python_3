# Crie um algoritimo que leia um número e mostre seu dobro, triplo e sua raiz quadrada.

print('Olá, me chamo BOB, e vou lhe ajudar a calcular o Dobro, o Triplo e a Raiz quadrada de um número.')
numero = float(input('Digite um número qualquer : '))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero**(1/2)
print('O número digitado foi: {}, seu dobro é: {}, seu triplo é: {} e sua raiz quadrada é: {:.2f}'.format(numero, dobro, triplo, raizquadrada))
print('Obrigado, tenha um ótimo dia!')
