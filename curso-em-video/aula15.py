# Aula 15: Instrução Break e novas f'strings.

# __________________________

# Exercício 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

"""
num = cont = soma = 0

while True:
    num = int(input('Digite um número qualquer e "999" para acabar o programa: '))

    if num == 999:
        print('O programa não aceita mais números!!! ')
        break

    cont += 1
    soma += num

print(f'Você digitou {cont} números. A soma de todos eles fica {soma}')
"""

# _______________________

# Exercício 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.

"""
while True:
    pergunta = int(input('Você deseja ver a tabuada do número: '))

    if pergunta < 0:
        print('Número negativo! Encerrando o programa...')
        break

    for tabuada in range(1, 11):
        print(f'{pergunta} x {tabuada} = {pergunta * tabuada}')
"""

# _________________________

# Exercício 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep

print(f'{20 * '=-'}')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(f'{20 * '=-'}')


while True:
    num = int(input('Qual número você quer jogar? '))
    pergunta = str(input('Qual você acha que vai cair? Par ou ímpar: ')).upper()
    
    sorteio = randint(1, 10)
    print(f'\nComputador jogou = {sorteio}')

    soma_num_dedos = num + sorteio
    print(f'A soma dos números deu {soma_num_dedos}\n')

    if pergunta == 'PAR':
        if soma_num_dedos % 2 == 0:
            print('Usuário ganhou! O computador escolheu Ímpar. ')
        else:
            print('Computador ganhou! Ele escolheu ímpar. ')
            

    if pergunta == 'ÍMPAR':
        if soma_num_dedos % 2 != 0:
            print('Usuário ganhou! O computador escolheu Par. ')
        else:
            print('Computador ganhou! Ele escolheu par. ')
            

    pergunta = str(input('Deseja jogar mais uma vez? ')).upper()

    if pergunta != 'SIM':
        print('Encerrando o programa...')
        break
"""
    
# _________________________

# Exercício 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
 
"""
contpessoas_maiores_18 = 0
cont_mulheresmenores_20 = 0
cont_homens = 0

while True:

    idade = int(input('Digite a idade: '))
    sexo = str(input('Informe o sexo [F / M]: ')).upper()

    pergunta = str(input('Deseja continuar cadastrando? [SIM / NÃO]: ')).upper()

    if pergunta != 'SIM':
        print('Encerrando o programa...')
        break

    if idade > 18:
       contpessoas_maiores_18 += 1

    if sexo == 'F' and idade < 18:
        cont_mulheresmenores_20 += 1

    if sexo == 'M':
        cont_homens += 1

print(f'Total de pessoas maiores de 18 anos: {contpessoas_maiores_18}')
print(f'Total de mulheres menores de 20 anos: {cont_mulheresmenores_20} ')
print(f'Total de homens cadastrados: {cont_homens} ')
"""
# _____________________________

# Exercício 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

"""
valor_total = 0
produto_maisde_mil = 0
produto_barato_nome = ''
produto_barato_valor = 0

while True:

    nome = str(input('Qual é o nome do produto? '))
    valor = float(input('Agora digite o valor: R$ '))


    # a)

    valor_total += valor

    # b)

    if valor > 1000:
        produto_maisde_mil += valor

    # c)

    if produto_barato_nome == "" or valor < produto_barato_valor:
        produto_barato_nome = nome
        produto_barato_valor = valor

    pergunta = str(input('Deseja cadastrar mais produtos? [SIM / NÃO]: ')).upper()

    if pergunta != 'SIM':
        print('Encerrando a compra. ')
        break

    
print(f'Total gasto na compra R${valor_total:.2f}')
print(f'{produto_maisde_mil} produtos custam mais de R$1.000,00')
print(f'O produto mais barato é o {produto_barato_nome}, custando R${produto_barato_valor:.2f}')
"""

# ____________________________

# Exercício 71: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

"""
valor_saque = int(input('Qual é o valor do saque? R$ '))

cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0

while valor_saque > 0:
    cedula50 = valor_saque // 50
    valor_saque = valor_saque % 50

    cedula20 = valor_saque // 20
    valor_saque = valor_saque % 20

    cedula10 = valor_saque // 10
    valor_saque = valor_saque % 10

    cedula1 = valor_saque // 1
    valor_saque = valor_saque % 1    

print(f'Cédulas de R$50: {cedula50}')
print(f'Cédulas de R$20: {cedula20}')
print(f'Cédulas de R$20: {cedula10}')
print(f'Cédulas de R$2: {cedula1}')
"""

