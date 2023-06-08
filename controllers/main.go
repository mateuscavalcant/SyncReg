package main

import (
	"SyncReg/handlers"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/cadastro", handlers.InserirCadastro).Methods("POST")
	router.HandleFunc("/login", handlers.SolicitarLogin).Methods("POST")

	log.Fatal(http.ListenAndServe(":8081", router))
}
