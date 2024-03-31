from aiogram import Bot, Dispatcher, executor, types
import os
import  logging, warnings
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("Telegram_Token")
logging.basicConfig(level=logging.INFO)

#Initialize_bot
bot = Bot(token=API_TOKEN)
dp  = Dispatcher(bot)

@dp.message_handler(commands=["start","help"])
async def command_start_handler(message:types.Message):
    """
    This handler receives 
    """
    await message.reply("Hi!\n I am Echo Bot!\ Powered by Aiogram")
    
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo messege
    
    Args:
        messege (types.Message): [description]
    """
    await message.reply(message.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    