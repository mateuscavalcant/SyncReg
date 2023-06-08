import requests
from models.usuario import Usuario


def EnviarCadastro(nome, sobrenome, email, senha):

    data = Usuario(nome, sobrenome, email, senha).to_json()

    url = 'http://localhost:8081/cadastro'  # substitua pela URL correta da sua API Go

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return "Dados enviados com sucesso"
    else:
        return "Falha ao enviar dados"

def ReceberLogin(email, senha):
    # Dados de login
    dados = {
        "email": f"{email}",
        "senha": f"{senha}"
    }

    # URL do endpoint /login
    url = "http://localhost:8081/login"

    # Enviar requisição POST para o endpoint /login
    response = requests.post(url, json=dados)

    # Verificar o código de status da resposta
    if response.status_code == 200:
        # Login bem-sucedido
        print("Login bem-sucedido!")
    else:
        # Login falhou
        print("Falha ao fazer login:", response.text)
