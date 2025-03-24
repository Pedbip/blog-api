# FirstServer

Este é um projeto de servidor FastAPI que inclui funcionalidades de autenticação, criação de blogs e gerenciamento de usuários.

## Requisitos

- Python 3.10+
- SQLite (ou outro banco de dados configurado)
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/Pedbip/blog-api.git
    cd FirstServer
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # No Windows
    source .venv/bin/activate  # No Linux/Mac
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:

    O banco de dados SQLite será criado automaticamente na primeira execução do servidor.

## Executando o Servidor

Para iniciar o servidor FastAPI, execute:

```sh
uvicorn blog.main:app --reload