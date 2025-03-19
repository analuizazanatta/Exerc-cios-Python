# MUNDO 2

# Exercício 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""
valor_casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Quanto você recebe mensalmente? R$ '))
anos = int(input('Em quantos anos planeja pagar? '))

prestacao = valor_casa / (anos * 12)
porcentagem = salario * 30 / 100

if prestacao > porcentagem:
    print(f'Empréstimo negado! O valor da casa de R${valor_casa} excede 30% ou mais do seu salário de {salario}. ')

else:
    print(f'Aprovado! O valor da prestação R$ {prestacao} não excede 30 % do seu salário de R$ {salario}.')"""

# __________________________________

# Exercício 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

"""num = int(input('Digite um número inteiro: '))
conversao = int(input('Para qual base você deseja converter? 1, 2 ou 3? '))

if conversao == 1:
    condicao_1 = bin(num)
    print(f'Você escolheu a opção 1 (Binário). O número que você digitou convertido fica {condicao_1}')

elif conversao == 2:
    condicao_2 = oct(num)
    print(f'Você escolheu a opção 2 (Octal). O número que você digitou convertido fica {condicao_2}')

elif conversao == 3:
        condicao_3 = hex(num)
        print(f'Você escolheu a opção 3 (Hexadecimal). O número que você digitou convertido fica {condicao_3}')

else:
     print('Opção inválida, TENTE NOVAMENTE')"""

# __________________________

# Exercício 38 Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais;

"""num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 < num2:
    print(f'{num2} é maior. ')

elif num1 > num2:
    print(f'{num1} é maior.')

else:
    print('Os dois valores são iguais.')"""

# ___________________________

# Exercício 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
# se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date 

data_atual = date.today().year

ano_nascimento = int(input('Em que ano você nasceu? '))

idade = data_atual - ano_nascimento

print(idade)

if idade < 18:
    print(f'Você ainda não pode se alistar, não completou 18 anos ainda.')

elif idade == 18:
    print(f'Você completou 18 anos esse ano, deve se alistar! ')

elif idade > 18:
    print(f'Você tem {idade} anos e não fez alistamento, o prazo de idade já passou.')"""

# ______________________________

# Exercício 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

"""nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Você está APROVADO! Sua média foi {media}. ')

elif media > 6 and media < 7:
    print(f'Você está em recuperação! Sua média foi {media}. ')

elif media < 6:
    print(f'Você está REPROVADO. Sua média ficou abaixo do esperado: {media}')"""

# ______________________
 
# Exercício 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

"""from datetime import date
atual = date.today().year

ano_nascimento = int(input('Digite o ano do seu nascimento para verificar em qual classificação você se encaixa: '))

idade = atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos, se encaixa na categoria até 9 anos: MIRIM')

elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos, se encaixa na categoria até 14 anos: INFANTIL')

elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos, se encaixa na categoria até 19 anos: JÚNIOR')

elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} anos, se encaixa na categoria até 25 anos: SÊNIOR')

else:
    print(f'Você tem {idade} anos, se encaixa na categoria 25 ou mais: MASTER')"""

# _________________________

# Exercício 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

"""r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses lados podem formar um triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO')

    elif (r1 == r2 and r3 != r1) or (r1 == r3 and r2 != r1) or (r2 == r3 and r1 != r2):
        print('ISÓSCELES')
    
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    
    else:
        print('TRIÂNGULO NÃO PODE SER FORMADO')
else:
    print('Esses ângulos não podem formar um triângulo')"""


# ___________________________

# Exercício 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
#  mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

"""peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Seu imc é {imc:.2f}. Você está abaixo do PESO IDEAL. ')

elif  18.5 < imc <= 25:
    print(f'Seu IMC é {imc:.2f}. Você está no PESO IDEAL. ')

elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.2f}. Você está SOBREPESO. ')

elif 30 < imc <= 40:
    print(f'Seu imc é {imc:.2f}. Você está em OBESIDADE. ')

else:
    print(f'Seu imc é {imc:.2f}. Você está em OBESIDADE MÓRBIDA')"""

# ____________________________________

# Exercício 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

"""produto = input('Qual é o produto? ')
valor_produto = float(input('Qual é o valor dele? R$ '))
print('Opção de pagamento: \n'
      '[1] À vista no dinheiro: 10% de desconto;\n'
      '[2] À vista no cartão: 5% de desconto;\n'
      '[3] Em até 2x no cartão: Preço normal;\n' 
      '[4] 3x ou mais no cartão: 20% de juros;')

opcao_pagamento = input('Qual a forma de pagamento? ')

if opcao_pagamento == '1':
    condicao = valor_produto - (valor_produto * 10 / 100)
    print(f'Opção de pagamento 1: Você ganhou 10% de desconto no valor da sua compra! O total a pagar fica R$ {condicao:.2f}')

elif opcao_pagamento == '2':
    condicao = valor_produto - (valor_produto * 5 / 100)
    print(f'Opção de pagamento 2: Você ganhou 5% de desconto no valor da sua compra! O total a pagar fica R$ {condicao:.2f}')

elif opcao_pagamento == '3':
    print(f'Opção de pagamento 3: O valor total da compra fica R$ {valor_produto:.2f}')

elif opcao_pagamento == '4':
    condicao = valor_produto + (valor_produto * 20 / 100)
    print(f'Opção de pagamento 4: Taxa do cartão em 20% de juros. O valor total da sua compra fica R$ {condicao:.2f}')

else:
    print('OPÇÃO INVÁLIDA!')"""

# __________________________

# Exercício 45: Crie um programa que faça o computador jogar Jokenpô com você.

"""from random import choice

lista = ['pedra', 'papel', 'tesoura']

opcao = choice(lista)

print('Vamos Jogar Jokenpô!')
opcao_usuario = input('Você escolhe pedra, papel ou tesoura? ')

if opcao == opcao_usuario:
    print('Empatou! Jogue novamente.')

elif opcao == 'pedra' and opcao_usuario == 'papel':
    print('Usuário ganhou!')
    print(f'O computador escolheu {opcao}.')

elif opcao == 'pedra' and opcao_usuario == 'tesoura':
    print('Computador ganhou!')

elif opcao == 'papel' and opcao_usuario == 'pedra':
    print('Computador ganhou')

elif opcao == 'papel' and opcao_usuario == 'tesoura':
    print('Usuário ganhou')
    print(f'O computador escolheu {opcao}. ')

elif opcao == 'tesoura' and opcao_usuario == 'pedra':
    print('Usuário ganhou')
    print(f'O computador escolheu {opcao}. ')

elif opcao == 'tesoura' and opcao_usuario == 'papel':
    print('Computador ganhou')

else:
    print('Opção INVÁLIDA! TENTE NOVAMENTE.')"""


