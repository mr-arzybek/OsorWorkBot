# ===========================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# ===========================================================================
basic_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

info_reg_button = KeyboardButton('/info')
products_reg_button = KeyboardButton('/fill_products')
bookings_reg_button = KeyboardButton('/fill_booking')
reg_staff_reg_button = KeyboardButton('/reg_staff')

basic_markup.add(info_reg_button, products_reg_button, bookings_reg_button, reg_staff_reg_button)

# ===========================================================================

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
