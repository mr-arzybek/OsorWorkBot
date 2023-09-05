

""""Кнопки нужно доработать!"""


# ===========================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ===========================================================================
back_admins_button = KeyboardButton('/<назад')
back_staff_button = KeyboardButton('/<-назад')
info_button = KeyboardButton("/Информация")
# ===========================================================================
start_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

regular_customers_button = KeyboardButton("/Постоянные_клиенты")
finance_button = KeyboardButton("/Финансы")
products_button = KeyboardButton("/Товары")
staff_button = KeyboardButton("/Сотрудники")

start_admins_markup.add(finance_button, products_button, staff_button, info_button, regular_customers_button)

staff_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)
products_button = KeyboardButton("/Товары")
staff_button = KeyboardButton("/Сотрудники")

staff_markup.add(products_button, staff_button, info_button)
# ===========================================================================
products_staff_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

data_recording_button = KeyboardButton('/запись_данных_товара')

products_staff_markup.add(data_recording_button, back_staff_button)

data_recording_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
products_comming_button = KeyboardButton('/запись_прихода_товаров')
products_care_button = KeyboardButton('/записать_уход_товара')
bookings_reg_button = KeyboardButton('/записать_бронь')

data_recording_markup.add(products_comming_button, products_care_button, bookings_reg_button, back_staff_button)

"""Для Админа"""
# ===========================================================================
# finance_markup = ReplyKeyboardMarkup(
#     resize_keyboard=True,
#     one_time_keyboard=False,
#     row_width=1
# )
# error_button = KeyboardButton('Здесь пока ничего нет')
# finance_markup.add(error_button, back_admins_button)

# ===========================================================================

products_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

data_recording_button = KeyboardButton('/запись_данных_товара')
pull_data_button = KeyboardButton('/вывести_данные_товара')

products_admins_markup.add(data_recording_button, pull_data_button, back_admins_button)

# ===========================================================================

staff_admins_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=1
)

reg_staff_reg_button = KeyboardButton('/запись_данных_сотрудников')
control_reg_button = KeyboardButton('/вывести_данные_сотрудников')

staff_admins_markup.add(reg_staff_reg_button, control_reg_button, back_admins_button)

# ===========================================================================
data_recording_staff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
reg_staff_reg_button = KeyboardButton('/регистрация_сотрудников')
control_reg_button = KeyboardButton('/контроль_сотрудников')

data_recording_staff_markup.add(reg_staff_reg_button, control_reg_button, back_admins_button)

# ===========================================================================

staff_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

staff_get_bishkek_button = KeyboardButton('/Сотрудники_Бишкек')
staff_get_osh_button = KeyboardButton('/Сотрудники_Ош')
staff_get_moscow_1_button = KeyboardButton('/Сотрудники_Москва_1')
staff_get_moscow_2_button = KeyboardButton('/Сотрудники_Москва_2')

staff_pull_data_markup.add(staff_get_bishkek_button, staff_get_osh_button, staff_get_moscow_1_button,
                           staff_get_moscow_2_button, back_admins_button)

# ====================================================================================================================

products_pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

products_get_bishkek_button = KeyboardButton('/Бишкек')
products_get_osh_button = KeyboardButton('/Ош')
products_get_moscow_1_button = KeyboardButton('/Москва_1')
products_get_moscow_2_button = KeyboardButton('/Москва_2')

products_pull_data_markup.add(products_get_bishkek_button, products_get_osh_button, products_get_moscow_1_button,
                              products_get_moscow_2_button, back_admins_button)

# ====================================================================================================================

get_bishkek_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_coming_bishkek_button = KeyboardButton("/Товары_Бишкек(Приход)")
get_products_care_bishkek_button = KeyboardButton("/Товары_Бишкек(Проданные)")
get_booking_bishkek_button = KeyboardButton("/Брони_Бишкек")

get_bishkek_markup.add(get_products_coming_bishkek_button, get_products_care_bishkek_button, get_booking_bishkek_button,
                       back_admins_button)

# ===========================================================================

