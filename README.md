# 🧠 Backend API (FastAPI)

API simples de usuários para integração com front-end.

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://bitbucket.org/seuusuario/meu-backend.git
   cd meu-backend
   ```

2. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o .env (opcional):
   ```bash
   cp .env.example .env
   ```
   Por padrão, usa SQLite (`data.db`). Para mudar, edite o `.env`.

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse:
   - **Documentação Interativa:** http://127.0.0.1:8000/docs  
   - **Home/Health Check:** http://127.0.0.1:8000/
   - **Documentação Alternativa:** http://127.0.0.1:8000/redoc

## 📚 Documentação para Frontend

📖 **Leia o guia completo:** [API_GUIDE.md](./API_GUIDE.md)

Este arquivo contém:
- Todos os endpoints disponíveis
- Exemplos de código (JavaScript, React, Axios)
- Como tratar erros
- Configurações importantes

## 🔌 Endpoints Disponíveis

### Usuários
- **POST** `/users/` - Criar novo usuário
- **GET** `/users/` - Listar todos os usuários

### Geral
- **GET** `/` - Health check (verifica se API está online)

## 🛠️ Tecnologias

- FastAPI (framework web)
- SQLAlchemy (ORM)
- Pydantic (validação)
- Passlib + bcrypt (criptografia de senhas)
- SQLite (banco de dados padrão)
