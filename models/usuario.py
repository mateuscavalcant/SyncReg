class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def to_json(self):
        return {
            "nome": self.get_nome(),
            "sobrenome": self.get_sobrenome(),
            "email": self.get_email(),
            "senha": self.get_senha()
        }
