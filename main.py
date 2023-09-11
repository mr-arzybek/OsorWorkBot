from aiogram.utils import executor
import logging
from config import dp, bot, Admins, Director
from handlers import commands
from handlers.FSM import (FSM_coming_products, FSM_care_products, FSM_booking, FSM_reg_staff, FSM_being_late)

from db.db_bish.ORM_Bish import sql_create_bish
from db.db_osh.ORM_Osh import sql_create_osh
from db.db_moscow_1.ORM_Moscow_1 import sql_create_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import sql_create_moscow_2

from db.Delete_data import delete_care_products, delete_coming_products, delete_booking, delete_staff

from db.sql_commands import get_products_comming, get_booking, get_staff, \
    get_salary_staff, get_products_care, get_regular_customer
from db.checkout_control import get_info_ForControl
from keyboards import buttons


# ===========================================================================
async def on_startup(_):
    await bot.send_message(chat_id=Admins[0], text="Бот запущен!", reply_markup=buttons.start_admins_markup)
    await bot.send_message(chat_id=Director[0], text="Бот запущен!", reply_markup=buttons.start_director_markup)
    sql_create_bish()
    sql_create_osh()
    sql_create_moscow_1()
    sql_create_moscow_2()


# ===========================================================================
commands.register_commands(dp)

FSM_coming_products.register_products(dp)
FSM_care_products.register_products(dp)
FSM_booking.register_booking(dp)
FSM_reg_staff.register_staff(dp)
FSM_being_late.register_control(dp)
# =====================================================
get_products_comming.register_sql_commands(dp)
get_products_care.register_sql_commands(dp)
get_booking.register_sql_commands(dp)
get_staff.register_sql_commands(dp)
get_salary_staff.register_sql_commands(dp)
get_regular_customer.register_super_customers(dp)
# ===========================================================================
get_info_ForControl.register_control(dp)
# ===========================================================================
delete_care_products.register_handler_admin(dp)
delete_coming_products.register_handler_admin(dp)
delete_booking.register_handler_admin(dp)
delete_staff.register_handler_admin(dp)
# ===========================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
