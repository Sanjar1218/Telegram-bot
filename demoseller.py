from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton
# import os
# TOKEN = os.environ['TOKEN']
def start(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Hello! 👋\nThis is a demo version of the Telegram Store bot. You can test out\n catalog function and checkout process. If you have questions, you\n can contact developer via Fiverr (https://www.fiverr.com/wrenaker), or directly here: @wren_aker'
    button=ReplyKeyboardMarkup([
        ['🏬 Catalog','📦 Orders'],
        ["👤 Userinfo","🛒 Cart"],
        ['🎛 Administration']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Administration(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    button=ReplyKeyboardMarkup([
        ['👥 Users','🏷  Orders'],
        ['👋 Welcome text','🤑 Bonus rate'],
        ['➕ Add category','🗑 Remove category'],
        ['📦 New product','🗑 Delete product'],
        ['🚪 Exit']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Welcome(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Write what you want it doesn\'t matter'
    button=ReplyKeyboardMarkup([
        ['❌ Cancel']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Bonus(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Write what you want it doesn\'t matter'
    button=ReplyKeyboardMarkup([
        ['❌ Cancel']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Dproduct(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Rcategory(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Acategory(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Nproduct(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def catalog(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text=update.message.text
    button=InlineKeyboardButton('🍕Pizza', switch_inline_query_current_chat='pizza')
    button2=InlineKeyboardButton('🍾Soda', switch_inline_query_current_chat='soda')
    reply_markup=InlineKeyboardMarkup([
        [button,button2]
    ])
    bot.sendMessage(chat_id, text, reply_markup=reply_markup)
def inlinequery(update, context):
    button=InlineKeyboardButton('➕ Add to cart', callback_data='add')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    txt='\n$22\.99\n\nOriginal Signature crust, 100% whole milk mozzarella, Canadian\-style bacon, applewood smoked bacon, sliced red onions, Dole® pineapple chunks, Kogi™ Serrano Chili sauce drizzle, and topped with fresh chopped cilantro\.'
    txt2='soda'
    url='https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg'
    m=InputTextMessageContent(
        message_text=f'[Chili Pizza\(14"\)]({url}) {txt}',
        parse_mode='MarkdownV2'
    )
    m1=InputTextMessageContent(
        message_text=f'[soda]({url}) {txt2}',
        parse_mode='MarkdownV2'
    )
    result2=InlineQueryResultArticle(
        title='Chili Pizza (14)',
        input_message_content=m,
        thumb_url=url,
        description='$22.99',
        reply_markup=reply_markup,
        hide_url=True,
        id=1
    )
    result1=InlineQueryResultArticle(
        title='soda',
        input_message_content=m1,
        thumb_url=url,
        description='$0.0',
        reply_markup=reply_markup,
        hide_url=True,
        id=2
    )
    result1=[result2,result2]
    update.inline_query.answer(result1)
lst=[]
def add(update, context):
    query=update.callback_query
    data = query.data
    lst.append(data)
    query.answer('✅Added to cart')
    print(lst)
def cart(update, context):
    l=len(lst)
    bot=context.bot
    chat_id=update.message.chat.id
    button=InlineKeyboardButton(text='❌ Clear', callback_data='clear')
    button1=InlineKeyboardButton(text='✅ Place order', callback_data='place')
    reply_markup=InlineKeyboardMarkup([
        [button, button1]
    ])
    bot.sendMessage(chat_id,f'🛒 Cart\n\nChili Pizza (14") - $22.99x{l}=${22.99*l}\n\n💵 Total:${22.99*l}', reply_markup=reply_markup)
def clear(update, context):
    del lst[:]
    query=update.callback_query
    query.answer('Working')
    query.edit_message_text('✅ Cart cleared')
def place(update, context):
    bot=update.callback_query.bot
    chat_id=update.callback_query.message.chat.id
    button=KeyboardButton('Location', request_location=True)
    reply_markup=ReplyKeyboardMarkup([
        [button],
        ['❌ Cancel.']
    ], resize_keyboard=True)
    bot.sendMessage(chat_id,' 📍 Please send the address to which you want your order to be delivered.', reply_markup=reply_markup)
def location(update, context):
    bot=context.bot
    l=len(lst)
    chat_id=update.message.chat.id
    button=InlineKeyboardButton(text='❌ Clear', callback_data='clear')
    button1=InlineKeyboardButton(text='✅ Place order', callback_data='place')
    reply_markup=InlineKeyboardMarkup([
        [button, button1]
    ])
    bot.sendMessage(chat_id, '👍 Done! Now you can place orders.')
    bot.sendMessage(chat_id,f'🛒 Cart\n\nChili Pizza (14") - $22.99x{l}=${22.99*l}\n\n💵 Total:${22.99*l}', reply_markup=reply_markup)
def order(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    button=InlineKeyboardButton('❌ Cancel.', callback_data='cancel')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    bot.sendMessage(chat_id, '✍️ Order #1602922406 (SETTING)\n🛒 Order list:\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: None\n📍 Delivery address: bulungur', reply_markup=reply_markup)
def cancel(update, context):
    query=update.callback_query
    query.edit_message_text('❌ Order cancelled')
def userinfo(update, context):
    bot=context.bot
    first=update.message.chat.first_name
    chat_id=update.message.chat.id
    button=InlineKeyboardButton('🗺Addresses', callback_data='addresses')
    button2=InlineKeyboardButton('➕ Add address', callback_data='address')
    reply_markup=InlineKeyboardMarkup([
        [button, button2]
    ])
    bot.sendMessage(chat_id, f'👤 {first}\n🤝 Invited friends: 0\n💸 Bonus balance: $0.0\nℹ️ You can get 5.0% on your bonus balance from the amount of each order of your invited friends.\n🔗 Your referral link: https://t.me/demosellerbot?start=555351863', reply_markup=reply_markup)

updater=Updater(token='1175464841:AAEZ4Omez8DqnmmUCt_h2eTdUnAv3nBMDPs')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel'), Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel.'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Location'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🚪 Exit'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🤑 Bonus rate'), Bonus))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Delete product'), Dproduct))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Remove category'), Rcategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('➕ Add category'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 New product'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👋 Welcome text'), Welcome))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'), catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'), cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Orders'), order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👤 Userinfo'), userinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.location, location))
updater.dispatcher.add_handler(CallbackQueryHandler(add, pattern='add'))
updater.dispatcher.add_handler(CallbackQueryHandler(place, pattern='place'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear, pattern='clear'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancel, pattern='cancel'))
updater.dispatcher.add_handler(InlineQueryHandler(callback=inlinequery))
updater.start_polling()
updater.idle()