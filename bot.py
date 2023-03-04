import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem 
from datetime import datetime

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    update.message.reply_text("Добро пожаловать, друг")


def planet(update, context):
    user_planet = " ".join(context.args).capitalize()
    list_of_planets = str(ephem._libastro.builtin_planets())
    if user_planet in list_of_planets:
        dt_now = datetime.now()
        dt_now_str = dt_now.strftime('%Y/%m/%d')
        planet = getattr(ephem, user_planet)()
        planet.compute(dt_now_str)
        update.message.reply_text(ephem.constellation(planet))
    else:
        update.message.reply_text('Вы ввели несуществующую планету')


def talk_to_me(update, context):
    text = update.message.text
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
