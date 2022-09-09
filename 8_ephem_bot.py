
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='lot.log')


def greet_user(update, context):
    text = 'Наберите команду /planet и название планеты из списка для \
    определения созвездия: Sun, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune'
    update.message.reply_text(text)


def talk_to_me(update, context):
    if update.message.text.split()[0] == "/planet":
        planet = update.message.text.split()[1]
        date = update['message']['date']
        try: 
            if planet == "Mars":
                planet = ephem.Mars(date)
            elif planet == "Sun":
                planet = ephem.Sun(date)
            elif planet == "Mercury":
                planet = ephem.Mercury(date)
            elif planet == "Venus":
                planet = ephem.Venus(date)
            elif planet == "Jupiter":
                planet = ephem.Jupiter(date)
            elif planet == "Saturn":
                planet = ephem.Saturn(date)
            elif planet == "Uranus":
                planet = ephem.Uranus(date)
            elif planet == "Neptune":
                planet = ephem.Neptune(date)
            constellation = ephem.constellation(planet)
            text = f'Созвездие {constellation[1]}'
        except:
            text = 'Нет такой планеты в Солнечной системе'     
        update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
