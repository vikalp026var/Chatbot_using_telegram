from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai
import sys 
from langchain.agents import AgentType
from langchain.agents import load_tools 
from langchain.agents import initialize_agent
from langchain.llms import OpenAI


class Reference:
    '''
    A class to store previous responses from the chatgpt API
    '''
    def __init__(self) -> None:
        self.response = ""
        
load_dotenv()
openai.api_key = os.getenv("mykey")

reference = Reference()
TOKEN = os.getenv("TOKEN")

## google search engine

client=OpenAI(openai_api_key=os.getenv("mykey"))


# MODEL name 
MODEL_NAME = "gpt-3.5-turbo"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


tool=load_tools(["serpapi"],serpapi_api_key=os.getenv("serp_api_key"),llm=client)
agent=initialize_agent(tool,client,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)



def clear_past():
    '''Clear the previous input'''
    reference.response = ""

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """This handler receives messages with '/start' or '/help'"""
    await message.reply("Hi\nI am TeleBot!\nCreated by Vikalp(Zhcet).\nHow can I assist you?")

@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
    Hi There, I'm a chatGPT Telegram bot created by Vikalp! Please follow these commands!!\n
    /start - to start the conversation.
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    /vikalp-to get about vikalp.
    I hope this helps. :)
    """
    await message.reply(help_command)

@dp.message_handler(commands=['vikalp'])
async def about(message:types.Message):
     command="""
     Vikalp is currently doing B.Tech from ZHCET-AMU.\n
     He is from Bahjoi.\n
     And his father name is Kaushal Kumar .\n
     """
     
     await message.reply(command)
     
     
# @dp.message_handler()
# async def chatgpt(message: types.Message):
#     """A handler to process the users input and generate a response using the ChatGPT API."""
#     print(f">>>USER:\n\t{message.text}")
#     try:
#      #    response = openai.ChatCompletion.create(
#      #        model=MODEL_NAME,
#      #        messages=[
#      #            {"role": "assistant", "content": reference.response},
#      #            {"role": "user", "content": message.text}
#      #        ]
#      #    )
#      #    reference.response = response.choices[0].message.content
#         response=agent.run(message.text)
#         print(f">>> Chatgpt:\n\t{reference.response}")
#         await bot.send_message(chat_id=message.chat.id, text=reference.response)
#     except Exception as e:
#         print(f"Error: {e}")
#         await message.reply("I'm sorry, I encountered an error while processing your request.")
 
 
@dp.message_handler()
async def chatgpt(message: types.Message):
    """A handler to process the users input and generate a response using the ChatGPT API."""
    print(f">>>USER:\n\t{message.text}")
    try:
        response = agent.run(message.text)
        # Assuming response contains the message directly, if not, you'll need to extract the message text correctly
        reference.response = response 
        print(f">>> Chatgpt:\n\t{reference.response}")
        await bot.send_message(chat_id=message.chat.id, text=reference.response)
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("I'm sorry, I encountered an error while processing your request.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
