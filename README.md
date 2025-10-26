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

4. Configure o .env:
   ```bash
   cp .env.example .env
   ```

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse:
   - Docs: http://127.0.0.1:8000/docs  
   - Home: http://127.0.0.1:8000/
