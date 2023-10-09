# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, bot, Director

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================

async def sql_command_products_bish(message: types.Message):
    products = cursor_bish.execute("SELECT * FROM products_care").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
                                                                                  f"Информация о товаре: {product[14]}\n"
                                                                                  f"Дата ухода: {product[1]}\n"
                                                                                  f"Имя заказчика: {product[2]}\n"
                                                                                  f"Номер тел заказчика: {product[3]}\n"
                                                                                  f"Продавец: {product[4]}\n"
                                                                                  f"Номер телефона продавца: {product[5]}\n"
                                                                                  f"Цена(без скидки): {product[6]}\n"
                                                                                  f"Скидка: {product[7]}\n"
                                                                                  f"Итоговая цена: {product[8]}\n"
                                                                                  f"Город: {product[9]}\n"
                                                                                  f"Артикул: {product[10]}\n"
                                                                                  f"количество: {product[11]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_osh(message: types.Message):
    products = cursor_osh.execute("SELECT * FROM products_care").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
                                                                                  f"Информация о товаре: {product[14]}\n"
                                                                                  f"Дата ухода: {product[1]}\n"
                                                                                  f"Имя заказчика: {product[2]}\n"
                                                                                  f"Номер тел заказчика: {product[3]}\n"
                                                                                  f"Продавец: {product[4]}\n"
                                                                                  f"Номер телефона продавца: {product[5]}\n"
                                                                                  f"Цена(без скидки): {product[6]}\n"
                                                                                  f"Скидка: {product[7]}\n"
                                                                                  f"Итоговая цена: {product[8]}\n"
                                                                                  f"Город: {product[9]}\n"
                                                                                  f"Артикул: {product[10]}\n"
                                                                                  f"количество: {product[11]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_moscow_1(message: types.Message):
    products = cursor_moscow_1.execute("SELECT * FROM products_care").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
                                                                                  f"Информация о товаре: {product[14]}\n"
                                                                                  f"Дата ухода: {product[1]}\n"
                                                                                  f"Имя заказчика: {product[2]}\n"
                                                                                  f"Номер тел заказчика: {product[3]}\n"
                                                                                  f"Продавец: {product[4]}\n"
                                                                                  f"Номер телефона продавца: {product[5]}\n"
                                                                                  f"Цена(без скидки): {product[6]}\n"
                                                                                  f"Скидка: {product[7]}\n"
                                                                                  f"Итоговая цена: {product[8]}\n"
                                                                                  f"Город: {product[9]}\n"
                                                                                  f"Артикул: {product[10]}\n"
                                                                                  f"количество: {product[11]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


async def sql_command_products_moscow_2(message: types.Message):
    products = cursor_moscow_2.execute("SELECT * FROM products_care").fetchall()

    for product in products:
        if message.from_user.id in Admins or Director:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[13]}\n"
                                                                                  f"Информация о товаре: {product[14]}\n"
                                                                                  f"Дата ухода: {product[1]}\n"
                                                                                  f"Имя заказчика: {product[2]}\n"
                                                                                  f"Номер тел заказчика: {product[3]}\n"
                                                                                  f"Продавец: {product[4]}\n"
                                                                                  f"Номер телефона продавца: {product[5]}\n"
                                                                                  f"Цена(без скидки): {product[6]}\n"
                                                                                  f"Скидка: {product[7]}\n"
                                                                                  f"Итоговая цена: {product[8]}\n"
                                                                                  f"Город: {product[9]}\n"
                                                                                  f"Артикул: {product[10]}\n"
                                                                                  f"количество: {product[11]}\n"
                                 )
        else:
            await message.answer("Вы не админ!")


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_products_bish, commands=['Товары_Биш(Проданные)', ])
    dp.register_message_handler(sql_command_products_osh, commands=['Товары_Ош(Проданные)'])
    dp.register_message_handler(sql_command_products_moscow_1, commands=['Товары_М1(Проданные)'])
    dp.register_message_handler(sql_command_products_moscow_2, commands=['Товары_М2(Проданные)'])
