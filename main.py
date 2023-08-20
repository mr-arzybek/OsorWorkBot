from aiogram.utils import executor
import logging
from config import dp
from handlers import commands, FSM_products
from db.orm import sql_create


async def on_startup(_):
    sql_create()


commands.register_commands(dp)
FSM_products.register_products(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
