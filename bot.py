from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters
)

# Função para mostrar o menu principal
async def mostrar_menu(update_or_query, context: ContextTypes.DEFAULT_TYPE, show_greeting=True):
    keyboard = [
        [InlineKeyboardButton("Ver jogadores da FURIA", callback_data='ver_furia')],
        [InlineKeyboardButton("História da FURIA", callback_data='historia_furia')],
        [InlineKeyboardButton("Redes sociais da FURIA", callback_data='redes_furia')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if isinstance(update_or_query, Update):  # Mensagem de texto
        if show_greeting:
            await update_or_query.message.reply_text("Oi! O que você deseja saber?", reply_markup=reply_markup)
        else:
            await update_or_query.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)
    else:  # CallbackQuery
        if show_greeting:
            await update_or_query.edit_message_text("Oi! O que você deseja saber?", reply_markup=reply_markup)
        else:
            await update_or_query.edit_message_text("Escolha uma opção:", reply_markup=reply_markup)

# Quando o usuário envia qualquer mensagem
async def responder_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await mostrar_menu(update, context)

# Quando o usuário clica em algum botão
async def botao_clicado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'ver_furia':
        texto = "Jogadores da FURIA:\nYuurih, Kscerato, Molodoy, Fallen e Yekindar."
    elif query.data == 'historia_furia':
        texto = (
            "🌍 *História da FURIA:*\n\n"
            "A FURIA Esports foi fundada em 2017 por Jaime 'raizen' Pádua e André Akkari.\n"
            "Começou no CS:GO com foco em disciplina, agressividade e alto desempenho.\n"
            "Hoje, é uma das maiores organizações brasileiras, com presença em diversos jogos como CS2, Valorant, League of Legends e outros."
        )
    elif query.data == 'redes_furia':
        texto = (
            "🔗 *Redes sociais da FURIA:*\n\n"
            "🌐 Site oficial: https://www.furia.gg\n"
            "📸 Instagram: https://www.instagram.com/furia\n"
            "🐦 Twitter/X: https://twitter.com/furiagg\n"
            "▶️ YouTube: https://www.youtube.com/FURIA\n"
            "🎵 TikTok: https://www.tiktok.com/@furia"
        )
    elif query.data == 'voltar_menu':
        await mostrar_menu(query, context, show_greeting=False)  # Não mostra saudação ao voltar
        return
    else:
        texto = "Opção desconhecida."

    # Adiciona botão de voltar
    voltar_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Voltar ao menu", callback_data='voltar_menu')]
    ])

    await query.edit_message_text(texto, reply_markup=voltar_markup, parse_mode="Markdown")

# Função principal
if __name__ == '__main__':
    app = ApplicationBuilder().token("7960724437:AAEImZcKC3xYjOUg6qxwqOwsBOzsAwpwxf0").build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_usuario))
    app.add_handler(CallbackQueryHandler(botao_clicado))

    print("Bot está rodando...")
    app.run_polling()


