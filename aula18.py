# Aula 18: Parte 2 do assunto de listas

# Exercío 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

nome_peso = []
cont_pessoas = 0
pesada_nome = []
leve_nome = []

while True:
    nome = input('Informe o nome: ')
    peso = float(input('Informe seu peso: '))
    nome_peso.append(nome)
    nome_peso.append(peso)

    pessoa_lista = [nome, peso]
    nome_peso.append(pessoa_lista)

    if peso > 60:
        pesada_nome.append(nome)
    else:
        leve_nome.append(nome)

    cont_pessoas += 1

    pergunta = input('Deseja continuar cadastando? ').upper()

    if pergunta != 'SIM':
        break


print(f'{cont_pessoas} pessoas foram adicionadas na lista. ')
print(f'As pessoas mais pesadas são {", ".join(pesada_nome)} ')
print(f'As pessoas mais leves são {", ".join(leve_nome)}')
    