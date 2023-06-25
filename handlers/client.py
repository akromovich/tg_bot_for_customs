from handlers.admin import catalog
from handlers.register_user import start,main_menu
from create_bot import dp
from aiogram import Dispatcher, types
from aiogram.types import InputFile

from keyboards.kb_admin import *


@dp.message_handler()
async def asd(msg: types.Message):
    if msg.text == 'назад◀️':
        await main_menu(msg)
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
    elif msg.text == 'Biz haqimizda🪪':
        file = InputFile(f'media/logo.jpg')
        await msg.answer_photo(file)
        await msg.answer('Адрес: город Ташкент, проспект Бунёдкор,\n35.Индекс: 100185\nТелефон: (71) 207-09-39\nТелефоны доверия: 11-08\nЭлектронная почта: toshkent_shahri@customs.uz\nОриентир: Метро Чиланзар, Сингапурскийинститут развития менеджмента\nТранспортные средства проезжающие возле управления:Автобусы - №21, 41, 74, 86, 100, 116, \nмаршрутные такси - №17, 19,40.\nГород Ташкент является крупнейшим центром железнодорожных, автомобильных и воздушных узлов страны, занимает площадь в327,9 км2.На территорииУправления Государственного таможенного комитета Республики Узбекистан по городу Ташсвоюдеятельностьосуществляют 8 таможенных постов, 6 из которых– по направлению внешней экономической деятельнос2являютсяприграничными таможенными постами.В структуре УГТК по г.Ташкенту 2 таможенных поста,отвечающих международным стандартам, это железнодорожныетаможенныепо«Келес» и «Чукурсай - техническая контора».На таможенном посту «Келес»осуществляется досмотр и таможенное оформление пассажиров, въезжающих в республику ивыезжаюеё пределы, а также их багажа на железнодорожномтранспорте.Таможенный пост «Чукурсай - техническая контора» осуществляет таможенный досмотр грузовых вагонов и контейнеров,въезжареспублику ивыезжающих за её пределы, а также перемещаемых транзитом.В деятельность таможенных постов ВЭД УГТК по г. Ташкенту входит осуществление таможенногодосмотра и оформлениявтаможотношении экспортируемых и импортируемых участниками внешней экономической деятельности грузов,взиманиятаможенныхплатеприменения таможенных режимов.На таможенных постах ВЭД «Ташкент-товарный», «Чукурсай» и «Сергели» осуществляется таможенныйдосвзиманиеначислениетаможенных платежей и таможенное оформление грузов, ввозимых и вывозимых из республжелезнодорожныхвагонах иконтейнерахгосударственных организаций, совместных предприятий и частных фирм, а предпринимателей.На таможенном посту ВЭД «Арк-булак» осуществляетсятаможенное оформление товаров организаций и предпросуществляющихэкспортно-импортные операции, перемещаемые грузовым автотранспортом.Город Ташкентпо праву называют «Воротами Востока». Здесь расположены посольства, дипломатические миссстранипредставительства многих международных организаций.В республике единственный таможенныйВЭД«Иностранныепредставительства» осуществляет таможенное оформление транспортных средств и грузов, ввозимыхдлятакихпосольств ипредставительств.')
    else:
        pass


def register_client_handlers(dp: Dispatcher):
    pass
