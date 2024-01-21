import logging
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
# print(API_TOKEN)
logging.basicConfig(level=logging.INFO)

#Initialise bot and dispatcher 
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message:types.Message)->None:
     await message.reply("Hi \nI am Echo Bot! \nPowered by aiogram.")

@dp.message_handler()
async def command_start_handler(message:types.Message)->None:
     await message.reply(message.text)

     

     
     
     
if __name__=="__main__":
     executor.start_polling(dp,skip_updates=True)
     
     
     
     




