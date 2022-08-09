from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle,InlineQueryResultPhoto,InputMediaPhoto,InputMediaVideo,InlineQueryResultVideo,InlineQueryResultAudio,InputMediaAudio, InputMessageContent
from loader import dp
from utils.ismlar import ismlar_manosi
import hashlib

   
   
# @dp.inline_handler()
# async def inline_echo(inline_query: InlineQuery):
#     text = inline_query.query or 'weather'
#     input_content = InputTextMessageContent(text)
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     item = InlineQueryResultArticle(
#         id=result_id,
#         title=f'Result {text!r}',
#         input_message_content=input_content,
#         description='Ismingizni kiriting',
#         thumb_url = 'https://ismlar.com/assets/front/img/apple-touch-icon.png',
#         url = 'https://t.me/renove_bg_bot'

#     )



@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'Ismingizni kiriting'
    result = ismlar_manosi(text)
    
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    items=[]
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'{text!r}',
        input_message_content=input_content,
        description='Ismingizni kiriting',
        thumb_url = "https://i.ibb.co/HLSd9N9/ism.jpg",
        url = 'https://t.me/renove_bg_bot'

    )
    if result:
        # link_text = f"<a href=\"{re['image']}\">.</a>"
        # text=link_text+f"{re['title']}\n{re['price']}"
        for i,re in enumerate(result):
            item = InlineQueryResultArticle(
            id=i,
            # photo_url = re['image'],
            title = re['name'],
            description=re['name_mean'],
            thumb_url = 'https://i.ibb.co/HLSd9N9/ism.jpg',
            input_message_content=InputTextMessageContent(f"<a href='https://i.ibb.co/HLSd9N9/ism.jpg'>.</a>Siz qidirgan ism:<b>{re['name']}</b>\nManosi:<b>{re['name_mean']}</b>"),
            )
            # print(my_url[i])
            items.append(item)
    
    if items:
        await inline_query.answer(results=items, cache_time=1)
    await inline_query.answer(results=[item], cache_time=1)
        






# import telebot
# from selenium import webdriver
# from time import sleep
# from selenium import webdriver
 
 
# driver = webdriver.Chrome('/path/to/chromedriver')
 
# bot = telebot.TeleBot('5342381989:AAG2DXXkU1OvoWFyRuhMF1clrDoJDSXhuFc')
 
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Привет")
 
# @bot.message_handler(commands=['search_videos'])
# def search_videos(message):
#     msg = bot.send_message(message.chat.id, "Введите текст, который вы хотите найти в YouTube")
#     bot.register_next_step_handler(msg, search)
 
# @bot.message_handler(commands=['search_channel'])
# def search_channel(message):
#     msg = bot.send_message(message.chat.id, "Введите YouTube канал")
#     bot.register_next_step_handler(msg, search_from_channel)
 
 
 
# @bot.message_handler(content_types=['text'])
# def text(message):
#     bot.send_message(message.chat.id, "Ты что-то хотел?")
 
# def search_from_channel(message):
#     bot.send_message(message.chat.id, "Начинаю поиск")
#     driver.get(message.text + "/videos")
#     videos = driver.find_elements_by_id("video-title")
#     for i in range(len(videos)):
#         bot.send_message(message.chat.id, videos[i].get_attribute('href'))
#         if i == 10:
#             break
 
# def search(message):
#     bot.send_message(message.chat.id, "Начинаю поиск")
#     video_href = "https://www.youtube.com/results?search_query=" + message.text
#     driver.get(video_href)
#     sleep(2)
#     videos = driver.find_elements_by_id("video-title")
#     for i in range(len(videos)):
#         bot.send_message(message.chat.id, videos[i].get_attribute('href'))
#         if i == 10:
#             break
 
 
# bot.polling()