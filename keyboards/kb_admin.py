from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

back = KeyboardButton("назад◀️")
back_category = KeyboardButton("назад")
kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
k1 = KeyboardButton("Katalog🗂")
k2 = KeyboardButton("Savatcha🗑")
k3 = KeyboardButton("Biz haqimizda🪪")
k4 = KeyboardButton("Kontaktlar📞")
k5 = KeyboardButton("Sozlamalar⚙️")
kb.add(k1).add(k2, k3, k4, k5)

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
k1_admin = KeyboardButton("Katalog🗂")
k2_admin = KeyboardButton("Savatcha🗑")
k3_admin = KeyboardButton("Biz haqimizda🪪")
k4_admin = KeyboardButton("Kontaktlar📞")
k5_admin = KeyboardButton("Sozlamalar⚙️")
k6_admin = KeyboardButton("Foydalanuvchilar Ro`yhati")
k7_admin = KeyboardButton("Tovar kushish+")
k8_admin = KeyboardButton("Kontakt kushish+")
kb_admin.add(k1_admin).add(
    k2_admin, k3_admin, k4_admin, k5_admin, k6_admin, k7_admin, k8_admin
)

katalog = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
kt_1 = KeyboardButton("Детский мир")
kt_2 = KeyboardButton("Транспорт")
kt_3 = KeyboardButton("Для дома")
kt_4 = KeyboardButton("Электроника")
kt_5 = KeyboardButton("Сырьё/Материалы")
kt_6 = KeyboardButton("Одежда")
katalog.add(kt_1, kt_2, kt_3, kt_4, kt_5, kt_6, back)

detskiy_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
d_1 = KeyboardButton("детская одежда")
d_2 = KeyboardButton("детская обувь")
d_3 = KeyboardButton("прочие")
detskiy_m.add(d_1, d_2, d_3).add(back_category)

dom_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
dom_1 = KeyboardButton("мебель")
dom_2 = KeyboardButton("посуда")
dom_3 = KeyboardButton("концтовары")
dom_m.add(dom_1, dom_2, dom_3).add(back_category)

transport_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
trans_1 = KeyboardButton("мотоскутера")
trans_2 = KeyboardButton("запчасти далман")
trans_3 = KeyboardButton("прочие")
transport_m.add(
    trans_1,
    trans_2,
    trans_3,
).add(back_category)

electronic_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
electr_1 = KeyboardButton("телефоны")
electr_2 = KeyboardButton("телевизоры")
electr_3 = KeyboardButton("фены")
electr_4 = KeyboardButton("вылесосы")
electr_5 = KeyboardButton("компьютеры")
electr_6 = KeyboardButton("аудиотехника")
electr_7 = KeyboardButton("техника для дома")
electr_8 = KeyboardButton("техника для кухни")
electr_9 = KeyboardButton("аксессуары")
electronic_m.add(
    electr_1,
    electr_2,
    electr_3,
    electr_4,
    electr_5,
    electr_6,
    electr_7,
    electr_8,
    electr_9,
).add(back_category)

materials_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
materials_1 = KeyboardButton("гвозди")
materials_2 = KeyboardButton("прочие")
materials_m.add(materials_1, materials_2).add(back_category)

clothes_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
clothes_1 = KeyboardButton("мужская")
clothes_2 = KeyboardButton("женская")
clothes_3 = KeyboardButton("обувь")
clothes_4 = KeyboardButton("наручные часы")
clothes_5 = KeyboardButton("прочие")
clothes_m.add(clothes_1, clothes_2, clothes_3, clothes_4, clothes_5).add(back_category)

phone_kb = ReplyKeyboardMarkup(resize_keyboard=True)
phone_k1 = KeyboardButton("Отправть контакт", request_contact=True)
phone_kb.add(phone_k1)

lang_kb = ReplyKeyboardMarkup(resize_keyboard=True)
lang_uz = KeyboardButton("UZ")
lang_ru = KeyboardButton("RU")
lang_eng = KeyboardButton("ENG")
lang_kb.add(lang_uz, lang_ru, lang_eng)

for_contact = InlineKeyboardMarkup(row_width=3)
contact_name = InlineKeyboardButton(text='F.I.O',callback_data='')
contact_phone_number = InlineKeyboardButton(text='telefon raqam')
contact_lang = InlineKeyboardButton(text='Til')
for_contact.add(contact_name,contact_phone_number,contact_lang)