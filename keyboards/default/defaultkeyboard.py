from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

defaults_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ismlar manosi'),
            # KeyboardButton(text='Location', request_location=True),
        ],
        [
            KeyboardButton(text='About'),
            KeyboardButton(text='More...'),
        ],
    ],
    resize_keyboard=True
)