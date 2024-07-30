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


times_tupla = ('Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro', 'São Paulo', 'Bahia', 'Atlético-PR', 'Atlético-MG', 'Bragantina', 'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corínthians', 'Grêmio', 'Ec-Vitória', 'Cuiaba', 'Fluminense', 'Atlético-GO' )


print(f'TIMES DO BRASILEIRÃO: {times_tupla}\n')
print('-=' * 20)

# a)
print(f'\nOs primeiros 5 times do brasileirão são: {times_tupla[0:5]}')

# b)
print(f'\nOs 4 últimos colocados do brasileirão são: {times_tupla[-4:]}')

# c)
print(f'\nOs times em ordem alfabética: {sorted(times_tupla)}')

# d)
print(f'O time Internacional se encontra na posição {}')