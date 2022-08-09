from distutils.cmd import Command
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Text,Command
from keyboards.inline import OurInlineKeyboard
from states.RegistrationState import Form
from loader import dp
from aiogram.dispatcher import FSMContext

@dp.message_handler(Text("More..."))
async def bot_start(message: types.Message):
    await message.answer(f"Adminga murojat qilish!",reply_markup=OurInlineKeyboard.Courses)
    
@dp.callback_query_handler(text=('admin'))
async def online_course(call: types.CallbackQuery):
    await Form.admin.set()
    await call.message.answer(f"🧑‍💻 Adminga botdagi nosozliklar, takliflar va boshqa narsalar haqida yozishingiz mumkin.")
    call.message.delete()
    
@dp.message_handler(state=Form.admin)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.finish()
    await dp.bot.send_message(1282301807, f"Foydalanuvchi sizga murojat qildi.\nIsmi:{message.from_user.full_name}\nMurojat:\t{message.text}")
    
    
    
@dp.message_handler(Command('developer'))
async def online_course(message: types.Message):
    await message.answer('🇺🇿Dasturchi: @rakhmat0v_2007')
    
    
@dp.message_handler(text=('/admin'))
async def online_course(message: types.Message):
    await Form.admin.set()
    await message.answer(f"🧑‍💻 Adminga botdagi nosozliklar, takliflar va boshqa narsalar haqida yozishingiz mumkin.")
    message.delete()
    
@dp.message_handler(state=Form.admin)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.finish()
    await dp.bot.send_message(1282301807, f"Foydalanuvchi sizga murojat qildi.\nIsmi:{message.from_user.full_name}\nMurojat:\t{message.text}")
    
