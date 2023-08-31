# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards.buttons import cancel_markup, data_recording_markup, submit_markup, city_markup

from db.db_bish.ORM_Bish import bish_sql_product_coming_insert
from db.db_osh.ORM_Osh import osh_sql_product_insert
from db.db_moscow_1.ORM_Moscow_1 import moscow_1_sql_product_insert
from db.db_moscow_2.ORM_Moscow_2 import moscow_2_sql_product_insert
from datetime import datetime


# =======================================================================================================================

class fsm_products(StatesGroup):
    name = State()  # Название товара
    info_product = State()
    date_coming = State()  # Дата где будут записаны приход
    name_customer = State()
    phone = State()
    name_salesman = State()
    price = State()
    discount = State()
    city = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_products.name.set()
    await message.answer('Название товара?', reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await fsm_products.next()
    await message.answer('Информация о товаре!?')


async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
    await fsm_products.next()
    await message.answer('Дата прихода?')


async def load_date_coming(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_coming'] = message.text
    await fsm_products.next()
    await message.answer('Имя заказчика?')


async def load_name_customer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_customer'] = message.text
    await fsm_products.next()
    await message.answer('Номер телефона заказчика? \n'
                         '+996 или +7')


async def load_phone_customer(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone_customer'] = message.text
        await fsm_products.next()
        await message.answer('Имя продавца?')


async def load_name_salesman(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_salesman'] = message.text
    await fsm_products.next()
    await message.answer('Цена?')


async def load_price(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['price'] = message.text
        await fsm_products.next()
        await message.answer('Скидка?\n'
                             '(Сумму скидки!)')
    else:
        await message.answer('Укажите цифрами!')


async def load_discount(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['discount'] = message.text
            data['total_price'] = int(data['price']) - int(data['discount'])

        await fsm_products.next()
        await message.answer('Город?\n'
                             'Если Москва, то указать какой филиал!\n'
                             'Выберите снизу по кнопкам, какой город!',
                             reply_markup=city_markup)
    else:
        await message.answer('Укажите цифрами!')


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await fsm_products.next()
    await message.answer('Фотография товара?')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f"Данные брони: \n"
                    f"Название товара: {data['name']}\n"
                    f"Информация о товаре: {data['info']}\n"
                    f"Дата прихода товара: {data['date_coming']}\n"
                    f"Заказчик: {data['name_customer']}\n"
                    f"Номер телефона заказчика: {data['phone_customer']}\n"
                    f"Продацев: {data['name_salesman']}\n"
                    f"Цена: {data['price']}\n"
                    f"Скидка: {data['discount']}\n"
                    f"Итоговая цена: {data['total_price']}\n"
                    f"Город: {data['city']}")
    await fsm_products.next()
    await message.answer("Все верно?", reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                await bish_sql_product_coming_insert(state)
                await message.answer('Готово!', reply_markup=data_recording_markup)
                await state.finish()

            elif data['city'] == 'ОШ':
                await osh_sql_product_insert(state)
                await message.answer('Готово!', reply_markup=data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                await moscow_1_sql_product_insert(state)
                await message.answer('Готово!', reply_markup=data_recording_markup)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                await moscow_2_sql_product_insert(state)
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



# =======================================================================================================================

def register_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['запись_прихода_товаров'])

    dp.register_message_handler(load_name, state=fsm_products.name)
    dp.register_message_handler(load_info_product, state=fsm_products.info_product)
    dp.register_message_handler(load_date_coming, state=fsm_products.date_coming)
    dp.register_message_handler(load_name_customer, state=fsm_products.name_customer)
    dp.register_message_handler(load_phone_customer, state=fsm_products.phone)
    dp.register_message_handler(load_name_salesman, state=fsm_products.name_salesman)
    dp.register_message_handler(load_price, state=fsm_products.price)
    dp.register_message_handler(load_discount, state=fsm_products.discount)
    dp.register_message_handler(load_city, state=fsm_products.city)
    dp.register_message_handler(load_photo, state=fsm_products.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=fsm_products.submit)
