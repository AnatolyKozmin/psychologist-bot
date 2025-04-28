import asyncio 
import os 

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())