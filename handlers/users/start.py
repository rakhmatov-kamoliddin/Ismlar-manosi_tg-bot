from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards import default
from keyboards.default import defaultkeyboard
from keyboards.default.defaultkeyboard import defaults_buttons
from keyboards.inline import OurInlineKeyboard

from states.RegistrationState import Form
from loader import dp
from aiogram.dispatcher import FSMContext


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=defaultkeyboard.defaults_buttons)


import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!",reply_markup=defaultkeyboard.defaults_buttons)
    await message.answer('Menu:',reply_markup=OurInlineKeyboard.Course)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)



@dp.message_handler(Command('count'))
async def bot_start(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"Botda {count}-ta foydalanuvchi mavjud!")