get_branches_osh_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_coming_osh_button = KeyboardButton("/Товары_Ош(Приход)")
get_products_care_osh_button = KeyboardButton("/Товары_Ош(Проданные)")
get_booking_osh_button = KeyboardButton("/Брони_Ош")

get_branches_osh_markup.add(get_products_coming_osh_button, get_products_care_osh_button, get_booking_osh_button,
                            back_admins_button)

# ===========================================================================

get_branches_moscow_1_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_coming_moscow_1_button = KeyboardButton("/Товары_Москва_1(Приход)")
get_products_care_moscow_1_button = KeyboardButton("/Товары_Москва_1(Проданные)")
get_booking_moscow_1_button = KeyboardButton("/Брони_Москва_1")

get_branches_moscow_1_markup.add(get_products_coming_moscow_1_button, get_products_care_moscow_1_button,
                                 get_booking_moscow_1_button, back_admins_button)

# ===========================================================================

get_branches_moscow_2_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_products_coming_moscow_2_button = KeyboardButton("/Товары_Москва_2(Приход)")
get_products_care_moscow_2_button = KeyboardButton("/Товары_Москва_2(Проданные)")
get_booking_moscow_2_button = KeyboardButton("/Брони_Москва_2")

get_branches_moscow_2_markup.add(get_products_coming_moscow_2_button, get_products_care_moscow_2_button,
                                 get_booking_moscow_2_button, back_admins_button)

# ===========================================================================

get_staff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

get_staff_bishkek_button = KeyboardButton("/Сотрудники_Бишкек")
get_staff_osh_button = KeyboardButton("/Сотрудники_Ош")
get_staff_moscow_1_button = KeyboardButton("/Сотрудники_Москва_1")
get_staff_moscow_2_button = KeyboardButton("/Сотрудники_Москва_2")

get_staff_markup.add(get_staff_bishkek_button, get_staff_osh_button, get_staff_moscow_1_button,
                     get_staff_moscow_2_button, back_admins_button)

staff_pull_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

pull_staff_bishkek = KeyboardButton("")
pull_staff_osh = KeyboardButton("")
pull_staff_moscow_1 = KeyboardButton("")
pull_staff_moscow_2 = KeyboardButton("")

staff_pull_markup.add(pull_staff_bishkek, pull_staff_bishkek, pull_staff_moscow_1, pull_staff_moscow_2,
                      back_admins_button)

# ======================================================================================================================

""" Кнопки, которые будут внутри кнопки 'Финансы' """
ButtonForFinance_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)
SalaryStaff_button = KeyboardButton("/Зарплаты")
RegularСustomer_button = KeyboardButton("/Постоянные_клиенты")
CheckoutControl_button = KeyboardButton("/Контроль_кассы")


ButtonForFinance_markup.add(SalaryStaff_button, RegularСustomer_button, CheckoutControl_button, back_admins_button)


SalaryStaff_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

salary_staff_bishkek = KeyboardButton("/ЗП_Бишкек")
salary_staff_osh = KeyboardButton("/ЗП_Ош")
salary_staff_moscow_1 = KeyboardButton("/ЗП_Москва_1")
salary_staff_moscow_2 = KeyboardButton("/ЗП_Москва_2")

SalaryStaff_markup.add(salary_staff_bishkek, salary_staff_osh, salary_staff_moscow_1, salary_staff_moscow_2, back_admins_button)




# ==============================

RegularСustomer_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)

RegularCustomer_bishkek = KeyboardButton("/Клиенты_Бишкек")
RegularCustomer_osh = KeyboardButton("/Клиенты_Ош")
RegularCustomer_moscow_1 = KeyboardButton("/Клиенты_Москва_1")
RegularCustomer_moscow_2 = KeyboardButton("/Клиенты_Москва_2")

RegularСustomer_markup.add(RegularCustomer_bishkek, RegularCustomer_osh, RegularCustomer_moscow_1,
                           RegularCustomer_moscow_2, back_admins_button)

# ==============================

"""-------------------------"""


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