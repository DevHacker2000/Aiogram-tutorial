from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text, Command
from config import TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


bot = Bot(TOKEN)
dp = Dispatcher(bot)

# text="hello"


@dp.message_handler(Text(startswith=["hello", "hi"]))
async def say_hi(message: Message):
    await message.answer("Hello programmer !!!")

# commands=["start", "help"]


@dp.message_handler(Command(["start", "help"], ignore_case=True))
async def handle_start_command(message: Message):
    await message.answer("Hello let's start")


@dp.message_handler(lambda m: m.text == "Bye")
async def say_bye(message: Message):
    await message.answer("Goodbye")


if __name__ == "__main__":
    executor.start_polling(dp)


