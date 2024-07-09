# Exercício 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


"""from random import choice 

num = int(input('Tente adivinhar que número o computador pensou: '))

lista = list(range(1, 6))

sorteio = choice(lista)

if sorteio == num:
    print(f'você acertou, o computador também pensou no número {sorteio}')

else: 
    print(f'Você errou, o computador pensou no número {sorteio}')"""

# ________________________________
 
# Exercício 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

"""velocidade = float(input('Qual a velocidade que seu carro estava? '))

multa = (velocidade - 80) * 7

print(multa)

if velocidade > 80: 
    print(f'Você foi MULTADO! Sua multa é de R$ {multa} reais.')

else:
    print('Você estava no limite, o sistema não apresenta multas.')"""

# _______________________________

# Exercício 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""num = int(input('Digite um número qualquer: '))

if num % 2 == 0:
    print(f'Este número é PAR!')

else:
    print('Este número é ÍMPAR')"""

# _______________________________

# Exercício 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

"""km = float(input('Quantos km sua viagem vai ter? '))

if km <= 200:
    condicao = km * 0.50
    print(f'Sua passagem vai custar R$ {condicao}')

else:
    condicao2 = km * 0.45
    print(f'Sua viagem ultrapassa 200km que sai com preço promocional! Ela vai custar R$ {condicao2}')"""

# _________________________________

# Exercício 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

"""from datetime import date

ano = int(input('Digite um ano qualquer: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é BISSEXTO.')

else:
    print('Este ano não é Bissexto.')"""

# ____________________________________

# Exercício 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor

"""
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

# Menor: 

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

# Maior:

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print(f'O maior número entre os três é o {maior}. ')
print(f'O menor número entre os três é o {menor}. ')"""

# ______________________________

# Exercício 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

"""salario = float(input('Quanto o funcionário recebe atualmente? R$ '))

if salario > 1250:
    aumento = salario * 10 / 100
    print(f'O aumento no salário vai ser de R$ {aumento}')

else:
    aumento = salario * 15 / 100
    print(f'O aumento no salário vai ser de R$ {aumento}')"""

# _______________________________

# Exercício 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

"""r1 = float(input('Defina o primeiro ângulo: '))
r2 = float(input('Defina o segundo ângulo: '))
r3 = float(input('Defina o terceiro ângulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses ângulos podem formar um triângulo')

else:
    print('Esses ângulos não podem formar um triângulo')"""







