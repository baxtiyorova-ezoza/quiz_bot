import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


main_quiz_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Matematika"),
              KeyboardButton(text="J/t"),
        ],
        [
            KeyboardButton(text="Fizika"),
        ],
    ],
    resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Victorina_bot.",reply_markup=main_quiz_keyboard  )


    
@dp.message_handler(text = "s")
async def send_welcome(message: types.Message):
    await message.answer_poll(
        question="Kim yaxshi",
        options=["Olim", "hakim", "Tohir", "Eldor"],
        is_anonymous=False
    )
    await asyncio.sleep(3)

    await message.answer_poll(
        question="Kim yaxshi",
        options=["Olim", "hakim", "Tohir", "Eldor"],
        is_anonymous=False,
        allows_multiple_answers=True
    )
    await asyncio.sleep(3)

    await message.answer_poll(
        question="Kim yaxshi",
        options=["Olim", "hakim", "Tohir", "Eldor"],
        is_anonymous=False,
        correct_option_id=3,
        type="quiz"
    )

# 1savol
@dp.message_handler(text = "Matematika")
async def send_welcome(message: types.Message):
    await message.answer_poll(
        question="9*8",
        options=["1", "64", "72"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

# 2savol
    await message.answer_poll(
        question="210*540",
        options=["8765", "113400", "112347"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )

    await asyncio.sleep(3)

    await message.answer_poll(
        question="670/5",
        options=["87", "134", "112"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )

@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
