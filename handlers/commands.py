from aiogram import types, Dispatcher
from config import bot


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                 "Этот бот для управления бизнесом!")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
