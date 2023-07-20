import logging
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.message import ContentType
from aiogram.utils import executor

TOKEN = '5990812777:AAGSAKc8FoA-hU45R79hDQ1_05BWdOxF3xw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # chat_id = message.from_user.id


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1. Посмотреть селфи", "2. Посмотреть фото из школы", "3. Рассказ о моем увлечении", "4. Получить войс"]
    keyboard.add(*buttons)
    await message.answer("""<b>Привет! В этом боте ты можешь пользоваться такими функциями:</b>
    
        1) Кнопка 'Посмотреть селфи' для того чтобы увидеть мое фото
        2) Кнопка 'Посмотреть фото из школы' для того чтобы увидеть мое школьное фото
        3) Кнопка 'Рассказ о моем увлечении' для того чтобы узнать о моих увлечениях
        4) Кнопка 'Получить войс' где ты увидишь 4 пункта и можешь послшать голосвые на интересне темы
        5) Команда '/github' где ты увидишь исходный код данного бота
        6) <s>Посхалка</s> <tg-spoiler>Команда '/nextstep' где можно узнать о дальнейших действиях</tg-spoiler>""", reply_markup=keyboard, parse_mode=ParseMode.HTML)





@dp.message_handler(commands=['github'])
async def get_github_link(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # github_link = 'https://praktikum.notion.site/kids-ai-465035eb1e3c4409ac05e38a2beb41be'
    await message.reply(f'Вот ссылка на GitHub: <a href="https://github.com/dkimperia/Bot_forYaTeam">ТЫК</a>', reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message_handler(commands=['nextstep'])
async def send_next_step_info(message: types.Message):
    await message.answer("Дальнейшие шаги: ...")  # Здесь инфа о следующих шагах


# Обработчик кнопок
@dp.message_handler(content_types=ContentType.TEXT)
async def handle_buttons(message: types.Message):
    if message.text == "1. Посмотреть селфи":
        await message.answer_photo(photo=open('last.jpg', 'rb'))

    elif message.text == "2. Посмотреть фото из школы":
        await message.answer_photo(photo=open('school.jpg', 'rb'))

    elif message.text == "3. Рассказ о моем увлечении":
        post = """Мое главное увлечение - это программирование. Я обожаю создавать полезные и интересные проекты,
                а также изучать новые технологии. Программирование - это для меня не только профессия, но и хобби,
                которому я уделяю много времени и энергии. Через программирование я стараюсь внести свой вклад
                в развитие технологий и делать мир немного лучше!"""
        await message.answer(post, parse_mode=ParseMode.MARKDOWN)

    elif message.text == "4. Получить войс":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["GPT", "SQL и NoSQL", "История первой любви", "Отмена"]
        keyboard.add(*buttons)
        await message.answer("Выберите войс:", reply_markup=keyboard)

    elif message.text == "GPT":
        await message.answer_voice(voice=open('gpt.ogg', 'rb'))

    elif message.text == "SQL и NoSQL":
        await message.answer_voice(voice=open('sql.ogg', 'rb'))

    elif message.text == "История первой любви":
        await message.answer_voice(voice=open('love.ogg', 'rb'))

    elif message.text == "Отмена":
        await message.answer("Отменено.", reply_markup=types.ReplyKeyboardRemove())




if __name__ == '__main__':
    print('bot running')
    executor.start_polling(dp, skip_updates=False)
