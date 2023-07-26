from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import random, string 


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

 


HELP_COMMAND = """
/help - list commands
/start - start work the bot
/description- desckription bot
/count - the number of your previous calls"""

# list of commands
@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

# start comand 
@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.answer(text="Hello")
    await message.delete()

# description amd delete message
@dp.message_handler(commands = ['description'])
async def description_command(message: types.Message):
    await message.answer(text="This bot very good bot")
    await message.delete()

# the number of calls
count=0
@dp.message_handler(commands = ['count'])
async def count_command(message: types.Message):
    global count
    count+=1
    await message.answer(text=count)

# echo comand
@dp.message_handler()
async def echo(message: types.Message):
    if "0" in message.text:
        await message.answer(text = "Yes")
    else:
        await message.answer(text = "No")
    await message.reply(random.choice(string.ascii_letters))





if __name__ == "__main__":
    executor.start_polling(dp)