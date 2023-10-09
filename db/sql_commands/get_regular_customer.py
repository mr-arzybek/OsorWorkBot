from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from aiogram import types, Dispatcher


# ====================================================================================================================


async def super_customer_moscow_1(message: types.Message):
    cursor_moscow_1.execute("SELECT phone_customer, name_customer FROM products_care")
    customers = cursor_moscow_1.fetchall()
    results = {}

    for customer in customers:
        phone = customer[0]
        if phone not in results:
            cursor_moscow_1.execute("SELECT SUM(total_price) FROM products_care WHERE phone_customer = ?", (phone,))
            total_price = cursor_moscow_1.fetchone()[0]
            if total_price > 10000:
                results[phone] = total_price
                vip_photo = open("media/vip_card.png", "rb")
                await message.answer_photo(photo=vip_photo, caption=f"Имя - {customer[1]}\n"
                                                                    f"Номер телефона - {phone}\n"
                                                                    f"Общая сумма покупок - {total_price}")


async def super_customer_moscow_2(message: types.Message):
    cursor_moscow_2.execute("SELECT phone_customer, name_customer FROM products_care")
    customers = cursor_moscow_2.fetchall()
    results = {}

    for customer in customers:
        phone = customer[0]
        if phone not in results:
            cursor_moscow_2.execute("SELECT SUM(total_price) FROM products_care WHERE phone_customer = ?", (phone,))
            total_price = cursor_moscow_2.fetchone()[0]
            if total_price > 10000:
                results[phone] = total_price
                vip_photo = open("media/vip_card.png", "rb")
                await message.answer_photo(photo=vip_photo, caption=f"Имя - {customer[1]}\n"
                                                                    f"Номер телефона - {phone}\n"
                                                                    f"Общая сумма покупок - {total_price}")


async def super_customer_bishkek(message: types.Message):
    cursor_bish.execute("SELECT phone_customer, name_customer FROM products_care")
    customers = cursor_bish.fetchall()
    results = {}

    for customer in customers:
        phone = customer[0]
        if phone not in results:
            cursor_bish.execute("SELECT SUM(total_price) FROM products_care WHERE phone_customer = ?", (phone,))
            total_price = cursor_bish.fetchone()[0]
            if total_price > 10000:
                results[phone] = total_price
                vip_photo = open("media/vip_card.png", "rb")
                await message.answer_photo(photo=vip_photo, caption=f"Имя - {customer[1]}\n"
                                                                    f"Номер телефона - {phone}\n"
                                                                    f"Общая сумма покупок - {total_price}")


async def super_customer_osh(message: types.Message):
    cursor_osh.execute("SELECT phone_customer, name_customer FROM products_care")
    customers = cursor_osh.fetchall()
    results = {}

    for customer in customers:
        phone = customer[0]
        if phone not in results:
            cursor_osh.execute("SELECT SUM(total_price) FROM products_care WHERE phone_customer = ?", (phone,))
            total_price = cursor_osh.fetchone()[0]
            if total_price > 10000:
                results[phone] = total_price
                vip_photo = open("media/vip_card.png", "rb")
                await message.answer_photo(photo=vip_photo, caption=f"Имя - {customer[1]}\n"
                                                                    f"Номер телефона - {phone}\n"
                                                                    f"Общая сумма покупок - {total_price}")


def register_super_customers(dp: Dispatcher):
    dp.register_message_handler(super_customer_moscow_1, commands=['Клиенты_Москва_1'])
    dp.register_message_handler(super_customer_moscow_2, commands=['Клиенты_Москва_2'])
    dp.register_message_handler(super_customer_bishkek, commands=['Клиенты_Бишкек'])
    dp.register_message_handler(super_customer_osh, commands=['Клиенты_Ош'])
