import logging

import aiogram

from production import API_TOKEN

from strings import get

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_start(message):
    await message.reply(get(message, "start"))

@dp.message_handler(commands=["bug"])
async def send_start(message):
    await message.reply(get(message, "bug"))

if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)
