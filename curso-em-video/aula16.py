# Aula 16: Tuplas

# ________________________

# Exercício  72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'vinte e um')

num = int(input('Digite um número entre 0 e 20: '))

for c in range(0, 21):
    if num == c:
        print(f'Você digitou o número {tupla[c]}')
'''

# Exercício 73: 3: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação.
# Depois mostre: 
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

"""
times_tupla = ('Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro', 'São Paulo', 'Bahia', 'Atlético-PR', 'Atlético-MG', 'Bragantina', 'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corínthians', 'Grêmio', 'Ec-Vitória', 'Cuiaba', 'Fluminense', 'Atlético-GO' )


print(f'TIMES DO BRASILEIRÃO: {times_tupla}\n')
print('_' * 20)

# a)
print(f'\nOs primeiros 5 times do brasileirão são: {times_tupla[0:5]}')

# b)
print(f'\nOs 4 últimos colocados do brasileirão são: {times_tupla[-4:]}')

# c)
print(f'\nOs times em ordem alfabética: {sorted(times_tupla)}')

# d)
print(f'\nO time Internacional se encontra na {times_tupla.index("Internacional") + 1}ª posição')
"""

# _____________________

# Exercício 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""
from random import randint

lista = tuple([randint(1, 10) for _ in range(5)])


print(f"Os números sorteados foram: {', '.join([str(i) for i in lista])}") 
# Join para juntar os elementos separando pela string ', '.

print(f'O menor número da lista foi {sorted(lista)[0]}')
print(f'O maior número da lista foi {sorted(lista)[-1]}')
"""

# ______________________

# Exercício 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

"""
cont_9 = 0
valores = tuple([int(input('Digite um valor: ')) for _ in range(0, 4)])

# a)
if valores == 9:
    cont_9 += 1
print(f'O número 9 foi digitado {cont_9 + 1}x.')

# b)
print(f'O número 3 apareceu na {valores.index(3) + 1}ª posição. ')

# c)
print(f'Os números pares da lista são: {", ".join([str(i) for i in valores if i % 2 == 0])}')  
"""
# __________________

# Exercício 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
tupla = ('maça', 3.5, 'banana', 4.80, 'pera', 3.00, 'abacate', 2.5, 'uva', 3.5, 'manga', 2.30)

print(f'{'*' * 3}OFERTAS HORTÍFRUTE{'*' * 4}')
for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f'{tupla[posicao]:.<20}', end="")
    else:
        print(f'R${tupla[posicao]:>3}')
"""

# ________________________

# Exercício 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
palavras = ('LAPIS', 'BORRACHA', 'ARVORE', 'CABELO', 'COMPUTADOR', 'ANEL', 'ESTRADA', 'BICICLETA', 'CHOCOLATE', 'NDTV')

print('Contando Vogais...')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end="")
    for vogal in p:
        if vogal.upper() in 'AÁÃÂEÉIÍOÓÕÔUÚ':
            print(f'{vogal}', end="")
"""