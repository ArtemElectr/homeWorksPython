from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = '8139003933:AAGYQqobCCfo12tNfBU9kwwI9-o0AdrLBBU'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')

kb.add(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    await message.answer(f"Ваша норма калорий {round((10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5), 2)}")
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)