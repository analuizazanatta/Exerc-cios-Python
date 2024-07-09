# Exercício 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""from math import trunc

num = float(input('Digite um número: '))

print(f'A porção inteira do número {num} é {trunc(num)}. ')"""

# _____________________________

# Exercicío 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

"""import math

ca = float(input('Digite a medida do cateto adjacente: '))

co = float(input('Digite a medida do cateto oposto: '))

# h = (ca ** 2 + co ** 2) ** (1/2) *Solução sem importação de biblioteca

h = math.hypot(ca, co)
# h = round(h, 2) *Para deixar com duas casas decimais

print(f'A Hipotenusa dos catetos adjacente ({ca}) e co ({co}), formam a hipotenusa {h:.2f}. ')"""

# ______________________________

# Exercício 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tan = math.tan(math.radians(angulo))

print(f'O seno do ângulo {angulo} informado é {seno:.2f}.')
print(f'O cosseno do ângulo {angulo} informado é {cosseno:.2f}.')
print(f'A tangente do ângulo {angulo} informado é {tan:.2f}.')"""

# _______________________________

# Exercício 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""from random import choice

aluno1 = input('DIgite o nome do primeiro aluno: ')
aluno2 = input('DIgite o nome do segundo aluno: ')
aluno3 = input('DIgite o nome do terceiro aluno: ')
aluno4 = input('DIgite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = choice(lista)

print(f'O aluno sorteado foi {sorteio}! ')"""

# ________________________________

# Exercício 20: 

"""from random import shuffle

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista) 

print(f'A ordem de apresentação dos trabalhos é {lista}. ')"""

# _________________________________

# Exercício 21:


