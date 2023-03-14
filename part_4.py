from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(TOKEN)
dp = Dispatcher(bot)


# one_time_keyboard=True
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="first"),
            KeyboardButton(text="/remove_kb")
        ],
        [
            KeyboardButton(text="location", request_location=True),
            KeyboardButton(text="contact", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

keyboard_alternate = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=4
)
keyboard_alternate.add(
    KeyboardButton(text="Alternate button"),
    KeyboardButton(text="Alternate button 2")
)
keyboard_alternate.insert(KeyboardButton(text="Second row btn1"))
keyboard_alternate.insert(KeyboardButton(text="Second row btn2"))


@dp.message_handler(commands="start")
async def handle_start_command(message: Message):
    await message.answer(
        "Hello let's start",
        reply_markup=keyboard_alternate
    )


@dp.message_handler(commands="remove_kb")
async def handle_remove_kb_command(message: Message):
    await message.answer("Removing keyboard", reply_markup=ReplyKeyboardRemove())


if __name__ == "__main__":
    executor.start_polling(dp)


