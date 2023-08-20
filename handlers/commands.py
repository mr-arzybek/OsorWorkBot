from aiogram import types, Dispatcher
from config import bot
from keyboards.buttons import basic_markup, data_recording_markup, pull_data_markup


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                 "Этот бот для управления бизнесом!", reply_markup=basic_markup)


async def info(message: types.Message):
    await message.answer(f"Какие команды есть в этом боте:\n\n"
                         f"=====Записи в базу=====\n"
                         f"/fill_products - для контроля товаров(приход и уход)\n"
                         f"/fill_booking - брони\n"
                         f"/reg_staff - регистрация сотрудников и их график\n"
                         f"/control - для контроля сотрудников(чтобы посмотреть кто опоздал)\n\n"
                         f"=====Взятие из базы=====\n",
                         reply_markup=basic_markup)


async def back(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=basic_markup)


async def data_recording(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=data_recording_markup)


async def pull_data(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=pull_data_markup)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(data_recording, commands=['data_rec'])
    dp.register_message_handler(pull_data, commands=['pull_data'])
    dp.register_message_handler(back, commands=['<-back'])
