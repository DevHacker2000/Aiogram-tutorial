from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(TOKEN)
dp = Dispatcher(bot)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Flask docs",
                url="https://flask.palletsprojects.com/en/2.2.x/"
            ),
            InlineKeyboardButton(
                text="inline2",
                callback_data="inline2"
            ),
        ]
    ]
)


alternate_inline_kb = InlineKeyboardMarkup(row_width=1)

inline_btn = InlineKeyboardButton(text="alternate", callback_data="alt")
inline_btn2 = InlineKeyboardButton(text="alternate2", callback_data="alt2")
alternate_inline_kb.add(inline_btn, inline_btn2)


@dp.message_handler(commands="start")
async def handle_start_command(message: Message):
    await message.answer(
        "Hello let's start",
        reply_markup=alternate_inline_kb
    )


if __name__ == "__main__":
    executor.start_polling(dp)


