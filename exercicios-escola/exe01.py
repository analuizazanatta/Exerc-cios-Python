# 1. Criar um programa que solicite os dados: Nome, telefone, e-mail, município, estado e questione se a escola está ativa ou inativa. Essa escola deve ser salva dentro de um dicionário "chave:valor", e depois ser adicionada em uma lista geral que contém todas as escolas.
# 2. Deve ser possível adicionar uma nova escola.
# 3. Deve ser possível listar todas as escolas
# 4. Deve ser possível ativar/Inativar uma escola já adicionada.
# 5. Deve ser possível listar as escolas filtrando por situação ativa ou inativa.


escolas_gerais = []


# Função de cadastrar escolas:

def cadastrar_escola():

    while True:

        # Dados de cadastro:

        cadastros_escolas = {
            "nome": "",
            "telefone": "",
            "email": "",
            "municipio": "",
            "estado": "",
            "status": ""
        }

        # Input solicitando os dados da escola.
        
        cadastros_escolas["nome"] = input("Nome da escola: ")

        cadastros_escolas["telefone"] = input("Telefone: ")

        cadastros_escolas["email"] = input("E-mail: ")

        cadastros_escolas["municipio"] = input("Município onde a escola se localiza: ")

        cadastros_escolas["estado"] = input("Estado de município: ")

        cadastros_escolas["status"] = input("Ativa ou inativa? ").upper()

        parar_cadastro = input("Deseja parar de cadastrar? [Sim/Não]: ").strip().upper()

        escolas_gerais.append(cadastros_escolas)
            
        if parar_cadastro == "SIM":
            break

# Função para listar escolas:

def listar_escolas():
    for indice, escola in enumerate(escolas_gerais):
        print(indice, escola)

# Função para exibir as escolas e escolher qual será alterada a situação:

def trocar_status():

    # Listar escolas

    listar_escolas()

    # Escolher escola

    indice = input("Qual escola você deseja alterar? ")

    indice_inteiro = int(indice)

    escola = escolas_gerais[indice_inteiro]

    # Alterar situação

    if escola["status"] == "ATIVA":

        escola["status"] = "INATIVA"

    elif escola["status"] == "INATIVA":

        escola["status"] = "ATIVA"

    else:
        print("Expressão inválida! ")

    escolas_gerais[indice_inteiro] = escola 

    print("Status alterado! Digite 2 para visualizar.")

# Função para filtrar as escolas pela status:

def filtrar_status():

    opção_status = input("Qual status você quer filtrar? Ativa ou Inativa: ").upper()
    
    for dicionario in escolas_gerais:
        if dicionario["status"] == opção_status:
            print(dicionario)
 
# Programa: 

while True:

    print()
    print('Opções de ações: \n'
          '[1] Cadastrar escolas.\n'
          '[2] listar escolas.\n'
          '[3] Trocas status do cadastro.\n' 
          '[4] Filtrar escolas pelo status.\n'
          '[5] Sair.')

    print()

    acao_escolhida = input('Qual ação você deseja fazer?  ')

    print()

    if acao_escolhida == "1":
        cadastrar_escola()

    elif acao_escolhida == "2":
        listar_escolas()

    elif acao_escolhida == "3":
        trocar_status()

    elif acao_escolhida == "4":
        filtrar_status()

    elif acao_escolhida == "5":
        print("Saindo do programa..")
        break

    else:
        print("Alternativa inválida, tente novamente.")

    print()