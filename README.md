# To-Do List API - Flask

Este projeto é uma API RESTful para gerenciamento de tarefas, desenvolvida com Python e Flask, focada em boas práticas de arquitetura e organização.

##  Status Atual

- [x] **Estrutura de Pastas Profissional:** Implementada utilizando o *Factory Pattern*.
- [x] **Ambiente Virtual:** Configuração de `.venv` e gerenciamento de dependências.
- [x] **Persistência de Dados:** Configuração de SQLite via `Flask-SQLAlchemy`.
- [x] **Modelagem de Dados:** Implementação dos modelos `Users` e `Tasks` com relacionamento **1:N** (Um usuário para muitas tarefas).
- [x] **Serialização:** Integração com `Flask-Marshmallow` para conversão de dados entre Objetos e JSON.
- [x] **Criação Automática do Banco:** Tabelas inicializadas com sucesso no banco de dados físico.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Micro-framework para desenvolvimento web.
* **Flask-SQLAlchemy:** ORM para manipulação do banco de dados.
* **Flask-Marshmallow:** Para serialização e validação de dados.
* **SQLite:** Banco de dados leve e relacional.

##  Organização do Projeto

* **`app/`**: Contém o núcleo da aplicação (Models, Routes, Schemas).
* **`app/models/`**: Definição das tabelas `Users` e `Tasks` e seus relacionamentos.
* **`instance/`**: Local onde o arquivo `database.db` é armazenado fisicamente.
* **`config.py`**: Configurações de conexão, chaves secretas e variáveis de ambiente.
* **`run.py`**: Ponto de entrada para iniciar o servidor Flask.

---
