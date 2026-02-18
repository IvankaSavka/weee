import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Словарь с тренировками
workouts = {
    "Грудь": "Отжимания: 3x12\nЖим лёжа: 4x8\nРазводка гантелей: 3x10",
    "Спина": "Подтягивания: 3x8\nТяга штанги: 4x10\nГиперэкстензия: 3x12",
    "Ноги": "Приседания: 4x10\nВыпады: 3x12\nПодъёмы на носки: 3x15",
    "Плечи": "Жим гантелей вверх: 4x10\nРазведения в стороны: 3x12",
    "Руки": "Сгибание рук на бицепс: 3x12\nРазгибание на трицепс: 3x12",
    "Пресс": "Скручивания: 3x15\nПланка: 3x30 сек\nПодъём ног: 3x12"
}

# Кнопки меню
keyboard = [
    ["Грудь", "Спина"],
    ["Ноги", "Плечи"],
    ["Руки", "Пресс"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Выбери группу мышц:",
        reply_markup=reply_markup
    )

# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in workouts:
        await update.message.reply_text(workouts[text])
    else:
        await update.message.reply_text("Выбери группу мышц из меню.")

# Главная функция
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

# Запуск программы
if name == "__main__":
    main()