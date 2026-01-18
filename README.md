# To-Do List API - Flask 🚀

Este projeto é uma API RESTful para gerenciamento de tarefas, desenvolvida com Python e Flask, utilizando arquitetura profissional (Factory Pattern), segurança baseada em Tokens e relacionamentos entre entidades.

## 🛠️ O que foi implementado recentemente
- [x] **Autenticação JWT (Bearer Token):** Proteção de rotas com validação de token no cabeçalho `Authorization`.
- [x] **Relacionamentos SQL:** Vínculo de integridade entre `Users` e `Tasks` (Um usuário para muitas tarefas).
- [x] **Marshmallow Nesting:** Serialização avançada que permite visualizar os detalhes das tarefas dentro do perfil do usuário em uma única consulta.
- [x] **Segurança de Nível de Registro:** Filtros de consulta que garantem que um usuário só possa visualizar e manipular suas próprias tarefas.

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
app/
├── models/          # Modelos de Dados (SQLAlchemy) e Schemas (Marshmallow)
│   ├── tasks.py     # Definição da tabela Tasks e TasksSchema
│   └── users.py     # Definição da tabela Users e UsersSchema (com ma.Nested)
├── routes/          # Gerenciamento de Blueprints
│   └── routes.py    # Definição centralizada de rotas e métodos
├── views/           # Lógica de negócio (Controllers)
│   ├── helper.py    # Decorator @token_required e lógica de auth
│   ├── users.py     # Funções de manipulação de usuários
│   └── tasks.py     # Funções de CRUD de tarefas (Listar, Criar, Deletar)
├── __init__.py      # Factory da aplicação e Registro de Blueprints
config.py            # Configurações de Banco de Dados e SECRET_KEY
run.py               # Ponto de entrada para iniciar o servidor Flask            # Ponto de entrada do sistema

##  Tecnologias Utilizadas
* **Python 3.x**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Marshmallow**

##  Organização do Projeto
- `app/`: Contém a lógica da aplicação.
- `config.py`: Configurações de banco de dados e chaves de segurança.
- `run.py`: Arquivo para iniciar o servidor.