from aiogram.dispatcher.filters.state import State, StatesGroup

class UserRegister(StatesGroup):
    lang = State()
    user_name= State()
    phone_number = State()
