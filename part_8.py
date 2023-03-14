from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message
from config import TOKEN


class UserInfoState(StatesGroup):
    username = State()
    age = State()
    email = State()


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def handle_start_command(message: Message, state: FSMContext):
    await state.set_state(UserInfoState.username.state)
    await message.answer("Enter your name")


@dp.message_handler(state=UserInfoState.username)
async def set_name(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(UserInfoState.age.state)
    await message.answer("Enter your age")


@dp.message_handler(state=UserInfoState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserInfoState.email.state)
    await message.answer("Enter your email")


@dp.message_handler(state=UserInfoState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    user_data = await state.get_data()
    await message.answer(
        f"Your name is {user_data['username']},"
        f" your age is {user_data['age']},"
        f" your email is {user_data['email']}"
    )
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp)


