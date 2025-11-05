# 🚀 Como Iniciar o Servidor FastAPI

## ❌ Problema: "Conexão recusada"

Esse erro significa que o **servidor FastAPI não está rodando**. Vamos resolver!

---

## ✅ Solução: Iniciar o Servidor

### Passo 1: Abrir Terminal na Pasta do Projeto

1. Abra o PowerShell ou CMD
2. Navegue até a pasta do projeto:
   ```bash
   cd C:\Users\Pichau\Documents\backend_works\first_backend
   ```

### Passo 2: Ativar Ambiente Virtual (se usar)

**Se você criou um ambiente virtual (.venv ou venv):**

**Windows PowerShell:**
```bash
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
```

Você verá `(.venv)` antes do prompt quando estiver ativado.

### Passo 3: Iniciar o Servidor

Execute este comando:

```bash
uvicorn main:app --reload
```

### Passo 4: Verificar se Funcionou

Você deve ver algo assim:

```
INFO:     Will watch for changes in these directories: ['C:\\Users\\Pichau\\Documents\\backend_works\\first_backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [67890]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Se aparecer isso, o servidor está rodando!**

### Passo 5: Testar no Navegador

Agora abra no navegador:
- **Home:** http://127.0.0.1:8000/
- **Documentação:** http://127.0.0.1:8000/docs
- **Listar usuários:** http://127.0.0.1:8000/users/

**Deve funcionar agora!** ✅

---

## ⚠️ Problemas Comuns

### Erro: "uvicorn não é reconhecido"

**Solução:** Instale as dependências primeiro:
```bash
pip install -r requirements.txt
```

### Erro: "Porta 8000 já está em uso"

**Solução:** Use outra porta:
```bash
uvicorn main:app --reload --port 8001
```

Depois acesse: `http://127.0.0.1:8001`

### Erro: "ModuleNotFoundError"

**Solução:** Verifique se está na pasta correta e instale dependências:
```bash
pip install -r requirements.txt
```

### Erro de conexão com banco

**Solução:** Verifique o arquivo `.env` e se o MySQL está rodando.

---

## 📋 Checklist Antes de Iniciar

Antes de iniciar o servidor, verifique:

- [ ] Está na pasta correta do projeto?
- [ ] Ambiente virtual ativado (se usar)?
- [ ] Dependências instaladas (`pip install -r requirements.txt`)?
- [ ] MySQL está rodando (se usar MySQL)?
- [ ] Arquivo `.env` configurado?

---

## 🔄 Comandos Úteis

### Parar o Servidor
- Pressione `Ctrl+C` no terminal

### Reiniciar o Servidor
- Pare com `Ctrl+C`
- Inicie novamente: `uvicorn main:app --reload`

### Ver Logs em Tempo Real
O servidor mostra logs automaticamente quando recebe requisições.

---

## 🎯 Resumo Rápido

1. Abra terminal na pasta do projeto
2. Ative ambiente virtual (se usar): `.venv\Scripts\Activate.ps1`
3. Execute: `uvicorn main:app --reload`
4. Aguarde: "Uvicorn running on http://127.0.0.1:8000"
5. Abra: http://127.0.0.1:8000/docs

**Pronto! Agora deve funcionar! 🎉**




