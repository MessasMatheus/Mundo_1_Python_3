# Desenvolva um programa que leia as quatro notas bimestrais de um aluno, transforme em notas semestrais e calcúle
# a media final do ano letivo.

print('Escola, Aviação!')
nota1 = float(input('Digite a nota do 1º bimestre: '))
nota2 = float(input('Digite a nota do 2º bimestre: '))
nota3 = float(input('Digite a nota do 3º bimestre: '))
nota4 = float(input('Digite a nota do 4º bimestre: '))

mediasemestre1 = (nota1 + nota2)/2
mediasemestre2 = (nota3 + nota4)/2
mediafinal = (nota1 + nota2 + nota3 + nota4)/4

print('Esse aluno, tirou essas notas. 1º: {}, 2º: {}, 3º: {}, 4º: {}'.format(nota1, nota2, nota3, nota4))
print('A média do 1º semestre foi: {}, e a média do 2º semestre foi: {}'.format(mediasemestre1, mediasemestre2))
print('Consegiu essa média final : {}'.format(mediafinal))
print('Agora é com você professor!!')
