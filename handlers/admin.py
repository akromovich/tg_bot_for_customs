from config import ID_ADMIN
from create_bot import bot,dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from keyboards.kb_admin import *
from states.states import UserRegister
from db import DataBase

db = DataBase()

@dp.message_handler(Text(equals='Katalog🗂'))
async def catalog(msg:types.Message):
    await msg.answer('Bosh katalogi',reply_markup=katalog)

@dp.message_handler(commands=['menu'])
async def main_menu(msg: types.Message):
    if msg.from_user.id == ID_ADMIN:
        await msg.answer('Bosh menyu👇', reply_markup=kb_admin)
    else:
        if not await db.check_user(msg.from_user.id):
            await msg.answer('Ismni kiriting F.I.O\nmisol:\nAzizov Aziz Azizovich:')
            await UserRegister.first()
        else:
            await bot.send_message(msg.chat.id, "bo`limlni tanlang👇", reply_markup=kb)




def register_admin_handlers(dp:Dispatcher):
    pass