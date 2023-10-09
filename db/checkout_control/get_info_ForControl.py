from aiogram import Dispatcher, types
from config import bot
from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2
from config import Admins


async def control_day_bish(message: types.Message):
    products = cursor_bish.execute("SELECT * FROM products_care WHERE DATE(creation_time) = DATE('now')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за сегодня - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за сегодня - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


async def control_bishkek_month(message: types.Message):
    products = cursor_bish.execute(
        "SELECT * FROM products_care WHERE strftime('%Y-%m', creation_time) = strftime('%Y-%m', 'now')").fetchall()
    total_sum_mon = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_mon.append(product[8])
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
        await message.answer(f"Проданная сумма за месяц - {sum(total_sum_mon)}\n"
                             f"кол-во проданных товаров за месяц - {len(total_sum_mon)}")
    else:
        await message.answer("Вы не админ!")


async def control_day_osh(message: types.Message):
    products = cursor_osh.execute("SELECT * FROM products_care WHERE DATE(creation_time) = DATE('now')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за сегодня - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за сегодня - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


async def control_osh_month(message: types.Message):
    products = cursor_osh.execute(
        "SELECT * FROM products_care WHERE strftime('%Y-%m', creation_time) = strftime('%Y-%m', 'now')").fetchall()
    total_sum_mon = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_mon.append(product[8])
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
        await message.answer(f"Проданная сумма за месяц - {sum(total_sum_mon)}\n"
                             f"кол-во проданных товаров за месяц - {len(total_sum_mon)}")
    else:
        await message.answer("Вы не админ!")


async def control_day_moscow_1(message: types.Message):
    products = cursor_moscow_1.execute("SELECT * FROM products_care WHERE DATE(creation_time) = DATE('now')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за сегодня - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за сегодня - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


async def control_moscow_1_month(message: types.Message):
    products = cursor_moscow_1.execute(
        "SELECT * FROM products_care WHERE strftime('%Y-%m', creation_time) = strftime('%Y-%m', 'now')").fetchall()
    total_sum_mon = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_mon.append(product[8])
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
        await message.answer(f"Проданная сумма за месяц - {sum(total_sum_mon)}\n"
                             f"кол-во проданных товаров за месяц - {len(total_sum_mon)}")
    else:
        await message.answer("Вы не админ!")


async def control_day_moscow_2(message: types.Message):
    products = cursor_moscow_2.execute("SELECT * FROM products_care WHERE DATE(creation_time) = DATE('now')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за сегодня - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за сегодня - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


async def control_moscow_2_month(message: types.Message):
    products = cursor_moscow_2.execute(
        "SELECT * FROM products_care WHERE strftime('%Y-%m', creation_time) = strftime('%Y-%m', 'now')").fetchall()
    total_sum_mon = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_mon.append(product[8])
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
        await message.answer(f"Проданная сумма за месяц - {sum(total_sum_mon)}\n"
                             f"кол-во проданных товаров за месяц - {len(total_sum_mon)}")
    else:
        await message.answer("Вы не админ!")



# ===================================================================================================
""" Отчет за неделю """
async def control_week_bish(message: types.Message):
    products = cursor_bish.execute("SELECT * FROM products_care WHERE creation_time >= DATE('now', '-7 days')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за неделю - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за неделю - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


async def control_week_osh(message: types.Message):
    products = cursor_osh.execute("SELECT * FROM products_care WHERE creation_time >= DATE('now', '-7 days')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за неделю - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за неделю - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")

async def control_week_moscow_1(message: types.Message):
    products = cursor_moscow_1.execute("SELECT * FROM products_care WHERE creation_time >= DATE('now', '-7 days')").fetchall()
    total_sum_mon = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_mon.append(product[8])
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
        await message.answer(f"Проданная сумма за неделю - {sum(total_sum_mon)}\n"
                             f"кол-во проданных товаров за неделю - {len(total_sum_mon)}")
    else:
        await message.answer("Вы не админ!")

async def control_week_moscow_2(message: types.Message):
    products = cursor_moscow_2.execute("SELECT * FROM products_care WHERE creation_time >= DATE('now', '-7 days')").fetchall()
    total_sum_day = []
    if message.from_user.id in Admins:
        for product in products:
            total_sum_day.append(product[8])
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
        await message.answer(f"Проданная сумма за неделю - {sum(total_sum_day)}\n"
                             f"кол-во проданных товаров за неделю - {len(total_sum_day)}")
    else:
        await message.answer("Вы не админ!")


def register_control(dp: Dispatcher):
    dp.register_message_handler(control_bishkek_month, commands=["Отчет_за_месяц_Б"])
    dp.register_message_handler(control_day_bish, commands=["Отчет_за_день_Б"])

    dp.register_message_handler(control_osh_month, commands=['Отчет_за_месяц_Ош'])
    dp.register_message_handler(control_day_osh, commands=["Отчет_за_день_Ош"])

    dp.register_message_handler(control_moscow_1_month, commands=['Отчет_за_месяц_М_1'])
    dp.register_message_handler(control_day_moscow_1, commands=["Отчет_за_день_М_1"])

    dp.register_message_handler(control_moscow_2_month, commands=['Отчет_за_месяц_М_2'])
    dp.register_message_handler(control_day_moscow_2, commands=["Отчет_за_день_М_2"])

    dp.register_message_handler(control_week_bish, commands=['Отчет_за_неделю_Б'])
    dp.register_message_handler(control_week_osh, commands=['Отчет_за_неделю_Ош'])
    dp.register_message_handler(control_week_moscow_1, commands=['Отчет_за_неделю_М_1'])
    dp.register_message_handler(control_week_moscow_2, commands=['Отчет_за_неделю_М_2'])
