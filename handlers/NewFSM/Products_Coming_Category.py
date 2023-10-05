from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import buttons
from aiogram.dispatcher.filters import Text

cities = ['Бишкек', 'ОШ', 'Москва 1-филиал', 'Москва 1-филиал']


class AllProductsForCategoryFSM(StatesGroup):
    city = State()
    category = State()


async def fsm_start(message: types.Message):
    await AllProductsForCategoryFSM.city.set()
    await message.answer('Филиал? ⬇', reply_markup=buttons.city_markup)


async def load_city(message: types.Message):
    if message.text in cities:
        await AllProductsForCategoryFSM.next()
        await message.answer('Категория?', reply_markup=buttons.CategoryButtons)  # Добавить кнопку с категориями
    else:
        await message.answer('Вы ввели не тот филиал!')


async def load_category(state: FSMContext):
    await state.finish()


async def cancel_reg_category(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=buttons.start_admins_markup)



def register_fsm_comitCategory(dp: Dispatcher):
    dp.register_message_handler(cancel_reg_category, Text(equals='Отмена!', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['Пришедшие_товары'])

    dp.register_message_handler(load_city, state=AllProductsForCategoryFSM.city)
    dp.register_message_handler(load_category, state=AllProductsForCategoryFSM.category)
