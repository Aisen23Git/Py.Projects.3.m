import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import os
import random
from aiogram.types import FSInputFile
load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    name = message.from_user.first_name
    surname = message.from_user.first_name
    await message.answer(
        f"Привет, {name}" + " {surname}"
    )


@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    files = os.listdir('/home/admin/VSCODE-projects(3m)/images')
    random1 = random.choice(files)
    photo=FSInputFile(random1)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
    )

@dp.message(Command("myinfo"))
async def info_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'id : {message.from_user.id}\n'
             f'name : {message.from_user.first_name}\n'
    )





async def main():
    # запускаем бот
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())