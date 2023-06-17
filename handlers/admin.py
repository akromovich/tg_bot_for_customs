from create_bot import bot,dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from keyboards.kb_admin import *


@dp.message_handler(Text(equals='Katalog🗂'))
async def catalog(msg:types.Message):
    await msg.answer('Bosh katalogi',reply_markup=katalog)




def register_admin_handlers(dp:Dispatcher):
    pass