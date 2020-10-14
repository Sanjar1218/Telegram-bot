from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = os.environ['TOKEN']


def start(update, context):

    button = InlineKeyboardButton(
        text='CodeSchoolUz',
        callback_data=345
    )

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )
    bot = context.bot
    # text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id=chat_id, text='New Text: 0', reply_markup=reply_markup)
lst=[]
def codeschool(update, context):
    lst.append('a')
    count=len(lst)
    button = InlineKeyboardButton(
        text='CodeSchoolUz',
        callback_data=1
    )

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )
    query = update.callback_query
    query.edit_message_text(f'New Text:{count}', reply_markup=reply_markup)
    data = query.data
    query.answer('GOOD!')

    print(data)


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(codeschool))

updater.start_polling()
updater.idle()
