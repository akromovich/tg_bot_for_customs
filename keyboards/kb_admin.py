from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import db

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
k9_admin  = KeyboardButton('Biz haqimizda malumot qo`shish+')
kb_admin.add(k1_admin).add(
    k2_admin, k3_admin, k4_admin, k5_admin, k6_admin, k7_admin, k8_admin,k9_admin
)


phone_kb = ReplyKeyboardMarkup(resize_keyboard=True)
phone_k1 = KeyboardButton("Отправть контакт", request_contact=True)
phone_kb.add(phone_k1)

phone_kb_for_edit = ReplyKeyboardMarkup(resize_keyboard=True)
phone_kb_for_edit_kb_1 = KeyboardButton(
    'Telefon_raqam_yuborish', request_contact=True)
phone_kb_for_edit_kb_2 = KeyboardButton('Bekor qilish')
phone_kb_for_edit.add(phone_kb_for_edit_kb_1).add(phone_kb_for_edit_kb_2)

lang_kb = ReplyKeyboardMarkup(resize_keyboard=True)
lang_uz = KeyboardButton("UZ")
lang_ru = KeyboardButton("RU")
lang_eng = KeyboardButton("ENG")
lang_back = KeyboardButton('Bekor qilish')
lang_kb.add(lang_uz, lang_ru, lang_eng).add(lang_back)


back_org = ReplyKeyboardMarkup(resize_keyboard=True)
back_org_kb = KeyboardButton('Bekor qilish')
back_org.add(back_org_kb)

for_contact = InlineKeyboardMarkup(row_width=3)
contact_name = InlineKeyboardButton(
    text='F.I.O', callback_data='shaxsiy isimni o`zgartirish')
contact_phone_number = InlineKeyboardButton(
    text='telefon raqam', callback_data='shaxsiy telefon o`zgartirish')
contact_lang = InlineKeyboardButton(
    text='Til', callback_data='shaxsiy tilni o`zgartirish')
for_contact.add(contact_name, contact_phone_number, contact_lang)



