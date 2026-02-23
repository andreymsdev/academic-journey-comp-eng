'''
Exemplo: tendo como dados de entrada a altura e o sexo de uma pessoa, construa um programa em Python que calcule seu peso ideal, utilizando para isso as seguintes fórmulas:
- Para homens: (72.7 * altura) - 58
- Para mulheres: (62.1 * altura) - 44.7
'''

genero = input('Qual seu gênero? (masc/fem)').lower().strip()
altura = float(input('Digite sua altura: '))
masc = (72.7 * altura) - 58
fem = (62.1 * altura) - 44.7
if genero == 'masc':
    print('Seu peso ideal é {}'.format(masc))
elif genero == 'fem':
    print('Seu peso ideal é {}'.format(masc))
else:
    print ('Algo deu errado. Tente novamente.')