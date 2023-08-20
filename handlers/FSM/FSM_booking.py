from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards.buttons import cancel_markup, data_recording_markup, submit_markup, city_markup
from db.orm import sql_booking_insert


class fsm_booking(StatesGroup):
    name_product = State()  # Название товара
    start_of_armor = State()  # Дата началы брони
    end_of_armor = State()  # Дата конца брони
    name_customer = State()
    phone = State()
    name_salesman = State()
    price = State()
    discount = State()
    city = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_booking.name_product.set()
    await message.answer('Название товара?', reply_markup=cancel_markup)


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text
    await fsm_booking.next()
    await message.answer('Начало брони?')


async def load_start_of_armor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['start_of_armor'] = message.text
    await fsm_booking.next()
    await message.answer('Конец брони?')


async def load_end_of_armor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['end_of_armor'] = message.text
    await fsm_booking.next()
    await message.answer('Имя заказчика?')


async def load_name_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await fsm_booking.next()
    await message.answer('Номер телефона заказчика? \n'
                         '+996 или +7')

async def load_phone_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_customer'] = message.text
    await fsm_booking.next()
    await message.answer('Имя продавца?')



async def load_name_salesman(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await fsm_booking.next()
    await message.answer('Цена?\n'
                         '(Без скидки)')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await fsm_booking.next()
    await message.answer('Скидка?'
                         '(Сумму скидки!)')


async def load_discount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['discount'] = message.text
        data['calculation'] = int(data['price']) - int(data['discount'])

    await fsm_booking.next()
    await message.answer('Город?\n'
                         'Если Москва, то указать какой филиал!',
                         reply_markup=city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        await message.answer(f"Данные: \n"
                             f"Название товара: {data['name_product']}\n"
                             f"Начало брони: {data['start_of_armor']}\n"
                             f"Конец брони: {data['end_of_armor']}\n"
                             f"Заказчик: {data['name_customer']}\n"
                             f"Номер телефона заказчика: {data['phone_customer']}\n"
                             f"Продацев: {data['name_salesman']}\n"
                             f"Цена: {data['price']}\n"
                             f"Скидка: {data['discount']}\n"
                             f"Итоговая цена: {data['calculation']}\n"
                             f"Город: {data['city']}")

    await fsm_booking.next()
    await message.answer('Всё верно?', reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_booking_insert(state)  # запись в базу
        await message.answer('Готово!', reply_markup=data_recording_markup)
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено', reply_markup=data_recording_markup)
        await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=data_recording_markup)


def register_booking(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['fill_booking'])
    dp.register_message_handler(load_name_product, state=fsm_booking.name_product)
    dp.register_message_handler(load_start_of_armor, state=fsm_booking.start_of_armor)
    dp.register_message_handler(load_end_of_armor, state=fsm_booking.end_of_armor)
    dp.register_message_handler(load_name_customer, state=fsm_booking.name_customer)
    dp.register_message_handler(load_phone_customer, state=fsm_booking.phone)
    dp.register_message_handler(load_name_salesman, state=fsm_booking.name_salesman)
    dp.register_message_handler(load_price, state=fsm_booking.price)
    dp.register_message_handler(load_discount, state=fsm_booking.discount)
    dp.register_message_handler(load_city, state=fsm_booking.city)
    dp.register_message_handler(load_submit, state=fsm_booking.submit)
