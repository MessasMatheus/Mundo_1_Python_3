# Desenvolva um programa que leia as quatro notas bimestrais de um aluno, transforme em notas semestrais e calcúle
# a media final do ano letivo.

print('Escola, Aviação!')
n1 = float(input('Digite a nota do 1º bimestre: '))
n2 = float(input('Digite a nota do 2º bimestre: '))
n3 = float(input('Digite a nota do 3º bimestre: '))
n4 = float(input('Digite a nota do 4º bimestre: '))

s1 = (n1 + n2)/2
s2 = (n3 + n4)/2
mf = (n1 + n2 + n3 + n4)/4

print('Esse aluno, tirou essas notas. 1º: {}, 2º: {}, 3º: {}, 4º: {}'.format(n1, n2, n3, n4))
print('A média do 1º semestre foi: {}, e a média do 2º semestre foi: {}'.format(s1, s2))
print('Consegiu essa média final : {}'.format(mf))
print('Agora é com você professor!!')
