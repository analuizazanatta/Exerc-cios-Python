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

# ________________________________

# Exercício 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Fez no curso


# __________________

# Exercício 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""from datetime import datetime 

lista = []

for _ in range(7):
    data_nascimento = input('Digite a data do seu nascimento [dd/mm/aaaa]: ')
    data = datetime.strptime(data_nascimento, '%d/%m/%Y')
    lista.append(data)

lista = sorted(lista)


lista_nascimento = []

for data in lista:
    nascimento = data.strftime('%d/%m/%Y')
    lista_nascimento.append(nascimento)

print(f'A menor data é a {lista_nascimento[0]}')
print(f'A maior data é a {lista_nascimento[-1]}')"""

# _____________________________

# Exercício 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


"""lista = []

for _ in range(5):
    peso = float(input('Digite o primeiro peso: '))
    lista.append(peso)

lista = sorted(lista)

print(f'O menor peso foi {lista[0]} e maior peso é {lista[-1]}. ')"""

# ____________________________

# Exercício 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

"""
lista_homens = []
quantidade_pessoas = 4
soma_idades = 0
cont_mulhermenor_20 = 0

for dados in range(quantidade_pessoas):
    print(f'{20 * "-"} {dados + 1}ª pessoa {20 * "-"}')
    nome = str(input(f'Digite o nome da {dados + 1}ª pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Qual é o sexo? [F / M]: ')).upper()

    if sexo == 'M':
        homem = {'nome': nome, 'idade': idade, 'sexo': sexo}
        lista_homens.append(homem)

    if sexo == 'F' and idade < 20:
        cont_mulhermenor_20 += 1

    soma_idades += idade
    
print(f'A média das idades do grupo foi {soma_idades / quantidade_pessoas}. ')

# homem(s) mais velho(s)
if len(lista_homens) == 0:
    print('Não existe nenhum homem. ')
elif len(lista_homens) == 1:
    print('Existe apenas 1 homem. ')
else:
    lista_homens_mais_velhos = []
    for homem in lista_homens:
        if len(lista_homens_mais_velhos) == 0:
            lista_homens_mais_velhos.append(homem)
        else:
            mais_velho = lista_homens_mais_velhos[0]

            if homem['idade'] == mais_velho['idade']:
                lista_homens_mais_velhos.append(homem)
            elif homem['idade'] > mais_velho['idade']:
                lista_homens_mais_velhos = [homem]

    if len(lista_homens_mais_velhos) == 1:
        mais_velho = lista_homens_mais_velhos[0]
        print(f'O homem mais velho é o {mais_velho["nome"]} com a idade {mais_velho["idade"]}. ')
    
    elif len(lista_homens) == len(lista_homens_mais_velhos):
        print(f'Todos os {len(lista_homens)} homens tem a mesma idade. ')

    else: 
        homens_mais_velhos = ''
        for i, mais_velho in enumerate(lista_homens_mais_velhos):
            if i == 0: 
                homens_mais_velhos = mais_velho['nome']
            elif i == len(lista_homens_mais_velhos) - 1:
                homens_mais_velhos += f' e {mais_velho["nome"]}'
            else:
                homens_mais_velhos += f', {mais_velho["nome"]}'

        print(f'Os {len(lista_homens_mais_velhos)} homens mais velhos são {homens_mais_velhos}. ')

#Verificação de quantidade de mulheres abaixo dos 20 anos dentro do print.

# print(f"Existe {cont_mulhermenor_20} mulher menor de 20 anos" 
#      if cont_mulhermenor_20 == 1 
#      else f"Existem {cont_mulhermenor_20} mulheres menores de 20 anos" 
#      if cont_mulhermenor_20 > 0 
#      else 'Não existem mulheres menores de 20 anos.')
 
if cont_mulhermenor_20 > 0:
    if cont_mulhermenor_20 == 1:
        print(f"Existe {cont_mulhermenor_20} mulher menor de 20 anos")
    else:
        print(f"Existem {cont_mulhermenor_20} mulheres menores de 20 anos")
else:
    print('Não existem mulheres menores de 20 anos.')
"""
