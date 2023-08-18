from aiogram.utils import executor
import logging
from config import dp
from handlers import commands, FSM_products

commands.register_commands(dp)
FSM_products.register_products(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
