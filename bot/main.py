from aiogram import (
    types,
    Bot,
    Dispatcher,
) 
from aiogram.filters.command import Command
import asyncio
import aiohttp

from config import *

bot = Bot(api_key)
dp = Dispatcher()

url = "http://127.0.0.1:8000/generate_text"

async def post_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            return await response.json()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Начнем, пожалуй!")
 
@dp.message()
async def answer(message: types.Message):
    data = {
        "prompt": message.text
    }
    answer = asyncio.create_task(post_request, data)
    response_json = await answer
    answer_text = response_json.get("text")
    await message.reply(answer_text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())