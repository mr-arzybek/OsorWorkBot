# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, bot, POSTGRES_URL, Director
import asyncpg

# ====================================================================================================================
global connection
connection = await asyncpg.connect(POSTGRES_URL)


async def sql_command_products_bish(message: types.Message):
    products = connection.execute("SELECT * FROM products_coming WHERE city = 'Бишкек'").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
                                                                                 f"Информация о товаре: {product[2]}\n"
                                                                                 f"Дата прихода: {product[3]}\n"
                                                                                 f"Цена: {product[4]}]\n"
                                                                                 f"Город: {product[5]}\n"
                                                                                 f"Артикул: {product[6]}\n"
                                                                                 f"Количество: {product[7]}\n")
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_osh(message: types.Message):
    products = connection.execute("SELECT * FROM products_coming WHERE city = 'Ош'").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
                                                                                 f"Информация о товаре: {product[2]}\n"
                                                                                 f"Дата прихода: {product[3]}\n"
                                                                                 f"Цена: {product[4]}]\n"
                                                                                 f"Город: {product[5]}\n"
                                                                                 f"Артикул: {product[6]}\n"
                                                                                 f"Количество: {product[7]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_moscow_1(message: types.Message):
    products = connection.execute("SELECT * FROM products_coming WHERE city = 'Москва_1'").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
                                                                                 f"Информация о товаре: {product[2]}\n"
                                                                                 f"Дата прихода: {product[3]}\n"
                                                                                 f"Цена: {product[4]}]\n"
                                                                                 f"Город: {product[5]}\n"
                                                                                 f"Артикул: {product[6]}\n"
                                                                                 f"Количество: {product[7]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_moscow_2(message: types.Message):
    products = connection.execute("SELECT * FROM products_coming WHERE city = 'Москва_2'").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
                                                                                 f"Информация о товаре: {product[2]}\n"
                                                                                 f"Дата прихода: {product[3]}\n"
                                                                                 f"Цена: {product[4]}]\n"
                                                                                 f"Город: {product[5]}\n"
                                                                                 f"Артикул: {product[6]}\n"
                                                                                 f"Количество: {product[7]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_products_bish, commands=['Товары_Бишкек(Приход)'])
    dp.register_message_handler(sql_command_products_osh, commands=['Товары_Ош(Приход)'])
    dp.register_message_handler(sql_command_products_moscow_1, commands=['Товары_Москва_1(Приход)'])
    dp.register_message_handler(sql_command_products_moscow_2, commands=['Товары_Москва_2(Приход)'])
