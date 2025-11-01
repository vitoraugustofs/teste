# 📚 Guia de Integração - API Backend

Este guia é para desenvolvedores de frontend que vão integrar com esta API.

## 🌐 URLs da API

- **Base URL (local):** `http://127.0.0.1:8000`
- **Documentação interativa:** `http://127.0.0.1:8000/docs`
- **Documentação alternativa:** `http://127.0.0.1:8000/redoc`
- **Health Check:** `http://127.0.0.1:8000/`

## 🚀 Endpoints Disponíveis

### 1. **Health Check**
Verifica se a API está online.

**GET** `/`

**Resposta:**
```json
{
  "message": "API online 🚀"
}
```

---

### 2. **Criar Usuário**
Registra um novo usuário no sistema.

**POST** `/users/`

**Body (JSON):**
```json
{
  "username": "joao_silva",
  "email": "joao@email.com",
  "password": "senha123"
}
```

**Resposta de Sucesso (201):**
```json
{
  "id": 1,
  "username": "joao_silva",
  "email": "joao@email.com"
}
```

**Validações:**
- `username`: string obrigatória (máx. 50 caracteres, único)
- `email`: email válido obrigatório (único)
- `password`: string obrigatória (será criptografada automaticamente)

**Erros possíveis:**
- `422`: Dados inválidos (email ou username duplicado, formato inválido)
- `400`: Requisição malformada

---

### 3. **Listar Usuários**
Retorna todos os usuários cadastrados.

**GET** `/users/`

**Resposta de Sucesso (200):**
```json
[
  {
    "id": 1,
    "username": "joao_silva",
    "email": "joao@email.com"
  },
  {
    "id": 2,
    "username": "maria_santos",
    "email": "maria@email.com"
  }
]
```

---

## 💻 Exemplos de Código

### JavaScript/TypeScript (Fetch API)

#### Criar Usuário
```javascript
async function criarUsuario(username, email, password) {
  try {
    const response = await fetch('http://127.0.0.1:8000/users/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        email: email,
        password: password
      })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Erro ao criar usuário');
    }

    const usuario = await response.json();
    console.log('Usuário criado:', usuario);
    return usuario;
  } catch (error) {
    console.error('Erro:', error);
    throw error;
  }
}

// Uso
criarUsuario('joao_silva', 'joao@email.com', 'senha123');
```

#### Listar Usuários
```javascript
async function listarUsuarios() {
  try {
    const response = await fetch('http://127.0.0.1:8000/users/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao listar usuários');
    }

    const usuarios = await response.json();
    console.log('Usuários:', usuarios);
    return usuarios;
  } catch (error) {
    console.error('Erro:', error);
    throw error;
  }
}

// Uso
listarUsuarios();
```

---

### Axios (JavaScript/TypeScript)

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  }
});

// Criar usuário
async function criarUsuario(username, email, password) {
  try {
    const response = await api.post('/users/', {
      username,
      email,
      password
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      // Erro da API (422, 400, etc)
      console.error('Erro da API:', error.response.data);
    } else {
      console.error('Erro de rede:', error.message);
    }
    throw error;
  }
}

// Listar usuários
async function listarUsuarios() {
  try {
    const response = await api.get('/users/');
    return response.data;
  } catch (error) {
    console.error('Erro:', error);
    throw error;
  }
}
```

---

### React com Hooks

```jsx
import { useState, useEffect } from 'react';

const API_URL = 'http://127.0.0.1:8000';

function CadastroUsuario() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState(null);
  const [sucesso, setSucesso] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErro(null);
    setSucesso(false);

    try {
      const response = await fetch(`${API_URL}/users/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Erro ao criar usuário');
      }

      const novoUsuario = await response.json();
      console.log('Usuário criado:', novoUsuario);
      setSucesso(true);
      setFormData({ username: '', email: '', password: '' });
    } catch (error) {
      setErro(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        value={formData.username}
        onChange={(e) => setFormData({...formData, username: e.target.value})}
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={formData.email}
        onChange={(e) => setFormData({...formData, email: e.target.value})}
        required
      />
      <input
        type="password"
        placeholder="Senha"
        value={formData.password}
        onChange={(e) => setFormData({...formData, password: e.target.value})}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Criando...' : 'Cadastrar'}
      </button>
      {erro && <p style={{color: 'red'}}>{erro}</p>}
      {sucesso && <p style={{color: 'green'}}>Usuário criado com sucesso!</p>}
    </form>
  );
}

function ListaUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    async function carregarUsuarios() {
      try {
        const response = await fetch(`${API_URL}/users/`);
        if (!response.ok) {
          throw new Error('Erro ao carregar usuários');
        }
        const data = await response.json();
        setUsuarios(data);
      } catch (error) {
        setErro(error.message);
      } finally {
        setLoading(false);
      }
    }

    carregarUsuarios();
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (erro) return <p>Erro: {erro}</p>;

  return (
    <ul>
      {usuarios.map(usuario => (
        <li key={usuario.id}>
          {usuario.username} - {usuario.email}
        </li>
      ))}
    </ul>
  );
}
```

---

## ⚙️ Configurações Importantes

### CORS
✅ A API já está configurada para aceitar requisições de **qualquer origem** (`allow_origins=["*"]`). Isso permite que seu frontend faça chamadas sem problemas de CORS.

### Content-Type
⚠️ **Sempre envie** `Content-Type: application/json` no header das requisições POST/PUT.

### URLs de Produção
Quando for para produção, substitua:
- `http://127.0.0.1:8000` → `https://sua-api-em-producao.com`

---

## 🧪 Testando a API

### Usando a Documentação Interativa
1. Inicie o servidor: `uvicorn main:app --reload`
2. Acesse: `http://127.0.0.1:8000/docs`
3. Teste os endpoints diretamente pelo navegador!

### Usando cURL
```bash
# Health check
curl http://127.0.0.1:8000/

# Criar usuário
curl -X POST http://127.0.0.1:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"teste","email":"teste@email.com","password":"senha123"}'

# Listar usuários
curl http://127.0.0.1:8000/users/
```

---

## 🐛 Tratamento de Erros

A API retorna erros no seguinte formato:

```json
{
  "detail": "Mensagem de erro aqui"
}
```

Exemplo de erro 422 (validação):
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

---

## 📝 Notas Importantes

1. **Senhas**: As senhas são automaticamente criptografadas antes de serem salvas (bcrypt). Nunca retornamos a senha na resposta.

2. **IDs**: Os IDs são gerados automaticamente pelo banco de dados (auto-increment).

3. **Email e Username**: Devem ser únicos. Se tentar cadastrar um email/username já existente, receberá erro 422.

4. **Validação de Email**: A API valida automaticamente o formato do email usando Pydantic.

---

## 🆘 Precisa de Ajuda?

- 📖 Documentação completa: `http://127.0.0.1:8000/docs`
- 🐛 Problemas? Verifique se o servidor está rodando na porta 8000
- 💡 Dica: Use o Swagger UI (`/docs`) para testar os endpoints antes de integrar no frontend

