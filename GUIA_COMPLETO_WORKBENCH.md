# 🚀 Guia Completo: Configurar MySQL Workbench do Zero

Este guia mostra **TODOS os passos** para configurar o MySQL Workbench e conectar no seu projeto.

---

## 📋 Pré-requisitos

- ✅ MySQL Server instalado no seu computador
- ✅ MySQL Workbench instalado
- ✅ Projeto Python configurado

---

## 🔧 PARTE 1: Configurar o .env

### Passo 1.1: Verificar/Criar arquivo .env

O arquivo `.env` já está criado na raiz do projeto com estas configurações:

```env
DATABASE_SCHEMA="first_backend_db"
DATABASE_USER="root"
DATABASE_PASSWORD=""
DATABASE_HOST=localhost
DATABASE_PORT="3306"
SECRET_KEY="changeme"
```

**⚠️ IMPORTANTE:** 
- Se você **NÃO SABE** a senha do MySQL, deixe `DATABASE_PASSWORD=""` (vazio)
- Se você **SABE** a senha, coloque entre aspas: `DATABASE_PASSWORD="sua_senha"`

---

## 🔌 PARTE 2: Configurar MySQL Workbench

### Passo 2.1: Abrir MySQL Workbench

1. Abra o **MySQL Workbench** no seu computador

### Passo 2.2: Criar Nova Conexão

1. Na tela inicial, veja o painel **"MySQL Connections"**
2. Clique no ícone **"+"** (sinal de mais) ao lado de "MySQL Connections"
   - Ou clique com botão direito > "Create Connection"

### Passo 2.3: Preencher Dados da Conexão

Use **exatamente** os mesmos valores do seu arquivo `.env`:

```
Connection Name: Local MySQL
(ou qualquer nome que você preferir)

Hostname: localhost
Port: 3306

Username: root

Password: (DEIXE VAZIO se não souber, ou coloque a senha)
```

**Configurações importantes:**
- ✅ Clique em **"Store in Vault"** ao lado da senha (para salvar)
- ✅ Marque **"Save password"** se aparecer a opção
- ✅ **Default Schema:** Pode deixar em branco ou colocar `first_backend_db`

### Passo 2.4: Testar Conexão

1. Clique no botão **"Test Connection"** (canto inferior direito)
2. **Resultados possíveis:**

   ✅ **"Successfully made the MySQL connection"**
   - Funcionou! Clique em "OK"
   - Pule para **PARTE 3**

   ❌ **"Access denied for user 'root'@'localhost'"**
   - Senha está incorreta ou MySQL tem senha diferente
   - Veja **PARTE 2.5** para resolver

   ❌ **"Cannot connect to MySQL server"**
   - MySQL não está rodando
   - Veja **PARTE 2.6** para resolver

### Passo 2.5: Se Der "Access Denied" (Sem Senha)

**Tentativa 1: Senha Vazia**

1. Edite a conexão no Workbench
2. Deixe o campo **Password completamente VAZIO**
3. Clique em "Store in Vault" (mesmo vazio)
4. Teste novamente

**Se funcionar:**
- ✅ MySQL não tem senha
- ✅ Atualize o `.env`: `DATABASE_PASSWORD=""`
- ✅ Continue para **PARTE 3**

**Se não funcionar:**
- Veja **PARTE 4** para resetar senha

### Passo 2.6: Se Der "Cannot Connect" (MySQL Não Rodando)

1. Pressione `Win+R`
2. Digite: `services.msc`
3. Pressione Enter
4. Procure por serviços com **"MySQL"** no nome (ex: MySQL80, MySQL Server 8.0)
5. Verifique o status:
   - Se estiver **"Running"** → OK, continue
   - Se estiver **"Stopped"** → Clique com botão direito > **"Start"**
6. Aguarde iniciar
7. Teste a conexão novamente no Workbench

---

## 🗄️ PARTE 3: Criar o Banco de Dados

### Passo 3.1: Conectar no Servidor

1. No MySQL Workbench, **clique duas vezes** na conexão "Local MySQL"
2. Digite a senha se pedir (ou deixe vazio se não tiver senha)

### Passo 3.2: Criar o Banco `first_backend_db`

**Opção A: Via Interface (Mais Fácil)**

1. No painel esquerdo, procure **"Schemas"**
2. Clique com botão direito em uma área vazia
3. Selecione **"Create Schema..."**
4. Digite: `first_backend_db`
5. Deixe **Character Set:** `utf8mb4`
6. Deixe **Collation:** `utf8mb4_unicode_ci`
7. Clique em **"Apply"**
8. Clique em **"Apply"** novamente na janela de revisão
9. Você verá o banco aparecer na lista!

**Opção B: Via SQL (Alternativa)**

1. No Workbench, abra um Query Tab: **File > New Query Tab** (ou `Ctrl+T`)
2. Cole e execute:
   ```sql
   CREATE DATABASE first_backend_db 
   CHARACTER SET utf8mb4 
   COLLATE utf8mb4_unicode_ci;
   ```
3. Clique no ícone ⚡ para executar (ou `Ctrl+Enter`)
4. Você verá "Success" na aba de resultados

### Passo 3.3: Selecionar o Banco

