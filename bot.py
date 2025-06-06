import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("7572057562:AAEYXsvfSGUlD0iyL27LDNlQjlpeVS4hZ1E")

async def start(update, context):
    await update.message.reply_text("မင်္ဂလာပါ။ Bot သက်တမ်းဝင်နေပါတယ်။")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
