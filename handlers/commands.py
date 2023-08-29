# =================================================================================================================
from aiogram import types, Dispatcher
from config import bot
from keyboards.buttons import data_recording_markup, products_pull_data_markup
from keyboards.buttons import (get_bishkek_markup, get_branches_osh_markup, get_branches_moscow_1_markup,
                               get_branches_moscow_2_markup, start_markup, products_markup, staff_markup, get_staff_markup)


# =================================================================================================================

async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                 "Этот бот для управления бизнесом!", reply_markup=start_markup)


async def info(message: types.Message):
    await message.answer(f"Какие команды есть в этом боте:\n\n"
                         f"=====Записи в базу=====\n"
                         f"/fill_products - для контроля товаров(приход и уход)\n"
                         f"/fill_booking - брони\n"
                         f"/reg_staff - регистрация сотрудников и их график\n"
                         f"/control - для контроля сотрудников(чтобы посмотреть кто опоздал)\n\n"
                         f"=====Взятие из базы=====\n"
                         f"/get_products - выдает товары (по 5)\n"
                         f"/get_bookings - выдает брони (по 5)\n"
                         f"/get_staff - выдает сотрудников(по 5)\n",
                         reply_markup=start_markup)

async def products_button(message: types.Message):
    await message.answer('Вы зашли в товары!', reply_markup=products_markup)

async def staff_button(message: types.Message):
    await message.answer('Вы зашли к сотрудникам!', reply_markup=staff_markup)


async def get_staff_buttons(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇️", reply_markup=get_staff_markup)

# =================================================================================================================

async def back(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=start_markup)


async def data_recording(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=data_recording_markup)


async def pull_data(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=products_pull_data_markup)



async def pull_staff(message: types.Message):
    pass



#=================================================================================================================
async def get_bishkek(message: types.Message):
    await message.answer(f"Вы выбрали Бишкек!", reply_markup=get_bishkek_markup)


async def get_osh(message: types.Message):
    await message.answer(f"Вы выбрали Ош!", reply_markup=get_branches_osh_markup)


async def get_moscow_1(message: types.Message):
    await message.answer(f"Вы выбрали Москву! (Первый филиал)", reply_markup=get_branches_moscow_1_markup)


async def get_moscow_2(message: types.Message):
    await message.answer(f"Вы выбрали Москву! (Второй филиал)", reply_markup=get_branches_moscow_2_markup)


# =================================================================================================================

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(data_recording, commands=['запись_данных'])
    dp.register_message_handler(pull_data, commands=['вывести_данные'])

    dp.register_message_handler(products_button, commands=['Товары'])
    dp.register_message_handler(staff_button, commands=['Сотрудники'])

    dp.register_message_handler(get_bishkek, commands=['Бишкек'])
    dp.register_message_handler(get_osh, commands=['Ош'])
    dp.register_message_handler(get_moscow_1, commands=['Москва_1'])
    dp.register_message_handler(get_moscow_2, commands=['Москва_2'])

    dp.register_message_handler(back, commands=['<-назад'])
