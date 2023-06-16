from handlers.admin import  catalog
from handlers.register_user import start
from create_bot import dp
from aiogram import Dispatcher, types

from keyboards.kb_admin import *


@dp.message_handler()
async def asd(msg: types.Message):
    if msg.text == 'назад◀️':
        await start(msg)
    elif msg.text == 'назад':
        await catalog(msg)
    elif msg.text == 'Детский мир':
        await msg.answer(f'категория: {msg.text}', reply_markup=detskiy_m)
    elif msg.text == 'Транспорт':
        await msg.answer(f'категория: {msg.text}', reply_markup=transport_m)
    elif msg.text == 'Для дома':
        await msg.answer(f'категория: {msg.text}', reply_markup=dom_m)
    elif msg.text == 'Электроника':
        await msg.answer(f'категория: {msg.text}', reply_markup=electronic_m)
    elif msg.text == 'Сырьё/Материалы':
        await msg.answer(f'категория: {msg.text}', reply_markup=materials_m)
    elif msg.text == 'Одежда':
        await msg.answer(f'категория: {msg.text}', reply_markup=clothes_m)
    elif msg.text == 'детская одежда':
        await msg.answer(msg.text)
    elif msg.text == 'детская обувь':
        await msg.answer(msg.text)
    elif msg.text == 'прочие':
        await msg.answer(msg.text)
    elif msg.text == 'мебель':
        await msg.answer(msg.text)
    elif msg.text == 'посуда':
        await msg.answer(msg.text)
    elif msg.text == 'концтовары':
        await msg.answer(msg.text)
    elif msg.text == 'мотосуктера':
        await msg.answer(msg.text)
    elif msg.text == 'телефоны':
        await msg.answer(msg.text)
    elif msg.text == 'телевизоры':
        await msg.answer(msg.text)
    elif msg.text == 'фены':
        await msg.answer(msg.text)
    elif msg.text == 'пылесосы':
        await msg.answer(msg.text)
    elif msg.text == 'компьютеры':
        await msg.answer(msg.text)
    elif msg.text == 'аудиотехника':
        await msg.answer(msg.text)
    elif msg.text == 'техника для дома':
        await msg.answer(msg.text)
    elif msg.text == 'техника для кухни':
        await msg.answer(msg.text)
    elif msg.text == 'аксессуары':
        await msg.answer(msg.text)
    elif msg.text == 'гвозди':
        await msg.answer(msg.text)
    elif msg.text == 'мужская':
        await msg.answer(msg.text)
    elif msg.text == 'женская':
        await msg.answer(msg.text)
    elif msg.text == 'обувь':
        await msg.answer(msg.text)
    elif msg.text == 'наручные часы':
        await msg.answer(msg.text)
    else:
        pass


def register_client_handlers(dp:Dispatcher):
    pass