# Aula 19: Dicionários 

# Exercício ChatGPT:

# Crie um dicionário que armazene os nomes de pessoas como chaves e seus números de telefone como valores.
# Depois, peça ao usuário para adicionar mais um contato e exiba o dicionário atualizado.

"""
contatos = {
    "ana": "8866-3775"
}


for c in range(5):
    nome = input('Qual é o nome do contato? ')
    telefone = input('Qual é o número de telefone? ')

    # Errado
    # contatos["nome"] = nome
    # contatos["telefone"] = telefone

    # Certo
    contatos[nome] = telefone


print(contatos)"""

# Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
"""
boletim = {
    "nome": "",
    "media": "",
    "situacao": ""
    }

nome = input('Qual é o nome do aluno? ')
media = float(input('E qual é sua média? '))

if media > 6:
    dados["situacao"] = "Aprovado"

else:
    dados["situacao"] = "Reprovado"

dados["nome"] = nome
dados["media"] = media

print(dados)"""

# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
# número no dado.
"""
from random import randint
from operator import itemgetter

numero_dados = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)
}

ranking = {}
# Vira uma lista e os dados tuplas como no print. Caso necessário formatar o print, terá que ser tratado desta maneira.

#for k, v in numero_dados.items(): 
#    print(f'O {k} tirou o número {v} no dado.')

ranking = sorted(numero_dados.items(), key=itemgetter(1), reverse=True)
#print(ranking)

for k, v in ranking:
    print(f'O {k} teve o maior valor no dado: {v}')
"""

# Exercício 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.