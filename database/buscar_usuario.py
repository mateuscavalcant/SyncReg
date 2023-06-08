import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="nome_banco_de_dados"
)


def buscarEmail(email):
    try:
        myCursor = mydb.cursor()

        # Verifica na tabela a existência de um usuário
        sql = "SELECT * FROM usuario WHERE Email = %s"
        val = (email,)

        myCursor.execute(sql, val)

        result = myCursor.fetchone()

        # Fechando o cursor e a conexão
        myCursor.close()
        mydb.close()

        if result:
            # Usuário encontrado
            return True
        else:
            # Usuário não encontrado
            return False

    except mysql.connector.Error as error:
        return None
