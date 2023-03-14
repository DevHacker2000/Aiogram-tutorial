from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


bot = Bot(TOKEN)
dp = Dispatcher(bot)


alternate_inline_kb = InlineKeyboardMarkup()
inline_btn = InlineKeyboardButton(text="alternate", callback_data="first_button")
inline_btn2 = InlineKeyboardButton(text="alternate2", callback_data="second_button")
alternate_inline_kb.add(inline_btn, inline_btn2)


@dp.message_handler(commands="start")
async def handle_start_command(message: Message):
    await message.answer(
        "Hello let's start",
        reply_markup=alternate_inline_kb
    )


@dp.callback_query_handler(text="first_button")
async def handle_cb(cb: CallbackQuery):
    cb_data = cb.data
    # await cb.message.answer("Clicked!!!")
    await cb.answer(cb_data, show_alert=True)


if __name__ == "__main__":
    executor.start_polling(dp)


