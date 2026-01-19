# To-Do List API - Flask 🚀

Este projeto é uma API RESTful para gerenciamento de tarefas, desenvolvida com Python e Flask, utilizando arquitetura profissional (Factory Pattern), segurança baseada em Tokens e relacionamentos entre entidades.

## 🛠️ O que foi implementado recentemente
## 🛠️ O que foi implementado recentemente
- [x] **Swagger UI (Flask-RestX):** Documentação interativa automática da API.
- [x] **Autenticação JWT (Bearer Token):** Proteção de rotas com `flask-jwt-extended`.
- [x] **Relacionamentos SQL:** Vínculo de integridade entre `User` e `Tasks` (1:N).
- [x] **Marshmallow Nesting:** Serialização que permite visualizar tarefas dentro do perfil do usuário.
- [x] **Testes Automatizados:** Suíte de testes com `Pytest` cobrindo o CRUD e Autenticação.

## 🔐 Segurança e Autenticação
A API utiliza um fluxo de autenticação moderno e seguro:
1. **Login:** Envio de credenciais via **Basic Auth** para a rota `/auth`.
2. **Acesso:** O servidor retorna um **JWT (Bearer Token)**.
3. **Persistência:** O token deve ser enviado no Header de todas as requisições protegidas:  
   `Authorization: Bearer <seu_token_aqui>`

## 📌 Endpoints da API

### Usuários e Autenticação
| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | Cadastra um novo usuário | Pública |
| `POST` | `/auth` | Realiza login e retorna o JWT | Basic Auth |
| `GET` | `/users` | Lista usuários e os detalhes de suas tarefas | Token |

### Gerenciamento de Tarefas
| Método | Endpoint | Descrição | Autenticação |
| :--- | :--- | :--- | :--- |
| `GET` | `/tasks` | Lista todas as tarefas do usuário autenticado | Token |
| `POST` | `/tasks` | Cria uma nova tarefa (vínculo automático ao ID do Token) | Token |
| `PUT` | `/tasks/<id>` | Atualiza título, descrição ou status (Somente dono) | Token |
| `DELETE` | `/tasks/<id>` | Remove permanentemente uma tarefa do usuário | Token |

## 📂 Estrutura de Pastas Atualizada
```text
├── app/
│   ├── models/          # Modelos SQLAlchemy (User, Tasks)
│   ├── routes/          # Namespaces e Definições do Flask-RestX
│   ├── __init__.py      # Factory Pattern e Configuração da App
├── tests/               # Testes automatizados (conftest.py, test_tasks.py)
├── config.py            # Variáveis de ambiente e configuração de DB
├── requirements.txt     # Dependências do projeto (pip)
└── run.py               # Ponto de entrada da aplicação

##  Tecnologias Utilizadas
* **Python 3.x**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Marshmallow**

##  Organização do Projeto
- `app/`: Contém a lógica da aplicação.
- `config.py`: Configurações de banco de dados e chaves de segurança.
- `run.py`: Arquivo para iniciar o servidor.