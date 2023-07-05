from config import ID_ADMIN
from create_bot import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from keyboards.kb_admin import *
from states.states import *
from db import DataBase
from aiogram.types import ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton

db = DataBase()
lang_list = ['UZ','RU','ENG']

@dp.message_handler(Text(equals="Katalog🗂"))
async def catalog(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('tovarlar haqida malumot👇',reply_markup=kb_admin)
    else:
        await msg.answer('tovarlar haqida malumot👇',reply_markup=kb)
    all_catalog = InlineKeyboardMarkup()
    for i in await db.show_all_catalog():
        all_catalog.add(InlineKeyboardButton(text=i[4],callback_data=i[4]))
    await msg.answer('kategoryani tanlang',reply_markup=all_catalog)
    await AllProduct().first()
        # await bot.send_photo(msg.chat.id,photo=i[5],caption=f'<b>NOMI</b>: {i[1]}\n\n{i[2]}\n\n<b>narxi</b>: {i[3]}s`om',parse_mode='html')

@dp.callback_query_handler(state=AllProduct.category)
async def show_all_product_func(clb:types.CallbackQuery,state:FSMContext):
    for i in await db.category(clb.data):
        await bot.send_photo(clb.message.chat.id,photo=i[5],caption=f'<b>NOMI</b>: {i[1]}\n\n{i[2]}\n\n<b>narxi</b>: {i[3]}s`om',parse_mode='html')
        await clb.answer()
        await state.finish()
@dp.message_handler(commands=["menu"])
async def main_menu(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer("Bosh menyu👇", reply_markup=kb_admin)
    else:
        if not await db.check_user(msg.from_user.id):
            await msg.answer("Ismni kiriting F.I.O\nmisol:\nAzizov Aziz Azizovich:")
            await UserRegister.first()
        else:
            await bot.send_message(msg.chat.id, "bo`limlni tanlang👇", reply_markup=kb)

@dp.message_handler(Text(equals='назад◀️'))
async def cancel_main_menu(msg:types.Message):
    await main_menu(msg)

@dp.message_handler(Text(equals='назад'))
async def cancel_main_menu(msg:types.Message):
    await catalog(msg)

@dp.message_handler(Text(equals="Bekor qilish"), state="*")
async def otmena(msg: types.Message, state: FSMContext):
    await state.finish()
    await main_menu(msg)


@dp.message_handler(Text(equals="Foydalanuvchilar Ro`yhati"))
async def list_users(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer(await db.list_users_db(), parse_mode="html")
    else:
        await msg.answer("вы не админ")


@dp.message_handler(Text(equals="Sozlamalar⚙️"))
async def settings(msg: types.Message):
    await msg.answer(
        await db.db_settings(msg.from_user.id),
        parse_mode="html",
        reply_markup=for_contact,
    )


@dp.callback_query_handler(Text(equals="shaxsiy isimni o`zgartirish"))
async def edit_user_full_name_start(clb: types.Message):
    await clb.message.answer(
        "To`liq ismingizni kiriting (Rasulov Rasul Rasulovich)", reply_markup=back_org
    )
    await EditUserDataFullName.first()


@dp.callback_query_handler(Text(equals="shaxsiy telefon o`zgartirish"))
async def edit_user_phone_number_start(clb: types.Message):
    await clb.message.answer(
        "Telefon raqamingizni yuboring (9989xxxxxxxx):", reply_markup=phone_kb_for_edit
    )
    await EditUserDataPhoneNumber.first()

@dp.message_handler(state=EditUserDataPhoneNumber.phone_number, content_types=["any"])
async def edit_user_phone_number(msg: types.Message, state: FSMContext):
    if msg.contact:
        await db.edit_phone_number(msg.from_user.id, msg.contact["phone_number"])
        if msg.from_user.id in ID_ADMIN:
            await msg.answer("akkaunt yangilandi", reply_markup=kb_admin)
        else:
            await msg.answer("akkaunt yangilandi", reply_markup=kb)
        await settings(msg)
        await state.finish()
    elif not msg.contact:
        await msg.answer("Telefon raqamingizni yuboring (9989xxxxxxxx):")
    else:
        await msg.answer("xatolik")

@dp.callback_query_handler(Text(equals="shaxsiy tilni o`zgartirish"))
async def edit_user_lang_start(clb: types.Message):
    await clb.message.answer("Tilni tanlang:", reply_markup=lang_kb)
    await EditUserDataLang.first()

@dp.message_handler(state=EditUserDataLang.lang)
async def edit_user_lang(msg: types.Message, state: FSMContext):
    if msg.text in lang_list:
        await db.edit_lang(msg.from_user.id, msg.text)
        if msg.from_user.id in ID_ADMIN:
            await msg.answer("akkaunt yangilandi", reply_markup=kb_admin)
        else:
            await msg.answer("akkaunt yangilandi", reply_markup=kb)
        await settings(msg)

        await state.finish()
    else:
        await msg.answer("Tilni tanlang:", reply_markup=lang_kb)



@dp.message_handler(state=EditUserDataFullName.full_name)
async def edit_user_full_name(msg: types.Message, state: FSMContext):
    await db.edit_fio(msg.from_user.id, msg.text)
    if msg.from_user.id in ID_ADMIN:
        await msg.answer("akkaunt yangilandi", reply_markup=kb_admin)
    else:
        await msg.answer("akkaunt yangilandi", reply_markup=kb)
    await settings(msg)

    await state.finish()



@dp.message_handler(Text(equals="Kontaktlar📞"))
async def contacts(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer(
            await db.db_contacts(), parse_mode="html", reply_markup=kb_admin
        )
    else:
        await msg.answer(await db.db_contacts(), parse_mode="html", reply_markup=kb)


@dp.message_handler(Text(equals="Biz haqimizda🪪"))
async def about_us(msg: types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer(await db.db_about_us(), reply_markup=kb_admin)
    else:
        await msg.answer(await db.db_about_us(), reply_markup=kb)



##_______TOVAR KUSHISH__________
@dp.message_handler(Text(equals='Tovar kushish+'))
async def add_product(msg:types.Message):
    if msg.from_user.id in ID_ADMIN:
        await msg.answer('tovarni nomini kiriting: ',reply_markup=back_org)
        await AddProduct.first()
    else:
        await msg.answer('siz admin emassiz')
@dp.message_handler(state=AddProduct.name)
async def add_product_name(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name']=msg.text
    await msg.answer('tovar haqida malumot kiriting: ')
    await AddProduct.next()

@dp.message_handler(state=AddProduct.desc)
async def add_product_desc(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['desc']=msg.text
    await msg.answer('tovarni narxini kiriting <b>(so`mda)</b>:',parse_mode='html')
    await AddProduct.next()


@dp.message_handler(state=AddProduct.price)
async def add_product_price(msg:types.Message,state:FSMContext):
    category = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in await db.kb_category():
        category.add(KeyboardButton(i[4]))
    category.add(KeyboardButton('Bekor qilish'))
    for i in category:
        for a in i:
            if type(a) == type(True):
                pass
            else:
                for b in a:
                    if type(b) == type(list()):
                        for g in b:
                            print(g['text'])
                    else:
                        pass
    async with state.proxy() as data:
        data['price']=msg.text
    await msg.answer('tovarni kategoryasini kiriting: ',reply_markup=category)
    await AddProduct.next()

@dp.message_handler(state=AddProduct.category)
async def add_product_category(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['category']=msg.text

    await msg.answer('tovarni rasmini yuboring :')
    await AddProduct.next()

@dp.message_handler(state=AddProduct.photo,content_types=['photo'])
async def add_product_photo(msg:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['photo_id']=msg.photo[0].file_id
        await db.add_product(data)    
    await msg.answer('tovar kushildi✅',reply_markup=kb_admin)
    await state.finish()

@dp.message_handler(Text(equals='Biz haqimizda malumot qo`shish+'))
async def add_data_about_us_start(msg:types.Message):
    await msg.answer('firma haqida malumot qo`shing: ')
    await AddAboutUs.first()

@dp.message_handler(state=AddAboutUs.text)
async def add_data_about_us(msg:types.Message,state:FSMContext):
    await db.insert_about_us(msg.text)
    await state.finish()
    await msg.answer('malumot qo`shildi')

def register_admin_handlers(dp: Dispatcher):
    pass
