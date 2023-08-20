# ===========================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# ===========================================================================
basic_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2
)

data_recording_button = KeyboardButton('/data_rec')
pull_data_button = KeyboardButton('/pull_data')
info_reg_button = KeyboardButton('/info')

basic_markup.add(data_recording_button, pull_data_button, info_reg_button)
# ===========================================================================
data_recording_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
products_reg_button = KeyboardButton('/fill_products')
bookings_reg_button = KeyboardButton('/fill_booking')
reg_staff_reg_button = KeyboardButton('/reg_staff')
control_reg_button = KeyboardButton('/control')
back_button = KeyboardButton('/<-back')

data_recording_markup.add(products_reg_button, bookings_reg_button, reg_staff_reg_button, control_reg_button,
                          back_button)
# ===========================================================================
pull_data_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=1)

# Здесь команды, которые будут вытаскивать данные из базы!
error_button = KeyboardButton('Здесь пока ничего нет!')
back_button = KeyboardButton('/<-back')

pull_data_markup.add(error_button, back_button)
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
