# =================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins
from db.db_bish.ORM_Bish import cursor_bish
from keyboards import buttons


# =================================================================================================================

async def start(message: types.Message):
    if message.from_user.id in Admins:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.start_admins_markup)
    else:
        await bot.send_message(message.from_user.id, "Добро пожаловать в OSOR!\n"
                                                     "Этот бот для управления бизнесом!",
                               reply_markup=buttons.staff_markup)


async def info(message: types.Message):
    if message.from_user.id in Admins:
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
                             reply_markup=buttons.start_admins_markup)
    else:
        await message.answer(f"Какие команды есть в этом боте:\n\n"
                             f"=====Записи в базу=====\n"
                             f"/fill_products - для контроля товаров(приход и уход)\n"
                             f"/fill_booking - брони\n"
                             f"/reg_staff - регистрация сотрудников и их график\n"
                             f"/control - для контроля сотрудников(чтобы посмотреть кто опоздал)",
                             reply_markup=buttons.staff_markup)


async def products_button(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_admins_markup)
    else:
        await message.answer('Вы зашли в товары!', reply_markup=buttons.products_staff_markup)


"""Только для Админов"""


async def finance_button(message: types.Message):
    await message.answer('Вы зашли в финансы!', reply_markup=buttons.finance_markup)


async def pull_data_staff(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇️", reply_markup=buttons.staff_pull_data_markup)


async def pull_data(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=buttons.products_pull_data_markup)


async def get_bishkek(message: types.Message):
    await message.answer(f"Вы выбрали Бишкек!", reply_markup=buttons.get_bishkek_markup)

async def get_osh(message: types.Message):
    await message.answer(f"Вы выбрали Ош!", reply_markup=buttons.get_branches_osh_markup)


async def get_moscow_1(message: types.Message):
    await message.answer(f"Вы выбрали Москву! (Первый филиал)", reply_markup=buttons.get_branches_moscow_1_markup)

async def get_moscow_2(message: types.Message):
    await message.answer(f"Вы выбрали Москву! (Второй филиал)", reply_markup=buttons.get_branches_moscow_2_markup)


# --------------------------------------------------

async def staff_button(message: types.Message):
    await message.answer('Вы зашли к сотрудникам!', reply_markup=buttons.staff_admins_markup)


async def get_staff_buttons(message: types.Message):
    await message.answer("Выберите снизу из кнопок ⬇️", reply_markup=buttons.data_recording_staff_markup)


# --------------------------------------------------

async def back_for_admins(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start_admins_markup)


"""----------"""


async def back_for_staff(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.staff_markup)


async def data_recording(message: types.Message):
    await message.answer('Выберите действие, из кнопок снизу!', reply_markup=buttons.data_recording_markup)

async def super_customer(message: types.Message):
    cursor_bish.execute("SELECT phone FROM booking")
    customers = cursor_bish.fetchall()

    results = []

    for customer in customers:
        phone = customer[0]
        cursor_bish.execute("SELECT SUM(total_price) FROM booking WHERE phone = ?", (phone,))
        total_prices = cursor_bish.fetchall()
        results.extend(total_prices)

    await message.answer(str(customers))
    await message.answer(str(results))



# =================================================================================================================

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(super_customer, commands=['super_customer'])

    dp.register_message_handler(info, commands=['Информация'])

    dp.register_message_handler(data_recording, commands=['запись_данных_товара'])
    dp.register_message_handler(pull_data, commands=['вывести_данные_товара'])

    dp.register_message_handler(get_staff_buttons, commands=['запись_данных_сотрудников'])
    dp.register_message_handler(pull_data_staff, commands=['вывести_данные_сотрудников'])

    dp.register_message_handler(products_button, commands=['Товары'])
    dp.register_message_handler(staff_button, commands=['Сотрудники'])
    dp.register_message_handler(finance_button, commands=['Финансы'])

    dp.register_message_handler(get_bishkek, commands=['Бишкек'])
    dp.register_message_handler(get_osh, commands=['Ош'])
    dp.register_message_handler(get_moscow_1, commands=['Москва_1'])
    dp.register_message_handler(get_moscow_2, commands=['Москва_2'])

    dp.register_message_handler(back_for_staff, commands=['<-назад'])
    dp.register_message_handler(back_for_admins, commands=['<назад'])
