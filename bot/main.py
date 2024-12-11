from aiogram import (
    types,
    Bot,
    Dispatcher,
) 
from aiogram.filters.command import Command
import asyncio

from config import *

bot = Bot(api_key)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Начнем, пожалуй!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())