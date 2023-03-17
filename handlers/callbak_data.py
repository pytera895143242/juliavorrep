import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username
import random
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content =  -1001989093345

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):

    if call.data == 'go_1':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_2')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=7,reply_markup=markup)

    if call.data == 'go_2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_3')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=10,reply_markup=markup)

    if call.data == 'go_3':
        change_status(call.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Давай скорее!', callback_data='go_4')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=22)
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=15)
        await asyncio.sleep(16)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=16)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=17,reply_markup=markup)

    if call.data == 'go_4':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='ПОГНАЛИ💸', url = 'https://t.me/BekirSPRINTbot?start=sprint_arbitraj')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=19,reply_markup=markup)


    try:
        await bot.answer_callback_query(call.id)
    except:
        pass
