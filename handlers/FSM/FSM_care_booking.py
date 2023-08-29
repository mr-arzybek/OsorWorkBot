from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards import buttons

from db.db_bish.ORM_Bish import bish_sql_booking_insert
from db.db_osh.ORM_Osh import osh_sql_booking_insert
from db.db_moscow_1.ORM_Moscow_1 import moscow_1_sql_booking_insert
from db.db_moscow_2.ORM_Moscow_2 import moscow_2_sql_booking_insert
from datetime import datetime


class fsm_booking(StatesGroup):
    name_product = State()  # Название товара
    care_product = State()  # Дата конца брони
    care_name_customer = State()  # Имя заказчика
    care_phone = State()  # Номер телефона заказчика
    care_name_salesman = State()  # Имя продавца
    care_price = State()  # Цена
    care_discount = State()  # Скидка
    care_city = State()  # Итоговая цена
    care_photo_product = State()
    care_submit = State()


async def fsm_start_care(message: types.Message):
    await fsm_booking.name_product.set()
    await message.answer('Название товара?', reply_markup=buttons.cancel_markup)


async def load_name_product_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text
    await fsm_booking.next()
    await message.answer('Конец брони?\n'
                         'Образец: 12.09.23')


async def load_end_of_armor_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['end_of_armor'] = message.text
    await fsm_booking.next()
    await message.answer('Имя заказчика?')


async def load_name_customer_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await fsm_booking.next()
    await message.answer('Номер телефона заказчика? \n'
                         'Начать нужно через "+"')


async def load_phone_customer_care(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_customer'] = message.text
        await fsm_booking.next()
        await message.answer('Имя продавца?')


async def load_name_salesman_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await fsm_booking.next()
    await message.answer('Цена?\n'
                         '(Без скидки)')


async def load_price_care(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await fsm_booking.next()
        await message.answer('Скидка?\n'
                             '(Сумму скидки!)')
    else:
        await message.answer('Укажите цифрами!')


async def load_discount_care(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['discount'] = message.text
            data['calculation'] = int(data['price']) - int(data['discount'])

        await fsm_booking.next()
        await message.answer('Город?\n'
                             'Если Москва, то указать какой филиал!\n'
                             'Выберите снизу по кнопкам, какой город!',
                             reply_markup=buttons.city_markup)
    else:
        await message.answer('Укажите цифрами!')


async def load_city_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await fsm_booking.next()
    await message.answer('Фотография товара !?')


async def load_photo_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        a = data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные брони: \n"
                    f"Название товара: {data['name_product']}\n"
                    f"Конец брони: {data['end_of_armor']}\n"
                    f"Заказчик: {data['name_customer']}\n"
                    f"Номер телефона заказчика: {data['phone_customer']}\n"
                    f"Продацев: {data['name_salesman']}\n"
                    f"Цена: {data['price']}\n"
                    f"Скидка: {data['discount']}\n"
                    f"Итоговая цена: {data['calculation']}\n"
                    f"Город: {data['city']}")
        print(a)
    await fsm_booking.next()
    await message.answer("Все верно?", reply_markup=buttons.submit_markup)


async def load_submit_care(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                await bish_sql_booking_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'ОШ':
                await osh_sql_booking_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                await moscow_1_sql_booking_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                await moscow_2_sql_booking_insert(state)
                await message.answer('Готово!', reply_markup=buttons.data_recording_markup)
                await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=buttons.data_recording_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.data_recording_markup)


def register_care_booking(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start_care, commands=['записать_конец_брони'])

    dp.register_message_handler(load_name_product_care, state=fsm_booking.name_product)
    dp.register_message_handler(load_end_of_armor_care, state=fsm_booking.care_product)
    dp.register_message_handler(load_name_customer_care, state=fsm_booking.care_name_customer)
    dp.register_message_handler(load_phone_customer_care, state=fsm_booking.care_phone)
    dp.register_message_handler(load_name_salesman_care, state=fsm_booking.care_name_salesman)
    dp.register_message_handler(load_price_care, state=fsm_booking.care_price)
    dp.register_message_handler(load_discount_care, state=fsm_booking.care_discount)
    dp.register_message_handler(load_city_care, state=fsm_booking.care_city)
    dp.register_message_handler(load_photo_care, state=fsm_booking.care_photo_product, content_types=['photo'])
    dp.register_message_handler(load_submit_care, state=fsm_booking.care_submit)
