from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# 👉 Укажи свой WebApp URL
WEBAPP_URL = "https://t.me/yourbusinessworld_bot/Clicker"

# 👉 Прямая ссылка на картинку
WELCOME_IMAGE_URL = "https://i.ibb.co/Cp5zK4y/welcome.png"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("▶️ Play", web_app={"url": WEBAPP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=WELCOME_IMAGE_URL,
        caption=(
            "👋 *Добро пожаловать в ClickerBot!*\n\n"
            "Нажми кнопку ниже, чтобы открыть игру и начать зарабатывать монеты!"
        ),
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Рекомендуется использовать .env
    if not BOT_TOKEN:
        raise Exception("❌ BOT_TOKEN не найден в переменных окружения!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен!")
    app.run_polling()
