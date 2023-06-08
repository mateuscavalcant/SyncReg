import string, random, re


def validarEmail(email):
    # Verifica se o email fornecido está no formato correto.
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


def validarSenha(senha):
    # Verifica se a senha fornecida tem entre 8 e 20 caracteres.
    if len(senha) < 8 or len(senha) > 20:
        return False
    return True


def gerarCodigo():
    # Gera um código de 6 caracteres aleatórios, formados por letras maiúsculas e dígitos.
    codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return codigo


def enviarEmail(codigo, email):
    print(f"Um código foi enviado para o email {email}")
    print(f"Código: {codigo}")

