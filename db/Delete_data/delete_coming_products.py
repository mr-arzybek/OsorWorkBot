# # ======================================================================================================================
# from config import Director, bot
#
# from db.db_main import ORM_Bish
# from db.db_osh import ORM_Osh
# from db.db_moscow_1 import ORM_Moscow_1
# from db.db_moscow_2 import ORM_Moscow_2
#
# from aiogram import types, Dispatcher
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
#
# # ======================================================================================================================
#
# async def delete_products_coming_command_bish(message: types.Message):
#     if message.from_user.id in Director:
#         products = await ORM_Bish.sql_command_all_products_coming()
#         for product in products:
#             await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
#                                                                                  f"Информация о товаре: {product[2]}\n"
#                                                                                  f"Дата прихода: {product[3]}\n"
#                                                                                  f"Цена: {product[4]}]\n"
#                                                                                  f"Город: {product[5]}\n"
#                                                                                  f"Артикул: {product[6]}\n"
#                                                                                  f"количество: {product[7]}\n",
#                                  reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
#                                                                                               callback_data=f"delete {product[0]}")))
#
#     else:
#         await message.answer("You not Director!")
#
#
# async def delete_products_coming_command_Osh(message: types.Message):
#     if message.from_user.id in Director:
#         products = await ORM_Osh.sql_command_all_products_coming()
#         for product in products:
#             await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
#                                                                                  f"Информация о товаре: {product[2]}\n"
#                                                                                  f"Дата прихода: {product[3]}\n"
#                                                                                  f"Цена: {product[4]}]\n"
#                                                                                  f"Город: {product[5]}\n"
#                                                                                  f"Артикул: {product[6]}\n"
#                                                                                  f"количество: {product[7]}\n",
#                                  reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
#                                                                                               callback_data=f"delete {product[0]}")))
#
#     else:
#         await message.answer("You not Director!")
#
#
# async def delete_products_coming_command_Moscow_1(message: types.Message):
#     if message.from_user.id in Director:
#         products = await ORM_Moscow_1.sql_command_all_products_coming()
#         for product in products:
#             await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
#                                                                                  f"Информация о товаре: {product[2]}\n"
#                                                                                  f"Дата прихода: {product[3]}\n"
#                                                                                  f"Цена: {product[4]}]\n"
#                                                                                  f"Город: {product[5]}\n"
#                                                                                  f"Артикул: {product[6]}\n"
#                                                                                  f"количество: {product[7]}\n",
#                                  reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
#                                                                                               callback_data=f"delete {product[0]}")))
#
#     else:
#         await message.answer("You not Director!")
#
#
# async def delete_products_coming_command_Moscow_2(message: types.Message):
#     if message.from_user.id in Director:
#         products = await ORM_Moscow_2.sql_command_all_products_coming()
#         for product in products:
#             await bot.send_photo(message.from_user.id, photo=product[8], caption=f"Товар: {product[1]}\n"
#                                                                                  f"Информация о товаре: {product[2]}\n"
#                                                                                  f"Дата прихода: {product[3]}\n"
#                                                                                  f"Цена: {product[4]}]\n"
#                                                                                  f"Город: {product[5]}\n"
#                                                                                  f"Артикул: {product[6]}\n"
#                                                                                  f"количество: {product[7]}\n",
#                                  reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete {product[0]}",
#                                                                                               callback_data=f"delete {product[0]}")))
#
#     else:
#         await message.answer("You not Director!")
#
#
# # ======================================================================================================================
#
# async def complete_delete(call: types.CallbackQuery):
#     await ORM_Bish.sql_command_delete_coming(call.data.replace("Удалить ", ""))
#     await ORM_Osh.sql_command_delete_coming(call.data.replace("Удалить ", ""))
#     await ORM_Moscow_1.sql_command_delete_coming(call.data.replace("Удалить ", ""))
#     await ORM_Moscow_2.sql_command_delete_coming(call.data.replace("Удалить ", ""))
#     await call.answer(text="Удалено", show_alert=True)
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#
#
# # ======================================================================================================================
#
# def register_handler_admin(dp: Dispatcher):
#     dp.register_message_handler(delete_products_coming_command_bish, commands=['Удал_Прих_Bishkek'])
#     dp.register_message_handler(delete_products_coming_command_Osh, commands=['Удал_Прих_Osh'])
#     dp.register_message_handler(delete_products_coming_command_Moscow_1, commands=['Удал_Прих_Moscow_1'])
#     dp.register_message_handler(delete_products_coming_command_Moscow_2, commands=['Удал_Прих_Moscow_2'])
#     dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("Удалить "))
