import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot token ကို environment variable ထဲကနေယူ
TOKEN = os.environ.get("7248432573:AAEfwlsSgJnEswh65n6TxIOYZRQe9rT8kjA
")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ဟယ်လို! ငါကသင့်ရဲ့ Telegram bot ပါ။")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ဘာကူညီပေးရမလဲ?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()
