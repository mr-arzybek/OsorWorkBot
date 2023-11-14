# from aiogram import Dispatcher, types
#
# from db.db_main.ORM_Bish import cursor_bish
# from db.db_osh.ORM_Osh import cursor_osh
# from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
# from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2
# from config import Director
#
#
# async def control_week_being_late_bish(message: types.Message):
#         cursor_bish.execute("SELECT * FROM being_late WHERE creation_time >= DATE('now', '-7 days')")
#         data = cursor_bish.fetchall()
#
#         for time in data:
#                 if message.from_user.id in Director:
#                         await message.answer(f'Данные: \n'
#                                              f'ФИО: {time[1]}\n'
#                                              f'Дата: {time[2]}\n'
#                                              f'Время прибытия: {time[3]}\n'
#                                              f'Город: {time[4]}')
#                 else:
#                         await message.answer('Только директор может просматривать!!')
#
#
# def register_week(dp: Dispatcher):
#     dp.register_message_handler(control_week_being_late_bish, commands=['График_за_неделю!'])