1. No painel esquerdo, expanda **"Schemas"**
2. Você verá `first_backend_db` na lista
3. **Clique duas vezes** nele (ou clique com botão direito > "Set as Default Schema")
4. Ou use o dropdown no topo do Workbench e selecione `first_backend_db`

---

## 🚀 PARTE 4: Iniciar o Projeto e Criar Tabelas

### Passo 4.1: Instalar Dependências (Se Ainda Não Fez)

```bash
pip install -r requirements.txt
```

Isso instala:
- `pymysql` (driver MySQL)
- `cryptography` (para conexão segura)
- Outras dependências

### Passo 4.2: Iniciar o Servidor FastAPI

```bash
uvicorn main:app --reload
```

### Passo 4.3: Tabelas Criadas Automaticamente

Quando o servidor iniciar, você verá:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**A tabela `users` será criada automaticamente!** 

Isso acontece porque o código tem:
```python
init_db()  # Cria as tabelas automaticamente
```

### Passo 4.4: Verificar no MySQL Workbench

1. No MySQL Workbench, **atualize** (botão de refresh ou F5)
2. Expanda:
   ```
   Schemas
     └─ first_backend_db
        └─ Tables
           └─ users  ← SUA TABELA FOI CRIADA! ✅
   ```

---

## 🔍 PARTE 5: Visualizar Dados

### Método 1: Visualização Rápida

1. No Workbench, expanda `first_backend_db` > `Tables` > `users`
2. Clique com botão direito em `users`
3. Selecione **"Select Rows - Limit 1000"**
4. Veja os dados na tabela!

### Método 2: Query SQL

1. Abra um Query Tab (`Ctrl+T`)
2. Digite:
   ```sql
   USE first_backend_db;
   SELECT * FROM users;
   ```
3. Execute (⚡ ou `Ctrl+Enter`)
4. Veja os resultados na aba "Results Grid"

---

## 🔧 PARTE 6: Resetar Senha (Se Necessário)

**Só faça isso se:** Você não conseguiu conectar e precisa resetar a senha do MySQL.

### Passo 6.1: Encontrar arquivo my.ini

1. Abra: `C:\ProgramData\MySQL\MySQL Server 8.0\my.ini`
   (Ou a versão que você tiver)
2. Se não encontrar, procure em: `C:\Program Files\MySQL\...`

### Passo 6.2: Editar my.ini

1. Clique com botão direito > **"Abrir com" > "Bloco de Notas"**
2. Se pedir permissão de administrador, **ACEITE**
3. Procure: `[mysqld]`
4. Logo abaixo, adicione:
   ```
   skip-grant-tables
   ```
5. **SALVE** o arquivo (Ctrl+S)

### Passo 6.3: Reiniciar MySQL

1. Vá em `services.msc` (Win+R)
2. Procure o serviço MySQL
3. Clique com botão direito > **"Restart"**

### Passo 6.4: Conectar Sem Senha

1. No Workbench, conecte com senha **VAZIA**
2. Deve funcionar agora!

### Passo 6.5: Definir Nova Senha

1. No Workbench, abra Query Tab
2. Execute:
   ```sql
   USE mysql;
   ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
   FLUSH PRIVILEGES;
   ```

### Passo 6.6: Remover skip-grant-tables

1. Volte ao `my.ini`
2. **REMOVA** a linha `skip-grant-tables`
3. **SALVE**

### Passo 6.7: Reiniciar MySQL Novamente

1. Reinicie o serviço MySQL em `services.msc`

### Passo 6.8: Atualizar .env

```env
DATABASE_PASSWORD="123456"
```

### Passo 6.9: Testar Com Nova Senha

1. No Workbench, edite a conexão
2. Senha: `123456`
3. Teste → Deve funcionar! ✅

---

## ✅ CHECKLIST FINAL

Use este checklist para verificar se está tudo certo:

- [ ] `.env` configurado com as informações corretas
- [ ] Conexão criada no MySQL Workbench
- [ ] Teste de conexão funcionou
- [ ] Banco `first_backend_db` criado
- [ ] Servidor FastAPI iniciado (`uvicorn main:app --reload`)
- [ ] Tabela `users` aparece no Workbench
- [ ] Consegue ver dados no Workbench

---

## 🎯 RESUMO DOS VALORES PARA USAR

### No arquivo `.env`:
```env
DATABASE_SCHEMA="first_backend_db"
DATABASE_USER="root"
DATABASE_PASSWORD=""  # ou sua senha
DATABASE_HOST=localhost
DATABASE_PORT="3306"
```

### No MySQL Workbench:
```
Connection Name: Local MySQL
Hostname: localhost
Port: 3306
Username: root
Password: (vazio ou sua senha)
Default Schema: first_backend_db (opcional)
```

**São os MESMOS valores!** 🎯

---

## 🆘 Problemas Comuns

| Problema | Solução |
|----------|---------|
| "Access denied" | Tente senha vazia primeiro, ou resetar senha |
| "Cannot connect" | Verifique se MySQL está rodando (services.msc) |
| Banco não aparece | Crie manualmente no Workbench |
| Tabela não aparece | Inicie o servidor FastAPI primeiro |

---

**Pronto! Agora você tem TUDO que precisa! 🎉**




