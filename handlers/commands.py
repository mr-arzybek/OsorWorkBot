from aiogram import types, Dispatcher
from config import bot
from keyboards.buttons import basic_markup


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                 "Этот бот для управления бизнесом!", reply_markup=basic_markup)


async def info(message: types.Message):
    await message.answer(f"")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
