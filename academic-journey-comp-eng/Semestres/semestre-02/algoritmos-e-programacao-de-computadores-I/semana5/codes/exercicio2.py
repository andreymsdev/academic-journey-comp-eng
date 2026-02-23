'''
Faça um programa em Python que leia duas notas N1 e N2 de um aluno, e informe se ele foi aprovado ou não numa disciplina.
Considere que a média final é dada pela equação:
    media = 0,4 * N1 + 0.6 * N2
E que o aluno está aprovado se a média for maior ou igual a 5.0, e reprovado caso contrário.
'''

n1 = float(input('Digite sua nota 1: '))
n2 = float(input('Digite sua nota 2: '))
media = 0.4 * n1 + 0.6 * n2

if media >= 5:
    print('Você está aprovado')
elif media <= 5: 
    print('Você está reprovado')
elif media ==5:
    print('Você está aprovado.')
else: 
    print('Ocorreu um erro, tente novamente.')