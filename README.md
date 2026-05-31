# 🤖 Discord Bot — Remove Background

Bot para remover o fundo de imagens e retornar em PNG com transparência.

---

## 📋 Comandos

| Comando | Descrição |
|---------|-----------|
| `!rembg` | Remove o fundo da imagem anexada |
| `!removebg` | Mesmo que acima |

**Como usar:** Envie uma imagem no Discord com o texto `!rembg` na mensagem.

---

## 🚀 Deploy no Railway (pelo celular)

### 1. Criar o bot no Discord
1. Acesse [discord.com/developers/applications](https://discord.com/developers/applications)
2. Clique em **New Application** → dê um nome
3. Vá em **Bot** → clique em **Add Bot**
4. Em **Privileged Gateway Intents**, ative:
   - ✅ `MESSAGE CONTENT INTENT`
5. Clique em **Reset Token** e copie o token (guarde bem!)
6. Vá em **OAuth2 → URL Generator**:
   - Scopes: `bot`
   - Permissions: `Send Messages`, `Read Messages`, `Attach Files`
7. Copie o link gerado e abra no navegador para adicionar o bot ao seu servidor

### 2. Subir o código no GitHub
1. Acesse [github.com](https://github.com) e crie uma conta (se não tiver)
2. Crie um novo repositório público chamado `discord-rembg-bot`
3. Faça upload dos arquivos: `bot.py`, `requirements.txt`, `railway.toml`

### 3. Deploy no Railway
1. Acesse [railway.app](https://railway.app) e entre com sua conta GitHub
2. Clique em **New Project → Deploy from GitHub Repo**
3. Selecione o repositório `discord-rembg-bot`
4. Vá em **Variables** e adicione:
   ```
   DISCORD_TOKEN = seu_token_aqui
   ```
5. O Railway vai fazer o deploy automaticamente! ✅

---

## ⚙️ Rodando localmente (PC)

```bash
pip install -r requirements.txt
export DISCORD_TOKEN="seu_token_aqui"
python bot.py
```

---

## 📁 Estrutura

```
discord-bot/
├── bot.py           # Código principal
├── requirements.txt # Dependências
├── railway.toml     # Config do Railway
└── README.md        # Este arquivo
```
