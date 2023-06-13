from aiogram import types
from create_bot import dp
from states.states import UserRegister

@dp.message_handler(commands=['start'])
async def start(msg:types.Message):
    await msg.answer('xush kelibsiz',reply_markup)
