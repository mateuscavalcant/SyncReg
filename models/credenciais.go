package models

type CredenciaisCadastro struct {
	Nome      string `json:"nome"`
	Sobrenome string `json:"sobrenome"`
	Email     string `json:"email"`
	Senha     string `json:"senha"`
}

type CredenciaisLogin struct {
	Email string `json:"email"`
	Senha string `json:"senha"`
}
