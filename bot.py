import logging
from aiogram import Dispatcher,Bot,types,executor
from handlers import admin,client,register_user
from aiogram.dispatcher.filters import Text
from create_bot import dp


admin.register_admin_handlers(dp)
client.register_client_handlers(dp)
register_user.register_user_handlers(dp)

logging.basicConfig(level=logging.INFO)
executor.start_polling(dp,skip_updates=True)

