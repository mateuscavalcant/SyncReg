package handlers

import (
	"BackCRUD/models"
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

func InserirCadastro(w http.ResponseWriter, r *http.Request) {
	var credenciais models.CredenciaisCadastro
	err := json.NewDecoder(r.Body).Decode(&credenciais)
	if err != nil {
		http.Error(w, "Falha ao ler as credenciais de login", http.StatusBadRequest)
		return
	}

	// Conectar ao banco de dados MySQL
	db, err := sql.Open("mysql", "root:sua_senha@tcp(localhost:3306)/seu_banco_de_dados")

	if err != nil {
		http.Error(w, "Falha ao conectar ao banco de dados", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	// Executar a inserção no banco de dados
	_, err = db.Exec(
		"INSERT INTO usuario (Nome, Sobrenome, Email, Senha) VALUES(?, ?, ?, ?)",
		credenciais.Nome, credenciais.Sobrenome, credenciais.Email, credenciais.Senha)

	if err != nil {
		log.Println("Erro ao inserir o usuário no banco de dados:", err)
		http.Error(w, "Falha ao cadastrar o usuário", http.StatusInternalServerError)
		return

	}

	// Cadastro bem-sucedido
	fmt.Fprintf(w, "Cadastro de usuário realizado com sucesso")
}
