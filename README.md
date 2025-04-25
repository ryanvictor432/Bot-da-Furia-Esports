# FURIA123 Bot - Telegram Bot

Este projeto é um bot interativo do Telegram que fornece informações sobre a equipe de Esports FURIA.

## Como acessar o bot

Existem duas formas principais de acessar e interagir com o **furia123_bot** no Telegram:

### 1. **Pesquisar pelo nome do bot**

A maneira mais fácil de encontrar o bot é pesquisando pelo **nome** do bot diretamente no Telegram. Siga esses passos:

1. Abra o **Telegram**.
2. Na barra de pesquisa no topo, digite **"furia123_bot"**.
3. Clique no bot nos resultados da pesquisa e inicie uma conversa.

Assim que a conversa for iniciada, o bot responderá com um menu de opções e você poderá interagir com ele.



Se você for o desenvolvedor ou quiser rodar o bot localmente, siga os passos abaixo.

### 1. **Clone o repositório**:
   Primeiro, clone este repositório para o seu computador.

   ```bash
   git clone https://github.com/ryanvictor432/Bot-da-Furia-Esports
   
Instale as dependências:
O código foi desenvolvido em Python, então você precisa instalar as dependências. Use o pip para instalar o necessário.
pip install python-telegram-bot
Obtenha um Token de Bot do Telegram:
Vá até o BotFather no Telegram.

Crie um novo bot e obtenha o TOKEN que será utilizado no código.

4. Adicione o Token no código:
No arquivo main.py, encontre a linha onde está app = ApplicationBuilder().token("SEU_TOKEN_AQUI").build(), e substitua "SEU_TOKEN_AQUI" pelo token que você obteve no BotFather.
app = ApplicationBuilder().token("seu_token_aqui").build()
Após configurar o token, você pode executar o bot localmente com o comando:
python main.py
