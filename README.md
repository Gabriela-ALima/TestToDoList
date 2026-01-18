# To-Do List API - Flask 🚀

Este projeto é uma API RESTful para gerenciamento de tarefas, desenvolvida com Python e Flask, utilizando arquitetura profissional (Factory Pattern) e segurança baseada em Tokens.

## 🛠️ O que foi implementado recentemente
- [x] **Autenticação JWT (JSON Web Token):** Proteção de rotas com geração de tokens dinâmicos.
- [x] **Criptografia de Senhas:** Uso de `werkzeug.security` (PBKDF2) para nunca salvar senhas em texto puro.
- [x] **Decorator de Segurança:** Implementação do `@token_required` para validar o acesso às rotas privadas.
- [x] **Geração Dinâmica de Chave:** Configuração de `SECRET_KEY` aleatória no servidor para maior segurança.

## 🔐 Segurança e Autenticação
A API utiliza **Basic Auth** para troca de credenciais por tokens e **Bearer/Query Token** para as rotas protegidas.
- **Expiração:** Os tokens gerados têm validade de 12 horas.
- **Algoritmo:** HS256.



## 📌 Endpoints Principais

### Usuários e Autenticação
| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | Cadastra um novo usuário | Pública |
| `POST` | `/auth` | Realiza login e retorna o Token | Basic Auth |
| `GET` | `/users` | Lista todos os usuários | Pública |
| `GET` | `/users/<id>` | Busca um usuário específico | Pública |

### Tarefas (Em desenvolvimento)
| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |


## 📂 Estrutura de Pastas Atualizada
```text
app/
├── models/          # Modelos Users e Tasks (SQLAlchemy)
├── views/           # Lógica de negócio (Users, Tasks)
│   ├── helper.py    # Funções de JWT e Decorators
│   └── users.py     # Funções de manipulação de usuários
├── __init__.py      # Factory da aplicação
├── routes.py        # Definição dos Blueprints e Rotas
config.py            # Configurações de DB e SECRET_KEY
run.py               # Ponto de entrada do sistema

##  Tecnologias Utilizadas
* **Python 3.x**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Marshmallow**

##  Organização do Projeto
- `app/`: Contém a lógica da aplicação.
- `config.py`: Configurações de banco de dados e chaves de segurança.
- `run.py`: Arquivo para iniciar o servidor.