from create_bot import bot,dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from keyboards.kb_admin import *

@dp.message_handler(commands=['start'])
async def start(msg:types.Message):
    await msg.answer('xush kelibsiz',reply_markup=kb)
    print(f'{msg.from_user.id} {msg.from_user.first_name} {msg.date},')
@dp.message_handler(Text(equals='Katalog🗂'))
async def catalog(msg:types.Message):
    await msg.answer('Каталог нашего бота',reply_markup=katalog)




def register_admin_handlers(dp:Dispatcher):
    dp.register_message_handler(start,commands=['start'])