# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboards.buttons import cancel_markup, staff_markup, submit_markup, city_markup

from db.db_bish.ORM_Bish import bish_sql_staff_insert
from db.db_osh.ORM_Osh import osh_sql_staff_insert
from db.db_moscow_1.ORM_Moscow_1 import moscow_1_sql_staff_insert
from db.db_moscow_2.ORM_Moscow_2 import moscow_2_sql_staff_insert

from datetime import datetime


# =======================================================================================================================

class fsm_reg_staff(StatesGroup):
    full_name_staff = State()
    phone_staff = State()
    info_staff = State()
    schedule_staff = State()
    city_staff = State()
    photo_staff = State()
    submit = State()


async def fsm_start(message: types.Message):
    await fsm_reg_staff.full_name_staff.set()
    await message.answer('Имя сотрудника?', reply_markup=cancel_markup)


async def load_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await fsm_reg_staff.next()
    await message.answer('Номер телефона сотрудника? \n'
                         '+996 или +7')


async def load_phone_staff(message: types.Message, state: FSMContext):
    if message.text.find("+"):
        await message.answer('Начните с +')
    else:
        async with state.proxy() as data:
            data['phone'] = message.text
        await fsm_reg_staff.next()
        await message.answer("Информация о сотруднике !?")


async def load_info_staff(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
    await fsm_reg_staff.next()
    await message.answer('График сотрудника?\n'
                         '(Во сколько начинается его рабочий день)\n'
                         'Образец: 9:00 - 17:00')


async def load_schedule(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['schedule'] = message.text
    await fsm_reg_staff.next()
    await message.answer('Сотрудник какого филиала?\n'
                         'Если Москва, то указать какой филиал!\n'
                         'Выберите снизу по кнопкам, какой город!',
                         reply_markup=city_markup)


async def load_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await fsm_reg_staff.next()
    await message.answer('Фотография сотрудника !?')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        data['date'] = datetime.now()
        await message.answer_photo(
            data["photo"],
            caption=f'Данные: \n'
                    f'ФИО: {data["full_name"]}\n'
                    f'Номер телефона: {data["phone"]}\n'
                    f'Информация о сотруднике: {data["info"]}'
                    f'График: {data["schedule"]}\n'
                    f'Город: {data["city"]}')
    await fsm_reg_staff.next()
    await message.answer("Все верно?", reply_markup=submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            if data['city'] == 'Бишкек':
                await bish_sql_staff_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'ОШ':
                await osh_sql_staff_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'Москва 1-филиал':
                await moscow_1_sql_staff_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

            elif data['city'] == 'Москва 2-филиал':
                await moscow_2_sql_staff_insert(state)
                await message.answer('Готово!', reply_markup=staff_markup)
                await state.finish()

        elif message.text.lower() == 'нет':
            await message.answer('Хорошо, отменено', reply_markup=staff_markup)
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=staff_markup)


# =======================================================================================================================

def register_staff(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['регистрация_сотрудников'])
    dp.register_message_handler(load_full_name, state=fsm_reg_staff.full_name_staff)
    dp.register_message_handler(load_phone_staff, state=fsm_reg_staff.phone_staff)
    dp.register_message_handler(load_info_staff, state=fsm_reg_staff.info_staff)
    dp.register_message_handler(load_schedule, state=fsm_reg_staff.schedule_staff)
    dp.register_message_handler(load_city, state=fsm_reg_staff.city_staff)
    dp.register_message_handler(load_photo, state=fsm_reg_staff.photo_staff, content_types=['photo'])

    dp.register_message_handler(load_submit, state=fsm_reg_staff.submit)
