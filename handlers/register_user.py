from aiogram import Dispatcher, types
from create_bot import dp, bot
from states.states import UserRegister
from db import DataBase
from aiogram.dispatcher import FSMContext
from keyboards.kb_admin import *

db = DataBase()


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    print(f'{msg.from_user.id} {msg.from_user.first_name} {msg.date},')

    global ID
    ID = msg.from_user.id

    if not await db.check_user(msg.from_user.id) == False:
        await msg.answer('Введите Ф.И.О\nпример:\nАзизов Азиз Азизович:')
        await UserRegister.first()
    else:
        await bot.send_message(msg.chat.id, "вы уже прошли регистрацию")


@dp.message_handler(state=UserRegister.f_i_o)
async def load_name(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['user_id'] = msg.from_user.id
        data['f.i.o'] = msg.text
    await msg.answer('Отправьте номер телефона\nнажмите кнопку снизу чтобы отправить контакт', reply_markup=phone_kb)
    await UserRegister.next()


@dp.message_handler(state=UserRegister.phone_number,content_types=['contact'])
async def load_phone_number(msg: types.Message, state=FSMContext):
    await msg.answer(msg)
    async with state.proxy() as data:
        data['phone_number'] = msg.contact['phone_number']

    await msg.answer('Выберите язык\nнажмите кнопку снизу чтобы выбрать язык',)
    await UserRegister.next()


@dp.message_handler(state=UserRegister.lang)
async def load_lang(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['lang'] = msg.text
        await db.add_user(data)
    await UserRegister.next()

# @dp.message_handler(state=UserRegister.phone)


async def load_phone(msg: types.Message, state=FSMContext):
    if msg.contact:
        async with state.proxy() as data:
            data['phone'] = msg.contact['phone_number']
        async with state.proxy() as data:
            await db.add_user(state)
            await msg.answer('Ожидание подтверждения...')
            await bot.send_message(ID_ADMIN, f'<b>{data["name"]}</b> <b>{data["surname"]}</b> хочет присоеденится к боту\nномер: {data["phone"]}', parse_mode='html', reply_markup=kb_admin.exam)
            await state.finish()
    else:
        await msg.answer('Введите номер', reply_markup=kb_admin.contact)


async def autorize(callback: types.CallbackQuery, state=FSMContext):

    if callback.data == 'answer_отказать':
        await db.del_user(ID)
        await bot.send_message(ID, 'отказано в доступе к боту')
        await callback.msg.answer('вы отказали пользователя', reply_markup=kb_admin.menu_kb)
        await callback.answer()
        await callback.msg.delete()
    elif callback.data == 'answer_принять':
        await bot.send_message(ID, 'вас приняли ')
        await callback.msg.answer('принято', reply_markup=kb_admin.menu_kb)
        await callback.answer()
        await callback.msg.delete()
    else:
        await callback.ansnwer('ошибка')


def register_user_handlers(dp: Dispatcher):
    pass
#     dp.register_message_handler(load_name, state=UserRegister.name)
#     dp.register_message_handler(load_surname, state=UserRegister.surname)
#     dp.register_message_handler(load_job, state=UserRegister.job)
#     dp.register_message_handler(load_phone, content_types=[
#                                 'any'], state=UserRegister.phone)
#     dp.register_callback_query_handler(autorize, Text(startswith='answer_'))
