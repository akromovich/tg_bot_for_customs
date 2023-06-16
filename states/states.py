from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegister(StatesGroup):
    f_i_o = State()
    phone_number = State()
    lang = State()
