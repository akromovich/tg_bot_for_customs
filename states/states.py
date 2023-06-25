from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegister(StatesGroup):
    f_i_o = State()
    phone_number = State()
    lang = State()

class EditUserDataFullName(StatesGroup):
    full_name = State()

class EditUserDataPhoneNumber(StatesGroup):
    phone_number = State()

class EditUserDataLang(StatesGroup):
    lang = State()