# SyncReg

O projeto SyncReg visa simular de forma interativa o funcionamento de uma conexão entre o back-end, API e o banco de dados.
Ele é um sistema de cadastro de usuários que se comunica com uma API para armazenar e realizar login. 
O sistema consiste em um back-end Python e uma API Go, com um banco de dados MySQL para armazenamento dos dados.

## Funcionalidades

- Cadastro de novos usuários com nome, sobrenome, email e senha.
- Validação do formato do email e senha.
- Verificação de duplicação de email durante o cadastro.
- Envio de um código de verificação por email para validar o cadastro.
- Login para usuários registrados, verificando as credenciais fornecidas.
- Comunicação segura entre o Python e a API (Go) por meio de requisições HTTP.

## Configuração

Para executar o sistema, siga as etapas abaixo:

1. Configure o ambiente Python e Go em sua máquina.
2. Crie um banco de dados MySQL e configure as credenciais de acesso nos arquivos das pastas `handlers` e `database`.
3. Para iniciar o backend interativo em Python, acesse `services/cadastro_services.py` e execute o arquivo.
4. Abra o prompt de comando do seu sistema operacional navegue até o diretório onde está localizado o arquivo main.go da sua API Go. Execute a API Go com o comando `go run main.go`.

## Próximos Passos

Abaixo estão algumas melhorias e recursos que podem ser implementadas:

- Reforçar a segurança do sistema criptografando as senhas armazenadas no banco de dados.
- Implementar autenticação e autorização para controlar o acesso às funcionalidades do sistema.
- Adicionar recursos de recuperação de senha via email.
- Melhorar a interface do usuário com um frontend mais amigável e responsivo.
- Implementar testes automatizados para garantir a qualidade do código.
