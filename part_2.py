from aiogram import Bot, Dispatcher, executor
from config import TOKEN, ADMIN_ID
from aiogram.types import Message

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: Message):
    await message.reply(message.text)


async def on_startup(_):
    await bot.send_message(ADMIN_ID, "Bot was started !!!")


async def on_shutdown(_):
    await bot.send_message(ADMIN_ID, "Bot was shutted down !!!")


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )

