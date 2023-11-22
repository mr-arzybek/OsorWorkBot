# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, bot, POSTGRES_URL, Director
import asyncpg

# ====================================================================================================================
global connection
connection = asyncpg.connect(POSTGRES_URL)


async def handle_sql_command_products(message: types.Message, city_query: str):
    products = connection.execute(f"SELECT * FROM products_coming WHERE city = '{city_query}'").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[9], caption=f"Товар: {product[1]}\n"
                                                                                 f"Информация о товаре: {product[2]}\n"
                                                                                 f"Дата прихода: {product[3]}\n"
                                                                                 f"Цена: {product[4]}]\n"
                                                                                 f"Город: {product[5]}\n"
                                                                                 f"Артикул: {product[7]}\n"
                                                                                 f"Количество: {product[8]}\n")
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_bish(message: types.Message):
    await handle_sql_command_products(message, 'Бишкек')

async def sql_command_products_osh(message: types.Message):
    await handle_sql_command_products(message, 'ОШ')

async def sql_command_products_moscow_1(message: types.Message):
    await handle_sql_command_products(message, 'Москва_1')

async def sql_command_products_moscow_2(message: types.Message):
    await handle_sql_command_products(message, 'Москва_2')


def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_products_bish, commands=['Товары_Бишкек(Приход)'])
    dp.register_message_handler(sql_command_products_osh, commands=['Товары_Ош(Приход)'])
    dp.register_message_handler(sql_command_products_moscow_1, commands=['Товары_Москва_1(Приход)'])
    dp.register_message_handler(sql_command_products_moscow_2, commands=['Товары_Москва_2(Приход)'])
