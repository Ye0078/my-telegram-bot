from telegram import Bot  
from telegram.ext import Updater, CommandHandler, MessageHandler  
import logging  

# Enable logging  
logging.basicConfig(  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    level=logging.INFO  
)  

logger = logging.getLogger(__name__)  

# API Token  
TOKEN = '7248432573:AAEfwlsSgJnEswh65n6TxIOYZRQe9rT8kjA'  

def start(update, context):  
    context.bot.send_message(  
        chat_id=update.effective_chat.id,  
        text='Hello! I am your GitHub Bot!'  
    )  

def main():  
    updater = Updater(TOKEN, use_context=True)  

    dp = updater.dispatcher  

    dp.add_handler(CommandHandler('start', start))  

    updater.start_polling()  
    updater.idle()  

if name == '__main__':  
    main()
