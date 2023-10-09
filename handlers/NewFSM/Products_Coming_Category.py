from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import buttons
from aiogram.dispatcher.filters import Text
from db.sql_commands.utils import get_product_from_category
from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2

cities = ['Бишкек', 'ОШ', 'Москва 1-филиал', 'Москва 1-филиал']
categories = ["/Обувь", "/Нижнее_белье", "/Акссесуары", "/Верхняя_одежда", "/Штаны"]


class AllProductsForCategoryFSM(StatesGroup):
    city = State()
    category = State()


async def fsm_start(message: types.Message):
    await AllProductsForCategoryFSM.city.set()
    await message.answer('Филиал? ⬇', reply_markup=buttons.city_markup)


async def load_city(message: types.Message, state: FSMContext):
    if message.text in cities:
        async with state.proxy() as data_category:
            data_category['city'] = message.text
        await AllProductsForCategoryFSM.next()
        await message.answer('Категория?', reply_markup=buttons.CategoryButtons)  # Добавить кнопку с категориями

    else:
        await message.answer('Вы ввели не тот филиал!')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data_category:
        if 'city' in data_category:
            city = data_category['city']
            category = message.text.replace("/", "")

            if city == "Бишкек":
                products = get_product_from_category(cursor=cursor_bish, category=category, city=city)
            elif city == "ОШ":
                products = get_product_from_category(cursor=cursor_osh, category=category, city=city)
            elif city == "Москва 1-филиал":
                products = get_product_from_category(cursor=cursor_moscow_1, category=category, city=city)
            elif city == "Москва 2-филиал":
                products = get_product_from_category(cursor=cursor_moscow_2, category=category, city=city)

            for product in products:
                await message.answer_photo(photo=product[9], caption=f"Товар: {product[1]}\n"
                                                                     f"Информация о товаре: {product[2]}\n"
                                                                     f"Дата прихода: {product[3]}\n"
                                                                     f"Цена: {product[4]}\n"
                                                                     f"Город: {product[5]}\n"
                                                                     f"Категория: {product[6]}\n"
                                                                     f"Артикул: {product[7]}\n"
                                                                     f"Количество: {product[8]}\n")
        else:
            await message.answer("Филиал не выбран. Выберите филиал сначала.")


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
