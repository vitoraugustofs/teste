# 🐍 Como Ativar o Ambiente Virtual

## ✅ Seu Ambiente: `venv`

Você tem um ambiente virtual chamado `venv` na pasta do projeto.

---

## 🚀 Como Ativar (Windows PowerShell)

### Passo 1: Abrir Terminal na Pasta do Projeto

Abra o PowerShell na pasta:
```
C:\Users\Pichau\Documents\backend_works\first_backend
```

### Passo 2: Executar Comando de Ativação

Execute este comando:

```powershell
venv\Scripts\Activate.ps1
```

### Passo 3: Verificar se Funcionou

Você verá `(venv)` no início da linha do terminal:

```
(venv) PS C:\Users\Pichau\Documents\backend_works\first_backend>
```

✅ **Se aparecer `(venv)`, está ativado!**

---

## ⚠️ Se Der Erro de Política de Execução

Se aparecer erro como:
```
venv\Scripts\Activate.ps1 : Não é possível carregar o arquivo porque a execução de scripts foi desabilitada neste sistema.
```

**Solução rápida:**

1. Execute no PowerShell (como Administrador):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
2. Digite `Y` quando perguntar
3. Tente ativar novamente: `venv\Scripts\Activate.ps1`

**OU** use o comando alternativo:
```powershell
venv\Scripts\activate.bat
```

---

## 🎯 Depois de Ativar

Depois que o ambiente estiver ativado (com `(venv)` visível), você pode:

1. **Instalar dependências (se necessário):**
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciar o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

---

## 📋 Resumo Rápido

1. Abra PowerShell na pasta do projeto
2. Execute: `venv\Scripts\Activate.ps1`
3. Veja `(venv)` no prompt
4. Execute: `uvicorn main:app --reload`

**Pronto! 🎉**

---

## 🔄 Desativar Ambiente (Quando Terminar)

Para desativar o ambiente virtual:
```bash
deactivate
```

---

## 💡 Alternativa: Usar CMD ao Invés de PowerShell

Se preferir usar o CMD (Prompt de Comando):

```cmd
venv\Scripts\activate.bat
```

Funciona da mesma forma!



