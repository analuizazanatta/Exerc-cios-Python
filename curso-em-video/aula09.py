# Len(): Comprimento da frase.
# Count(''): Contar quantas vezes o caracter está na frase (Letras maiúsculas e minúsculas são diferentes.)
# find(''): Encontrar 
# IN: 'palavra caracter' in variável (retorna true ou false)
# Replace: Alterar        .replace('antigo', 'novo')
# Upper(): Transforma em Maiúscula
# Lower(): Transforma em Minúscula
# Capitalize: Coloca apenas a primeira letra da frase da string para Maiúsculo
# title: TRanforma todas as primeiras letras das palaras para Maiúsculo
# strip(): Remove os espaços do começo e do fim da string (Dá pra por r(right) e l(left) para removes espaços de um lado apenas)
# split(): Gera uma lista com as palavras da string
# Join: Junta a divisão feita das palavras com a configuração fornecida '-'(exemplo de como vai juntar).join(frase exemplo) = jdjdjd-jdjdjdj-jdjdjd

# _________________________________

# Exercício 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

"""nome = str(input('Informe seu nome completo para analise: '))

print(nome.upper()) 

print(nome.lower())

print(len(nome)) 

print(len(nome.strip())) 

print(nome.replace('Zanatta', ' De Souza')) 

nome = nome.split() 
letras = len(nome[0])                 
print(letras)"""

# ________________________________

# Exercício 23: 

"""num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A unidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'O milhar é {m}')"""

# _________________________________

# Exercício 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

"""cidade = str(input('Informe a cidade que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')"""

# _________________________________

# Exercício 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

"""nome = str(input('Digite seu nome completO: ')).strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')"""

# _________________________________

# Exercício 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

"""frase = str(input('Digite uma frase: '))

print(f'A letra a apareceu {frase.upper().count('A')}')
print(f'A primeira letra a apareceu na posição {frase.find('a')+1}')"""

# _________________________________

# Exercício 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


"""nome = input('Digite seu nome completo: ').split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')"""

# __________________________________
