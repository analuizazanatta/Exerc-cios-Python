# Aula 17: Listas

# Lista.append() -> Adiciona
# Lista.insert((índice que vem antes), (índice adicionado)) -> Insere (No índice passado)
# Del -> Deleta
# Lista.pop() ou lista.pop(elemento) -> Deleta normalmente o último da lista mas pode ser passado um parâmetro
# Remove('') -> Remove do índice e ajusta em ordem
# lista.sort (sorted) -> Colaca em erdem e o parâmetro lista.sort(reverse=True) -> Colaca em ordem reversa
# Len(lista) -> Conta quantos índices

# _________________________

# Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
# o maior e o menor valor digitado e as suas respectivas posições na lista.

"""
# Inicializa a lista para armazenar os valores

valores = []

# Lê 5 valores numéricos e os adiciona à lista
for i in range(5):
    valor = float(input(f"Digite o valor {i + 1}: "))
    valores.append(valor)

# Determina o maior e o menor valor da lista
maior_valor = max(valores)
menor_valor = min(valores)

# Determina as posições do maior e do menor valor na lista
# posicoes_maior = [i for i, v in enumerate(valores) if v == maior_valor]
# posicoes_menor = [i for i, v in enumerate(valores ) if v == menor_valor]

# Exibe os resultados
print(f"\nO maior valor digitado foi {maior_valor} nas posição {valores[-1] + 1}")
print(f"O menor valor digitado foi {menor_valor} nas posição {valores[0]}")
"""

# ________________________

# Exercício 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

"""
lista = []

while True:
    numero = int(input('Digite um número: '))

    if numero not in lista:
        lista.append(numero)
        print('Número adicionado à lista com sucesso!')
    else:
        print('Número digitado já existe na lista!')

    pergunta = str(input('Deseja continuar adicionando? [SIM / NÃO]: ')).upper()

    if pergunta != 'SIM':
        print('OK! Encerrando a lista...')
        break

# Ordena a lista antes de exibir
lista.sort()
print(f'Sua lista guarda os seguintes números: {lista}')
"""
# _______________________

# Exercício 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""    
lista = []

for n in range(0, 5):
    numero = int(input(f'Digite o {n + 1}° número: '))
    lista.append(numero)

    if numero > 0:
        lista.append(numero)

    elif numero < 0:
        numero == 0
        lista.append(numero)

    elif numero > 0 and numero < -1:
        numero == 1
        lista.append(numero)

print(lista)"""
""""
lista = []

for i in range(5):
    numero = int(input('Digite um número: '))
    
    # Se a lista estiver vazia ou o número for maior que o último número da lista
    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Número adicionado ao final da lista.')
    else:
        # Encontra a posição correta para inserir o número
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Número adicionado na posição {posicao}.')
                break
            posicao += 1

print('Os números digitados em ordem foram:')
print(lista)"""

# ________________________

# Exercício 81: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
"""
print('Digite alguns números para criar uma lista...')

lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)

    pergunta = str(input('Deseja continuar adicionando? [SIM / NÃO]: ')).upper()

    if pergunta != 'SIM':
        print('OK! Encerrando a lista...')
        break
    
print(40 * '-=')

# A)
print(f'Existem {len(lista)} números na lista criada. ')

# B)
lista.sort(reverse = True)
print(f'A lista de forma descrescente fica: {lista}.')

# C)
if 5 in lista:
print(f'O número 5 está na sua lista! Ele aparece {lista.count(5)} vezes. ')

else:
print(f'O número 5 não foi encontrado na sua lista! ')
"""

# ______________________

# Exercício 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
# conteúdo das três listas geradas.