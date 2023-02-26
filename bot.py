import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem 
from datetime import datetime

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Добро пожаловать, друг")


def planet(update, context):
    user_planet = update.message.text.split()
    dt_now = datetime.now()
    dt_now_str = dt_now.strftime('%Y/%m/%d')
    planet = getattr(ephem, user_planet[1])()
    planet.compute(dt_now_str)
    update.message.reply_text(ephem.constellation(planet))


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

    

    