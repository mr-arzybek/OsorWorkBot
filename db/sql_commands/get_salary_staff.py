# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, Director

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================
async def salary_salesman_bishkek(message: types.Message):
    cursor_bish.execute("SELECT DISTINCT phone_salesman, name_salesman FROM products_care")
    customers = cursor_bish.fetchall()
    percentage = 4

    cursor_bish.execute("SELECT * FROM staff")

    if message.from_user.id in Admins or Director:
        if len(customers) == 0:
            await message.answer("Здесь пока ничего нет!")
        else:
            for customer in customers:
                phone_salesman = customer[0]
                cursor_bish.execute("SELECT SUM(total_price) FROM products_care WHERE phone_salesman = ?",
                                    (phone_salesman,))
                total_prices = cursor_bish.fetchone()[0]

                salary = total_prices * (percentage / 100.0)

                await message.answer(f"Имя сотрудника: {customer[0]}\n"
                                     f"Номер телефона сотрудника: {customer[1]}\n"
                                     f"Количество проданных товаров: {len(customers)}\n"
                                     f"Сумма на которую он продал: {total_prices}\n"
                                     f"Его ЗП: {salary}")

    else:
        await message.answer("Вы не админ!")


async def salary_salesman_osh(message: types.Message):
    cursor_osh.execute("SELECT phone_salesman, name_salesman FROM products_care")
    customers = cursor_osh.fetchall()
    percentage = 4

    if message.from_user.id in Admins or Director:
        if len(customers) == 0:
            await message.answer("Здесь пока ничего нет!")
        else:
            for customer in customers:
                phone_salesman = customer[0]
                cursor_osh.execute("SELECT SUM(total_price) FROM products_care WHERE phone_salesman = ?",
                                   (phone_salesman,))
                total_prices = cursor_osh.fetchone()[0]

                salary = total_prices * (percentage / 100.0)

                await message.answer(f"Данные сотрудника: {customers[0]}\n"
                                     f"Количество проданных товаров: {len(customers)}\n"
                                     f"Сумма на которую он продал: {total_prices}\n"
                                     f"Его ЗП: {salary}")
    else:
        await message.answer("Вы не админ!")


async def salary_salesman_moscow_1(message: types.Message):
    cursor_moscow_1.execute("SELECT phone_salesman, name_salesman FROM products_care")
    customers = cursor_moscow_1.fetchall()
    percentage = 4

    if message.from_user.id in Admins or Director:
        if len(customers) == 0:
            await message.answer("Здесь пока ничего нет!")
        else:
            for customer in customers:
                phone_salesman = customer[0]
                cursor_moscow_1.execute("SELECT SUM(total_price) FROM products_care WHERE phone_salesman = ?",
                                        (phone_salesman,))
                total_prices = cursor_moscow_1.fetchone()[0]

                salary = total_prices * (percentage / 100.0)

                await message.answer(f"Данные сотрудника: {customers[0]}\n"
                                     f"Количество проданных товаров: {len(customers)}\n"
                                     f"Сумма на которую он продал: {total_prices}\n"
                                     f"Его ЗП: {salary}")
    else:
        await message.answer("Вы не админ!")


async def salary_salesman_moscow_2(message: types.Message):
    cursor_moscow_2.execute("SELECT phone_salesman, name_salesman FROM products_care")
    customers = cursor_moscow_2.fetchall()
    percentage = 4

    if message.from_user.id in Admins or Director:
        if len(customers) == 0:
            await message.answer("Здесь пока ничего нет!")
        else:
            for customer in customers:
                phone_salesman = customer[0]
                cursor_moscow_2.execute("SELECT SUM(total_price) FROM products_care WHERE phone_salesman = ?",
                                        (phone_salesman,))
                total_prices = cursor_moscow_2.fetchone()[0]

                salary = total_prices * (percentage / 100.0)

                await message.answer(f"Данные сотрудника: {customers[0]}\n"
                                     f"Количество проданных товаров: {len(customers)}\n"
                                     f"Сумма на которую он продал: {total_prices}\n"
                                     f"Его ЗП: {salary}")
    else:
        await message.answer("Вы не админ!")


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(salary_salesman_bishkek, commands=['ЗП_Бишкек'])
    dp.register_message_handler(salary_salesman_osh, commands=['ЗП_Ош'])
    dp.register_message_handler(salary_salesman_moscow_1, commands=['ЗП_Москва_1'])
    dp.register_message_handler(salary_salesman_moscow_2, commands=['ЗП_Москва_2'])
