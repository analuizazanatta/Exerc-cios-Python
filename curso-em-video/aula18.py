# Aula 18: Parte 2 do assunto de listas

# Exercío 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

"""
nome_e_peso = []
pessoas_mais_pesadas = []
pessoas_mais_leves = []
cont_pessoas = 0

while True:
    nome = input('Informe o nome: ')
    peso = float(input('Informe seu peso: '))
   
    lista_pessoas = [nome, peso]
    print(lista_pessoas)

    nome_e_peso.append(lista_pessoas)
    print(nome_e_peso)

    if peso > 60:
        pessoas_mais_pesadas.append(nome)
    else:
        pessoas_mais_leves.append(nome)

    cont_pessoas += 1

    pergunta = input('Deseja continuar cadastando? ').upper()

    if pergunta != 'SIM':
        break

print('-=' * 40)
print(f'{cont_pessoas} pessoas foram adicionadas na lista. ')
print(f'As pessoas mais pesadas são {", ".join(pessoas_mais_pesadas)} ')
print(f'As pessoas mais leves são {", ".join(pessoas_mais_leves)}')
"""
    
# _______________________

# Exercício 5: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.
"""
# 0 - Ímpares | 1 - Pares
lista = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}° valor: '))

    if num % 2 != 0:
        lista[0].append(num)

    else:
        lista[1].append(num)

print(lista)
print(lista[0])
print(lista[1])
"""
# _________________________

# Exercício 86: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta

"""matrix = [
   # 0, 1, 2
    [0, 0, 0], # 0
    [0, 0, 0], # 1
    [0, 0, 0]  # 2
]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para as posições [{l} e {c}]: '))

print('-=' * 40)

for linha in matrix:
    for valor in linha:
        print(f'[{valor:^5}]', end="")
    print()
"""

# ________________________

# Exercício 87: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
"""
soma_pares = 0
soma_coluna = 0

matrix = [
   # 0, 1, 2
    [0, 0, 0], # 0
    [0, 0, 0], # 1
    [0, 0, 0]  # 2
]

# matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para as posições [{l} e {c}]: '))
        matrix[l][c] = num

        # A) A soma de todos os valores pares digitados.
        if num % 2 == 0:
            # soma_pares = soma_pares + num
            soma_pares += num
            
        # B) A soma dos valores da terceira coluna.
        if c == 2:
            soma_coluna += num
            
        # C) O maior valor da segunda linha.
        if l == 1 and c == 2:
            maior_num = sorted(matrix[1])[-1]
        
            
print('-=' * 40)

for linha in matrix:
    for valor in linha:
        print(f'[{valor:^5}]', end="")
    print()
           
print(f'A soma de todos os valores pares digitados foi de {soma_pares}. ')
print(f'A soma dos valores da terceira coluna foi de {soma_coluna}. ')
print(f'O maior valor da segunda linha é o número {maior_num}. ')"""

# _________________________

# Exercício 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

# Jogo usuário:

jogos = []

quantidade_palpites = int(input('Quantos palpites você deseja sortear? '))

for i in range(quantidade_palpites):
    jogo = []

    for _ in range(6):
        num = randint(1, 60)
        jogo.append(num)

    jogos.append(jogo)

    print(i, jogo)


indice = int(input('Qual jogo você deseja apostar? '))
jogo_usuario = jogos[indice]

# Jogo Mega Sena (Computador):

jogo_pc = []

for _ in range(6):
    num = randint(1, 60)
    jogo_pc.append(num)


acertos = 0
for num in jogo_usuario:
    if num in jogo_pc:
        acertos += 1

print(f'Usuário: {jogo_usuario}')
print(f'Computador: {jogo_pc}')
print(f'Você acertou {acertos} números')


