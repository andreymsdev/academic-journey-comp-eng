'''
Crie um programa em Python que:

    Pergunte ao usuário o nome dele. ok

    Pergunte ao usuário para digitar uma expressão matemática (por exemplo: 2+3*4).

    Use eval para calcular o resultado dessa expressão.

    Mostre na tela uma mensagem personalizada com o nome do usuário e o resultado da conta.
'''

nome = input('Digite seu nome: ')
expressao = input('Digite uma expressão matemática: ')
resultado = eval(expressao)
print('Olá {}! O resultado da expressão é {}.'.format(nome, resultado))