import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(1282301807, f"Bot ishga tushdi{admin}")

        except Exception as err:
            logging.exception(err)
