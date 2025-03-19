# Criar um programa que solicite os dados: nome, telefone, e-mail, município, estado e questione se a escola está ativa ou inativa.
# Essa escola deve ser salva dentro de um dicionário "chave:valor", e depois ser adicionada em uma lista geral que contém todas as escolas.
# Deve ser possível: 
# 1. Adicionar uma nova escola.
# 2. Deve ser possível listar todas as escolas
# 3. Ativar/Inativar uma escola já adicionada.
# 4. Deve ser possível listar as escolas filtrando por situação ativa ou inativa.


# ______________________________________




# 1. Adicionar uma nova escola.
# 2. Deve ser possível listar todas as escolas
# 3. Ativar/Inativar uma escola já adicionada.
# 4. Deve ser possível listar as escolas filtrando por situação ativa ou inativa.

escolas_gerais = []


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

        cadastros_escolas["status"] = input("Ativa ou inativa? ")

        parar_cadastro = input("Deseja parar de cadastrar? [Sim/Não]: ").strip().upper()

        escolas_gerais.append(cadastros_escolas)
            
        if parar_cadastro == "SIM":
            break



def listar_escolas():
    for indice, escola in enumerate(escolas_gerais):
        print(indice, escola)




def trocar_status():
    listar_escolas()
