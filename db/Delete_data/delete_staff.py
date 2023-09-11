# ======================================================================================================================
from config import Director, bot

from db.db_bish import ORM_Bish
from db.db_osh import ORM_Osh
from db.db_moscow_1 import ORM_Moscow_1
from db.db_moscow_2 import ORM_Moscow_2

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ======================================================================================================================

async def delete_staff_bish(message: types.Message):
    if message.from_user.id in Director:
        employees = await ORM_Bish.sql_command_all_staff()
        for staff in employees:
            await bot.send_photo(message.from_user.id, photo=staff[6], caption=f"Имя: {staff[1]}\n"
                                                                               f"Номер тел: {staff[2]}\n"
                                                                               f"Информация о сотруднике: {staff[3]}\n"
                                                                               f"График: {staff[4]}\n"
                                                                               f"Филиал: {staff[5]}",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {staff[0]}",
                                                                                              callback_data=f"delete {staff[0]}")))

    else:
        await message.answer("Вы не директор!")


async def delete_staff_osh(message: types.Message):
    if message.from_user.id in Director:
        employees = await ORM_Osh.sql_command_all_staff()
        for staff in employees:
            await bot.send_photo(message.from_user.id, photo=staff[6], caption=f"Имя: {staff[1]}\n"
                                                                               f"Номер тел: {staff[2]}\n"
                                                                               f"Информация о сотруднике: {staff[3]}\n"
                                                                               f"График: {staff[4]}\n"
                                                                               f"Филиал: {staff[5]}",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {staff[0]}",
                                                                                              callback_data=f"delete {staff[0]}")))

    else:
        await message.answer("Вы не директор!")


async def delete_staff_Mescow_1(message: types.Message):
    if message.from_user.id in Director:
        employees = await ORM_Moscow_1.sql_command_all_staff()
        for staff in employees:
            await bot.send_photo(message.from_user.id, photo=staff[6], caption=f"Имя: {staff[1]}\n"
                                                                               f"Номер тел: {staff[2]}\n"
                                                                               f"Информация о сотруднике: {staff[3]}\n"
                                                                               f"График: {staff[4]}\n"
                                                                               f"Филиал: {staff[5]}",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {staff[0]}",
                                                                                              callback_data=f"delete {staff[0]}")))

    else:
        await message.answer("Вы не директор!")


async def delete_staff_Mescow_2(message: types.Message):
    if message.from_user.id in Director:
        employees = await ORM_Moscow_2.sql_command_all_staff()
        for staff in employees:
            await bot.send_photo(message.from_user.id, photo=staff[6], caption=f"Имя: {staff[1]}\n"
                                                                               f"Номер тел: {staff[2]}\n"
                                                                               f"Информация о сотруднике: {staff[3]}\n"
                                                                               f"График: {staff[4]}\n"
                                                                               f"Филиал: {staff[5]}",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {staff[0]}",
                                                                                              callback_data=f"delete {staff[0]}")))

    else:
        await message.answer("Вы не директор!")


# ======================================================================================================================

async def complete_delete(call: types.CallbackQuery):
    await ORM_Bish.sql_command_delete_staff(call.data.replace("Удалить ", ""))
    await ORM_Osh.sql_command_delete_staff(call.data.replace("Удалить ", ""))
    await ORM_Moscow_1.sql_command_delete_staff(call.data.replace("Удалить ", ""))
    await ORM_Moscow_2.sql_command_delete_staff(call.data.replace("Удалить ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


# ======================================================================================================================

def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(delete_staff_bish, commands=['Удал_Сотруд_Bishkek'])
    dp.register_message_handler(delete_staff_osh, commands=['Удал_Сотруд_Osh'])
    dp.register_message_handler(delete_staff_Mescow_1, commands=['Удал_Сотруд_Moscow_1'])
    dp.register_message_handler(delete_staff_Mescow_2, commands=['Удал_Сотруд_Moscow_2'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("Удалить "))
