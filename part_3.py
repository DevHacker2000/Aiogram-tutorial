from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Command
from config import TOKEN
from aiogram.types import Message

bot = Bot(TOKEN)
dp = Dispatcher(bot)


# Command(["start", "help"])
@dp.message_handler(commands=["start", "help"])
async def handle_start_command(message: Message):
    await message.answer("Hello let's start")


@dp.message_handler()
async def echo(message: Message):
    await message.reply(message.text)


if __name__ == "__main__":
    executor.start_polling(dp)

