from api.api_connect_services import EnviarCadastro
from models.usuario import Usuario
from authetication.validacao import validarEmail, validarSenha, gerarCodigo, enviarEmail
from database.buscar_usuario import buscarEmail


def fazerCadastro():
    # Realiza o processo de cadastro de um novo usuário.
    cadastros = {}

    while True:
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        if nome and sobrenome.strip() != "":
            break
        else:
            print("Nome inválido. Tente novamente.")

    while True:
        email = input("Digite o e-mail: ")
        if not validarEmail(email):
            print("O endereço de e-mail não está no formato correto. Tente novamente.")
        elif buscarEmail(email):
            print("Já existe um usuário com este e-mail. Tente outro.")
        else:
            break

    while True:
        senha = input("Digite uma senha: ")
        confirm_senha = input("Confirmar senha: ")
        if senha == confirm_senha:
            if not validarSenha(senha):
                print("A senha deve ter entre 8 e 20 caracteres. Tente novamente.")
            else:
                break
        else:
            print("As senhas não conferem. Tente novamente.")

    codigo = gerarCodigo()
    enviarEmail(codigo, email)

    while True:
        codigo_digitado = input("Digite o código recebido: ")
        if codigo_digitado == codigo:
            EnviarCadastro(nome, sobrenome, email, senha)
            cadastro = Usuario(nome, sobrenome, email, senha)
            cadastros[email] = cadastro
            print("Cadastro realizado com sucesso.")
            break
        else:
            print("Código inválido. Tente novamente")
