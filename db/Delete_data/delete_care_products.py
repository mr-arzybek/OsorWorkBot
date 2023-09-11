# ======================================================================================================================
from config import Director, bot

from db.db_bish import ORM_Bish
from db.db_osh import ORM_Osh
from db.db_moscow_1 import ORM_Moscow_1
from db.db_moscow_2 import ORM_Moscow_2

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ======================================================================================================================

async def delete_products_care_command_bish(message: types.Message):
    if message.from_user.id in Director:
        products = await ORM_Bish.sql_command_all_products_care()
        for product in products:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[1]}\n"
                                                                                  f"Информация о товаре: {product[2]}\n"
                                                                                  f"Дата прихода: {product[3]}\n"
                                                                                  f"Имя заказчика: {product[4]}\n"
                                                                                  f"Номер тел заказчика: {product[5]}\n"
                                                                                  f"Продавец: {product[6]}\n"
                                                                                  f"Номер телефона продавца: {product[7]}"
                                                                                  f"Цена(без скидки): {product[8]}\n"
                                                                                  f"Скидка: {product[9]}\n"
                                                                                  f"Итоговая цена: {product[10]}\n"
                                                                                  f"Город: {product[11]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
                                                                                              callback_data=f"delete {product[0]}")))

    else:
        await message.answer("You not Director!")


async def delete_products_care_command_osh(message: types.Message):
    if message.from_user.id in Director:
        products = await ORM_Osh.sql_command_all_products_care()
        for product in products:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[1]}\n"
                                                                                  f"Информация о товаре: {product[2]}\n"
                                                                                  f"Дата прихода: {product[3]}\n"
                                                                                  f"Имя заказчика: {product[4]}\n"
                                                                                  f"Номер тел заказчика: {product[5]}\n"
                                                                                  f"Продавец: {product[6]}\n"
                                                                                  f"Номер телефона продавца: {product[7]}"
                                                                                  f"Цена(без скидки): {product[8]}\n"
                                                                                  f"Скидка: {product[9]}\n"
                                                                                  f"Итоговая цена: {product[10]}\n"
                                                                                  f"Город: {product[11]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
                                                                                              callback_data=f"delete {product[0]}")))

    else:
        await message.answer("You not Director!")


async def delete_products_care_command_moscow_1(message: types.Message):
    if message.from_user.id in Director:
        products = await ORM_Moscow_1.sql_command_all_products_care()
        for product in products:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[1]}\n"
                                                                                  f"Информация о товаре: {product[2]}\n"
                                                                                  f"Дата прихода: {product[3]}\n"
                                                                                  f"Имя заказчика: {product[4]}\n"
                                                                                  f"Номер тел заказчика: {product[5]}\n"
                                                                                  f"Продавец: {product[6]}\n"
                                                                                  f"Номер телефона продавца: {product[7]}"
                                                                                  f"Цена(без скидки): {product[8]}\n"
                                                                                  f"Скидка: {product[9]}\n"
                                                                                  f"Итоговая цена: {product[10]}\n"
                                                                                  f"Город: {product[11]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
                                                                                              callback_data=f"delete {product[0]}")))

    else:
        await message.answer("You not Director!")


async def delete_products_care_command_moscow_2(message: types.Message):
    if message.from_user.id in Director:
        products = await ORM_Moscow_2.sql_command_all_products_care()
        for product in products:
            await bot.send_photo(message.from_user.id, photo=product[12], caption=f"Товар: {product[1]}\n"
                                                                                  f"Информация о товаре: {product[2]}\n"
                                                                                  f"Дата прихода: {product[3]}\n"
                                                                                  f"Имя заказчика: {product[4]}\n"
                                                                                  f"Номер тел заказчика: {product[5]}\n"
                                                                                  f"Продавец: {product[6]}\n"
                                                                                  f"Номер телефона продавца: {product[7]}"
                                                                                  f"Цена(без скидки): {product[8]}\n"
                                                                                  f"Скидка: {product[9]}\n"
                                                                                  f"Итоговая цена: {product[10]}\n"
                                                                                  f"Город: {product[11]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
                                                                                              callback_data=f"delete {product[0]}")))

    else:
        await message.answer("You not Director!")


# ======================================================================================================================

async def complete_delete(call: types.CallbackQuery):
    await ORM_Bish.sql_command_delete_care(call.data.replace("delete ", ""))
    await ORM_Osh.sql_command_delete_care(call.data.replace("delete ", ""))
    await ORM_Moscow_1.sql_command_delete_care(call.data.replace("delete ", ""))
    await ORM_Moscow_2.sql_command_delete_care(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_products_care_command_bish, commands=['Удал_Прода_Bishkek'])
    dp.register_message_handler(delete_products_care_command_osh, commands=['Удал_Прода_Osh'])
    dp.register_message_handler(delete_products_care_command_moscow_1, commands=['Удал_Прода_Moscow_1'])
    dp.register_message_handler(delete_products_care_command_moscow_2, commands=['Удал_Прода_Moscow_2'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("delete "))

