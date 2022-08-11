from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Text
from keyboards.default import defaultkeyboard
from utils.ismlar import ismlar_manosi
from states.my_state import Form
from aiogram.dispatcher import FSMContext



# Echo bot
@dp.message_handler(Text('Ismlar manosi'))
async def bot_echo(message: types.Message,state=FSMContext):
    await message.answer("Ismingizni kiriting !",reply_markup=defaultkeyboard.defaults_buttons)
    # await Form.ism.set()
    # @dp.message_handler(state=Form.ism)
    @dp.message_handler()
    async def bot_ech(message: types.Message):
        
        data = ismlar_manosi(message.text)
        
        for content in data:
            name=content['name']
            name_mean=content['name_mean']
            await message.reply(
            f"<a href='https://i.ibb.co/HLSd9N9/ism.jpg'>.</a><b>{name}</b>\nManosi : <b><i>{name_mean}</i></b>"
            )
        # await state.finish()