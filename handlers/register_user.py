from aiogram import Dispatcher, types
from create_bot import dp, bot
from states.states import UserRegister
from db import DataBase

db = DataBase()


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    print(f'{msg.from_user.id} {msg.from_user.first_name} {msg.date},')

    global ID
    ID = msg.from_user.id

    if not await db.check_user(msg.from_user.id):
        await msg.answer('Введите имя:')
    else:
        await bot.send_message(msg.chat.id, "вы уже прошли регистрацию")


# async def load_name(msg: types.Message, state=FSMContext):
#     async with state.proxy() as data:
#         data['user_id'] = msg.from_user.id
#         data['name'] = msg.text
#     await Users.next()
#     await msg.answer('Введите фамилию:')

# # @dp.message_handler(state=Users.surname)


# async def load_surname(msg: types.Message, state=FSMContext):
#     async with state.proxy() as data:
#         data['surname'] = msg.text
#     await Users.next()
#     await msg.answer('Введите должность:')

# # @dp.message_handler(state=Users.job)


# async def load_job(msg: types.Message, state=FSMContext):
#     async with state.proxy() as data:
#         data['job'] = msg.text
#     await Users.next()
#     await msg.answer('Введите номер', reply_markup=kb_admin.contact)

# # @dp.message_handler(state=Users.phone)


# async def load_phone(msg: types.Message, state=FSMContext):
#     if msg.contact:
#         async with state.proxy() as data:
#             data['phone'] = msg.contact['phone_number']
#         async with state.proxy() as data:
#             await db.add_user(state)
#             await msg.answer('Ожидание подтверждения...')
#             await bot.send_message(ID_ADMIN, f'<b>{data["name"]}</b> <b>{data["surname"]}</b> хочет присоеденится к боту\nномер: {data["phone"]}', parse_mode='html', reply_markup=kb_admin.exam)
#             await state.finish()
#     else:
#         await msg.answer('Введите номер', reply_markup=kb_admin.contact)


# async def autorize(callback: types.CallbackQuery, state=FSMContext):

#     if callback.data == 'answer_отказать':
#         await db.del_user(ID)
#         await bot.send_message(ID, 'отказано в доступе к боту')
#         await callback.msg.answer('вы отказали пользователя', reply_markup=kb_admin.menu_kb)
#         await callback.answer()
#         await callback.msg.delete()
#     elif callback.data == 'answer_принять':
#         await bot.send_message(ID, 'вас приняли ')
#         await callback.msg.answer('принято', reply_markup=kb_admin.menu_kb)
#         await callback.answer()
#         await callback.msg.delete()
#     else:
#         await callback.ansnwer('ошибка')


def register_user_handlers(dp: Dispatcher):
    pass
#     dp.register_message_handler(load_start, commands=['start'])
#     dp.register_message_handler(load_name, state=Users.name)
#     dp.register_message_handler(load_surname, state=Users.surname)
#     dp.register_message_handler(load_job, state=Users.job)
#     dp.register_message_handler(load_phone, content_types=[
#                                 'any'], state=Users.phone)
#     dp.register_callback_query_handler(autorize, Text(startswith='answer_'))
