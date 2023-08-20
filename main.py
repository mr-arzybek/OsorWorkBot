from aiogram.utils import executor
import logging
from config import dp
from handlers import commands
from handlers.FSM import FSM_products, FSM_booking, FSM_reg_staff, FSM_being_late
from db.orm import sql_create


async def on_startup(_):
    sql_create()


commands.register_commands(dp)
FSM_products.register_products(dp)
FSM_booking.register_booking(dp)
FSM_reg_staff.register_staff(dp)
FSM_being_late.register_control(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
