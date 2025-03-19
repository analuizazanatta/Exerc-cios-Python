# Exercício 05:

"""num = int(input('Digite um número: '))

antecessor = num - 1

sucessor = num + 1

print(f'O número que você escolheu é {num}, seu antecessor é {antecessor} e seu sucessor é {sucessor}. ')"""

# ______________________________

# Exercício 06:

"""num = int(input('Digite um número: '))

dobro = num * 2

triplo = num * 3

raiz_4 = num ** 2

print(f'O número que você escolheu é {num}, o dobro dele é {dobro}, o triplo {triplo} e a raiz quadrada dele {raiz_4}. ')"""

# _______________________________

# Exercício 07: 

"""nota_1 = float(input('Digite a primeira nota: '))

nota_2 = float(input('Digite o segundo número: '))

media = (nota_1 + nota_2) / 2

print(f'A média do aluno é {media} ')"""

# _______________________________

# Exercício 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

"""metros = float(input('Digite uma medida: '))

cm = metros * 100
mm = metros * 1000

print(f'O valor em metros é {metros}, em centímetros ele fica {cm} e em milímetros fica {mm} ')"""

# ________________________________

# Exercício 09: 

"""num = int(input('Digite um número: '))

for n in range(1, 11):
    print(f'{num} x {n} = {num * n}')"""

# _________________________________

# Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

"""dinheiro = float(input('Quanto de dinheiro você gostaria de trocar? '))

troca = dinheiro / 5.25

print(f'Você consegue trocar por US$ {troca} a quantia {dinheiro} que você informou.') """

# __________________________________

# Exercício 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

"""larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

area = larg * alt

print(f'Sua parede é {larg} x {alt} e a área dela é de {area}m².')

tinta = area / 2

print(f'Para pintar a parede você precisará de {tinta}L de tinta. ')"""

# ___________________________________

# Exercício 12:

"""valor_produto = float(input('Qual o valor do seu produto? '))

desconto = (valor_produto * 5 ) / 100          # Poderia colocar tudo na mesma linha 

valor_com_desconto = valor_produto - desconto

print(f'Você ganhou 5% de desconto! O valor ficará R$ {valor_com_desconto}.')"""

# ____________________________________

# Exercício 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""salario = float(input('Qual é o salário do funcionário? '))

novo_salario = salario + (salario * 15 / 100) 

print(f'O Funcionário que ganhava R$ {salario}, ganhou um aumento de 15% recebendo agora R$ {novo_salario} por mês. ')"""

# _____________________________________

# Exercício 14:

"""c = float(input('Informe a temperatura em C: '))

f = ((c * 9) / 5) + 32

print(f'A temperatura {c}C em Celsius agora em Fahrenheit fica {f})')"""

# _____________________________________

# Exercício 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""km = float(input('Quantos km seu carro percorreu? '))

dias = int(input('Quantos dias alugaram? '))

diaria = (dias * 60) + (km * 0.15)

print(f'Você alugou {dias} dias e percorreu durante a viagem {km}km, o valor total do aluguel ficou em R$ {diaria}. Qual a forma de pagamento? ')"""


