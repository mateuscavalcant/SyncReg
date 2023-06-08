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

func SolicitarLogin(w http.ResponseWriter, r *http.Request) {
	var credenciais models.CredenciaisLogin
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

	// Consultar o banco de dados para verificar as credenciais de login
	var email, senha string
	err = db.QueryRow("SELECT Email, Senha FROM usuario WHERE Email = ?", credenciais.Email).Scan(&email, &senha)
	if err != nil {
		log.Println("Erro na consulta do banco de dados:", err)
		if err == sql.ErrNoRows {
			http.Error(w, "Email não encontrado", http.StatusUnauthorized)
		} else {
			http.Error(w, "Falha ao consultar o banco de dados", http.StatusInternalServerError)
		}
		return
	}

	if senha != credenciais.Senha {
		http.Error(w, "Senha incorreta", http.StatusUnauthorized)
		return
	}

	// Login bem-sucedido
	fmt.Fprintf(w, "Login bem-sucedido para o email: %s", email)
}
