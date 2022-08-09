# from aiogram import types
# from filters.AdminFilter import IsAdmin
# from filters.PrivateFilter import IsPrivate
# from loader import dp
# from data.config import CHANNELS
# import time


# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     while True:
#         time.sleep(5)
#         await message.answer(message.text)
#         text =message.text+'\n@uz_python'
#         await dp.bot.send_message(CHANNELS[0], text)