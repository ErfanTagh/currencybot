# -*- coding: utf-8 -*-
import bs4 as bs
from urllib.request import Request, urlopen
from telegram.ext import Updater
import time
import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import os

req = Request('http://www.fibazar.ir/v/currency_prices', headers={'User-Agent': 'Chrome/68.0.3440.106 '})
suace = urlopen(req).read()

TOKEN = "565041875:AAFPQZtYC90sh-5KZtjIA9-FfrDBxhUmxgg"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN)
updater.bot.set_webhook("https://currencylooker.herokuapp.com/" + TOKEN)
updater.idle()


# http://www.o-xe.com/
# 94930647

# https://pythonprogramming.net/parsememcparseface/

soup = bs.BeautifulSoup(suace, 'lxml')

dispatcher = updater.dispatcher
table = soup.table
table_rows = table.find_all('tr')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def makeCurrency(t_row):
    str = ""
    for tr in t_row:
        td = tr.find_all('td')

        row = [i.text for i in td]
        if len(row) > 0:
            print('نرخ امروز' + row[0] + ' ' + row[1])
            print('نرخ روز گذشته' + row[0] + ' ' + row[2])

            str += 'نرخ امروز' + row[0] + ' ' + row[1] + '\n' + 'نرخ روز گذشته' + ' ' + row[2] + '\n'
    return str


string1 = makeCurrency(table_rows)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=string1)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()





