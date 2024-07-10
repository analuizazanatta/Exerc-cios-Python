# AULA 13 - ESTRUTURA DE REPETIÇÃO FOR

#  Exercício 46: Contagem regressiva

"""from time import sleep

lista = list(reversed(range(1, 11)))

for num in lista:
    print(num)
    sleep(1)"""

"""rom time import sleep

timer = int(input('De 1 a 60, quantos segundos tem o seu temporizador? '))

if 0 < timer < 61:
    lista = list(reversed(range(1, timer + 1)))

    for num in lista:
        print(num)
        sleep(1)

else:
    ('NÚMERO INVÁLIDO.')"""

# _______________________________

# Exercício 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

"""from time import sleep
pergunta = input('Quer ver o computador contar os números pares até 50? ').upper()

if pergunta == 'SIM':
    print('Ok, só um momento! ')
    sleep(3)
    for par in range(0, 50, 2):
        print(par)
        sleep(1)

else:
    print('Ok')"""


# Jeito Guanabara:   

"""for n in range(2, 51, 2 ):
        print(n,  end=' ')

print('Acabou! ')"""

# _____________________________

# Exercício 48: Faça um programa que calcule a soma entre todos os números que são 
# múltiplos de três e que se encontram no intervalo de 1 até 500.


"""cont = 0
for c in range(3, 501, 3):
    cont += c
    print(f"C vale {c} -> Contador = {cont}")"""

# Não fez

# _____________________________

# Exercício 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""num = int(input('Qual tabuada você deseja? De 1 a 10: '))

for n in range(0, 11):
    print(f'{num} x {n} = {num * n}')"""
    

# ______________________________

# Exercício 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

"""soma = 0
cont = 0
for c in range(6):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Você informou 6 números nos quais {cont} foram pares. A soma deles resulta em {soma}. ')"""
    
# _______________________________

# Exercício 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

"""primeiro = int(input('Digite o primeiro termo: '))   # De que número vai começar a contar.
razao = int(input('Digite a razão: '))                  # De quantos em quantos números o ocntador vai contar.
decimo = primeiro + (10 - 1) * razao                    # Estipulo até que número o contador vai contar (Até que número).

for c in range(primeiro, decimo + razao, razao):
    print(c,  end=' -> ')

print('ACABOU!')"""

# Exercício 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Número primo é aquele divisível por ele mesmo e por 1;

"""num = int(input('Digite um número: '))
 
cont = num

while cont > 0:
    # 1. Verifica se o cont é igual ao num (se é 7/7)
    # 2. Verifica se o cont é igual a 1 (se é 7/1)
    # 3. Verifica se o resto da divisão do num pelo cont é igual a 0 (divisão exata)

    if (cont != num) and (cont != 1) and (num % cont == 0):
        print(f'NÃO É PRIMO -> divisível por {cont}')
        exit()

    print(f'{num} resto da divisão por {cont} é igual a {num % cont}')
    
    cont -= 1
    
print('É PRIMO')"""





# ____________________________

# Exercício 53: 