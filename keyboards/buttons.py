# ===========================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ===========================================================================
back_button = KeyboardButton('/<-назад')
# ===========================================================================
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)
finance_button = KeyboardButton("/Финансы")
products_button = KeyboardButton("/Товары")
staff_button = KeyboardButton("/Сотрудники")

start_markup.add(finance_button, products_button, staff_button)

# ===========================================================================


products_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

data_recording_button = KeyboardButton('/запись_данных')
pull_data_button = KeyboardButton('/вывести_данные')

products_markup.add(data_recording_button, pull_data_button, back_button)

# ===========================================================================

staff_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)


reg_staff_reg_button = KeyboardButton('/регистрация_сотрудников')
control_reg_button = KeyboardButton('/контроль_сотрудников')

staff_markup.add(reg_staff_reg_button, control_reg_button, back_button)

# ===========================================================================


# ===========================================================================
data_recording_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
products_reg_button = KeyboardButton('/запись_товаров')
bookings_reg_button = KeyboardButton('/записать_бронь')

data_recording_markup.add(products_reg_button, bookings_reg_button, back_button)
# ====================================================================================================================


# ====================================================================================================================
staff_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

staff_get_bishkek_button = KeyboardButton('/Сотрудники_Бишкек')
staff_get_osh_button = KeyboardButton('/Сотрудники_Ош')
staff_get_moscow_1_button = KeyboardButton('/Сотрудники_Москва_1')
staff_get_moscow_2_button = KeyboardButton('/Сотрудники_Москва_2')

staff_pull_data_markup.add(staff_get_bishkek_button, staff_get_osh_button, staff_get_moscow_1_button,
                           staff_get_moscow_2_button, back_button)

# ============================================

products_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

products_get_bishkek_button = KeyboardButton('/Бишкек')
products_get_osh_button = KeyboardButton('/Ош')
products_get_moscow_1_button = KeyboardButton('/Москва_1')
products_get_moscow_2_button = KeyboardButton('/Москва_2')

products_pull_data_markup.add(products_get_bishkek_button, products_get_osh_button, products_get_moscow_1_button,
                              products_get_moscow_2_button, back_button)


# ====================================================================================================================



# ====================================================================================================================
get_bishkek_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_bishkek_button = KeyboardButton("/Товары_Бишкек")
get_booking_bishkek_button = KeyboardButton("/Брони_Бишкек")
# get_reg_staff_bishkek_button = KeyboardButton('')


get_bishkek_markup.add(get_products_bishkek_button, get_booking_bishkek_button, back_button)

# ===========================================================================

get_branches_osh_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_osh_button = KeyboardButton("/Товары_Ош")
get_booking_osh_button = KeyboardButton("/Брони_Ош")
# get_reg_staff_osh_button = KeyboardButton("")


get_branches_osh_markup.add(get_products_osh_button, get_booking_osh_button, back_button)

# ===========================================================================

get_branches_moscow_1_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_moscow_1_button = KeyboardButton("/Товары_Москва_1")
get_booking_moscow_1_button = KeyboardButton("/Брони_Москва_1")
# get_reg_staff_moscow_1_button = KeyboardButton("")


get_branches_moscow_1_markup.add(get_products_moscow_1_button, get_booking_moscow_1_button, back_button)

# ===========================================================================

get_branches_moscow_2_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_moscow_2_button = KeyboardButton("/Товары_Москва_2")
get_booking_moscow_2_button = KeyboardButton("/Брони_Москва_2")
# get_reg_staff_moscow_2_button = KeyboardButton("/")


get_branches_moscow_2_markup.add(get_products_moscow_2_button, get_booking_moscow_2_button, back_button)

# ===========================================================================

get_staff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_staff_bishkek_button = KeyboardButton("/Сотрудники_Бишкек")
get_staff_osh_button = KeyboardButton("/Сотрудники_Ош")
get_staff_moscow_1_button = KeyboardButton("/Сотрудники_Москва_1")
get_staff_moscow_2_button = KeyboardButton("/Сотрудники_Москва_2")

get_staff_markup.add(get_staff_bishkek_button, get_staff_osh_button, get_staff_moscow_1_button,
                     get_staff_moscow_2_button)



staff_pull_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

pull_staff_bishkek = KeyboardButton("")
pull_staff_osh = KeyboardButton("")
pull_staff_moscow_1 = KeyboardButton("")
pull_staff_moscow_2 = KeyboardButton("")

staff_pull_markup.add(pull_staff_bishkek, pull_staff_bishkek, pull_staff_moscow_1, pull_staff_moscow_2)

# ======================================================================================================================



# ======================================================================================================================
cancel_button = KeyboardButton('Отмена')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('да'),
                                          KeyboardButton('нет'))

city_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2
                                  ).add(KeyboardButton('Бишкек'),
                                        KeyboardButton('ОШ'),
                                        KeyboardButton('Москва 1-филиал'),
                                        KeyboardButton('Москва 2-филиал'))
# ===========================================================================
