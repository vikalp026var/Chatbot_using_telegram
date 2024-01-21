import logging
from aiogram import Bot,Dispatcher,Router,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
# print(API_TOKEN)
logging.basicConfig(level=logging.INFO)

#Initialise bot and dispatcher 
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message(CommandStart())
async def command_start_handler(message:Message)->None:
     await message.answer(f"Hello,{hbold(message.from_user.full_name)}")



