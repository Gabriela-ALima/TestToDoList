# To-Do List API

API REST para gerenciamento de tarefas (To-Do List) com autenticação via JWT, construída com Flask e documentada com Swagger.

## Tecnologias Utilizadas

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Marshmallow
* Flask-RESTX (Swagger)
* Flask-JWT-Extended

## Organização do Projeto

```
projeto/
├── run.py              # Arquivo para iniciar o servidor
├── config.py            # Configurações de banco de dados e chaves de segurança
├── requirements.txt      # Dependências do projeto
└── app/
    ├── __init__.py       # App factory (cria e configura a aplicação Flask)
    ├── models/           # Modelos do banco de dados (SQLAlchemy) e schemas (Marshmallow)
    ├── routes/           # Definição das rotas e namespaces do Swagger
    └── views/            # Lógica de negócio de cada rota (controllers)
```

## Como Rodar o Projeto

### Pré-requisitos

* Python 3.x instalado

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd <nome-da-pasta>
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o servidor

```bash
python run.py
```

Se tudo estiver certo, o terminal vai mostrar algo como:

```
* Running on http://127.0.0.1:5000
```

> Na primeira execução, o banco de dados SQLite (`database.db`) é criado automaticamente. Não é necessário instalar Postgres para rodar localmente — o projeto só usa Postgres se a variável de ambiente `DATABASE_URL` estiver configurada.

### 5. Acesse o Swagger

Abra no navegador:

```
http://127.0.0.1:5000/swagger
```

Lá você vai encontrar os três grupos de rotas: `login`, `users` e `tasks`.

## Como Testar a API

1. **Criar um usuário** — `POST /usuarios/` com `username`, `password`, `name` e `email`.
2. **Fazer login** — `POST /usuarios/logar/` com `username` e `password`. A resposta traz um `access_token`.
3. **Autorizar no Swagger** — clique no botão **Authorize** (canto superior direito) e cole:
   ```
   Bearer SEU_TOKEN_AQUI
   ```
4. **Usar as rotas protegidas** — agora é possível listar, criar, atualizar e excluir usuários e tarefas normalmente.