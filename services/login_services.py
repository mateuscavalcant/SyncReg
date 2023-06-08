from api.api_connect_services import ReceberLogin

def fazerLogin():
    email = input("Digite o seu e-mail: ") 
    senha = input("Digite a sua senha: ")

    ReceberLogin(email, senha)

