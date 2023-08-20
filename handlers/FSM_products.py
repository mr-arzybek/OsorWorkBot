from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards.buttons import cancel_markup, basic_markup, submit_markup, city_markup
from db.orm import sql_product_insert

class fsm_products(StatesGroup):
    name = State()         # Название товара
    date_coming = State()  # Дата где будут записаны приход
    date_care = State()    # Дата где будут записаны уходы
    city = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_products.name.set()
    await message.answer('Название товара?', reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await fsm_products.next()
    await message.answer('Дата прихода?')


async def load_date_coming(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_coming'] = message.text
    await fsm_products.next()
    await message.answer('Дата ухода?')


async def load_date_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_care'] = message.text
    await fsm_products.next()
    await message.answer('Город?\n'
                         'Если Москва, то указать какой филиал!',
                         reply_markup=city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        await message.answer(f"Данные: \n"
                             f"Название: {data['name']}\n"
                             f"Дата прихода: {data['date_coming']}\n"
                             f"Дата ухода: {data['date_care']}\n"
                             f"Город: {data['city']}")

    await fsm_products.next()
    await message.answer('Всё верно?', reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_product_insert(state)   # запись в базу
        await message.answer('Готово!', reply_markup=basic_markup)
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено', reply_markup=basic_markup)
        await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=basic_markup)


def register_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['fill_products'])
    dp.register_message_handler(load_name, state=fsm_products.name)
    dp.register_message_handler(load_date_coming, state=fsm_products.date_coming)
    dp.register_message_handler(load_date_care, state=fsm_products.date_care)
    dp.register_message_handler(load_city, state=fsm_products.city)
    dp.register_message_handler(load_submit, state=fsm_products.submit)
