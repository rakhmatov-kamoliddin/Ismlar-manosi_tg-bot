from aiogram.dispatcher.filters.state import State, StatesGroup

class Reklama(StatesGroup):
    reklama = State()

class Post(StatesGroup):
    post_content = State()

class YorN(StatesGroup):
    yorn = State()