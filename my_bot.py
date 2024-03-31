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

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model="gemini-pro"
llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0,convert_system_message_to_human=True)

#Initialize_bot
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

class Reference:
    def _init_(self)  -> None:
        self.response = ""
        
reference = Reference()

def clear_past():
    reference.response = ""
    
@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")




@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """This handler receives messages with `/start` or  `/help `command

    Args:
        message (types.Message): _description_
    """
    await message.reply("Hi\nI am a Chat Bot! Created by Ram. How can i assist you?")




@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm a bot created by Ram! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)




@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    A handler to process the user's input and generate a response using ChatGoogleGenerativeAI.
    """

    print(f">>> USER: \n\t{message.text}")

     # Convert user message to a list within a dictionary (expected format)
    # prompt = {
    #     "chat_history": [
    #         {"role": "assistant", "content": "Welcome! How can I help you today?"},
    #         {"role": "user", "content": message.text}
    #     ]
    # }

    response = llm.invoke(message.text)
    reference.response = response.content

    print(f">>> GeminiPro: \n\t{reference.response}")
    #await bot.send_message(chat_id = message.text.chat.id, text=reference.response)
    await bot.send_message(chat_id = message.chat.id, text = reference.response)
    


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)