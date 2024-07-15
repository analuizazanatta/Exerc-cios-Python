# Aula 14: Repetição While

# Exercício 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
while True:
    sexo = str(input('Digite seu sexo [ M / F ]: ')).upper()

    if sexo == "M" or sexo == "F":
        print(f"Seu sexo é {sexo}")

        break

    else:
        print('Opção inválida! Tente novamente')

    # Como aqui não tem mais nada, vai iniciar o próximo loop
"""

# _________________________

# Exercício 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint

pergunta = str(input(f'Pensei em um número entre 0 e 10... Quer adivinhar? ')).upper()
if pergunta == 'SIM':
     
    sorteio = randint(1, 11)

    while True:

        tentativas = 0

        num = int(input(f'Tente adivinhar o número que o computador pensou: {sorteio} '))
        sorteio = randint(1, 11)
        
        if sorteio == num:
            print(f'você acertou na {tentativas + 1}ª tentativa! O computador também pensou no número {sorteio}')

            break

        elif num > sorteio:
            print(f'Menos...Tente novamente!')

        elif num < sorteio:
            print(f'Mais...Tente novamente!')
        
        tentativas += 1


else:
    print('OK') 
