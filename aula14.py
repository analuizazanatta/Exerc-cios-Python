# Aula 14: Repetição While

# Exercício 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
while True:
    sexo = str(input('Digite seu sexo [ M / F ]: ')).upper()

    if sexo == "M" or sexo == "F":
        print(f"Seu sexo é {sexo}")

        break

    else:
        print('Opção inválida! Tente novamente')

    # Como aqui não tem mais nada, vai iniciar o próximo loop
"""

# _________________________

# Exercício 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.
"""
from random import randint

while True:
    pergunta = str(input(f'Pensei em um número entre 0 e 10... Quer adivinhar? ')).upper()

    if pergunta == 'SIM':
        
        sorteio = randint(1, 10)

        tentativas = 0

        while True:

            num = int(input(f'Tente adivinhar o número que o computador pensou: '))
            
            if sorteio == num:
                print(f'você acertou na {tentativas + 1}ª tentativa{"s" if tentativas > 0 else ""}! O computador também pensou no número {sorteio}')

                break

            elif num > sorteio:
                print(f'Menos...Tente novamente!')

            elif num < sorteio:
                print(f'Mais...Tente novamente!')
            
            tentativas += 1

    elif pergunta == 'NÃO':
        print('OK!Encerrando o programa...')
        break 
        
    print('Carácter inválido... Tente novamente!')
"""

# _____________________________

# Exercício 59:Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

while True:

    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))

    while True:
        print('\nSelecione uma das opções:\n'
              '[ 1 ] somar\n'
              '[ 2 ] multiplicar\n'
              '[ 3 ] maior\n'
              '[ 4 ] novos números\n'
              '[ 5 ] sair do programa\n')

        opcao = int(input('Qual opção você escolhe? '))
        print()

        if opcao == 1:
            soma = num_1 + num_2
            print(f'A soma dos dois números deu {soma}.')

        elif opcao == 2:
            multiplicacao = num_1 * num_2
            print(f'A multiplicação dos dois números resultou em {multiplicacao}. ')

        elif opcao == 3:
            if num_1 == num_2:
                print('Os dois números são iguais. ')

            elif num_1 > num_2:
                print('O primeiro número é maior. ')

            else:
                print('O segundo número é maior. ')
        
        elif opcao == 4:
            print('Reiniciando o programa...')
            break

        elif opcao == 5:
            for i in reversed(range(1, 4)):
                print(i)
                sleep(1)
            print('Encerrando o programa...')
            exit()
        
        else:
            print('Opção inválida! Digite os números novamente')
"""

# __________________________

# Exercício 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
num = int(input('Digite um número: '))

cont = num
fatorial = num

while cont != 1:
    cont -= 1
    fatorial *= cont

print(fatorial)
"""

# ___________________________

# Exercício 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura while.

"""
primeiro = int(input('Digite o primeiro termo: '))   # De que número vai começar a contar.
razao = int(input('Digite a razão: '))               # De quantos em quantos números o contador vai contar.
decimo = primeiro + (10 - 1) * razao                 # Estipulo até que número o contador vai contar (Até que número).

# for c in range(primeiro, decimo + razao, razao):
#     print(c,  end=' -> ')

cont = primeiro

while cont <= decimo:
    print(cont,  end=' -> ')
    cont += razao
    
print('ACABOU!')

"""

# _________________________

# Exercício 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

"""
primeiro = int(input('Digite o primeiro termo: '))   # De que número vai começar a contar.
razao = int(input('Digite a razão: '))               # De quantos em quantos números o contador vai contar.
decimo = primeiro + (10 - 1) * razao                 # Estipulo até que número o contador vai contar (Até que número).

# for c in range(primeiro, decimo + razao, razao):
#     print(c,  end=' -> ')

cont = primeiro

termos = decimo - razao

while True:
    while cont <= decimo:
        print(cont,  end=' -> ')
        cont += razao

    continuacao = str(input('Quer continuar vendo termos? ')).upper()
    if continuacao != 'SIM':
        break
    
    decimo += termos

        
print('ACABOU!')
"""

# _________________________

# Exercício 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""
num = int(input('Digite um número: '))

fibonacci = [0, 1]

while True:
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    if proximo_termo > num:
        break
    fibonacci.append(proximo_termo)

print(f'A sequência de Fibonacci até {num} é:\n{" -> ".join([str(i) for i in fibonacci])}')

"""
# _________________________

# Exercício 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
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

# ____________________________

# Exercício 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""
numeros = []

while True:
    quantidade_numeros = int(input('Deseja ler quantos números? '))

    for c in range(quantidade_numeros):
        num = int(input(f'Digite o {c + 1}° número: '))
        numeros.append(num)

    media = sum(numeros) / len(numeros)
    print(f'A média dos valores é de {media}. ')

    numeros = sorted(numeros)

    print(f'O maior dos números foi {numeros[-1]} e o menor número foi {numeros[0]}')



    pergunta = str(input('Deseja digitar mais números? ')).upper()

    if pergunta != 'SIM':
        print('Encerrando o programa...')
        break
 """   

# _______________________
