from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp)

