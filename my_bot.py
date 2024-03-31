from aiogram import Bot, Dispatcher, executor, types
import os
import  logging, warnings
from dotenv import load_dotenv

import os
import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
API_TOKEN = os.getenv("Telegram_Token")
logging.basicConfig(level=logging.INFO)

#Initialize_bot
bot = Bot(token=API_TOKEN)
dp  = Dispatcher(bot)
