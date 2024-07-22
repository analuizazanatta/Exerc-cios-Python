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

# Exercício 56 aula 13 
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

# Exercício 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

 
while True:

    nome_produto = str(input('Qual é o nome do produto? '))
    valor = float(input('Qual é o valor do produto? R$ '))

    pergunta = str(input('Deseja cadastrar mais produtos? [SIM / NÃO]: '))

    if pergunta != 'SIM':
        print('Encerrando a compra. ')







