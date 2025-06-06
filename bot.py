from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# BotFather ကရတဲ့ API Token ကို ဒီနေရာမှာထည့်ပါ
TOKEN = "7248432573:AAEfwlsSgJnEswh65n6TxIOYZRQe9rT8kjA
"

# /start command အတွက် function
def start(update, context):
    update.message.reply_text('Hello! Welcome to my bot.')

# ရိုးရိုး message တွေအတွက် function
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Updater instance တစ်ခုပြုလုပ်ပြီး token ကိုထည့်ပါ
    updater = Updater(TOKEN, use_context=True)

    # Dispatcher ကိုရယူပါ
    dp = updater.dispatcher

    # CommandHandler တွေထည့်ပါ
    dp.add_handler(CommandHandler("start", start))

    # MessageHandler တွေထည့်ပါ (စာသား message တွေကို echo လုပ်ဖို့)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Bot ကိုစတင်ပါ
    updater.start_polling()

    # Bot ကို Ctrl+C နှိပ်တဲ့အထိ run နေအောင်လုပ်ပါ
    updater.idle()

if name == '__main__':
    main()
