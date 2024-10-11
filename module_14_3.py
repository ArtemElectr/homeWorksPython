from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)


kb = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')

kb.add(button3, button4)

kb_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Яблочный сок', callback_data='product_buying'),
            InlineKeyboardButton(text='Апельсиновый сок', callback_data='product_buying'),
            InlineKeyboardButton(text='Ананасовый сок', callback_data='product_buying'),
            InlineKeyboardButton(text='Томатный сок', callback_data='product_buying')
        ],

    ],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer(text='Название: Апельсиновый сок | Описание: Свежевыжатый апельсиновый сок | Цена: 200')
    with open('files/shutterstock_71010697.0.jpeg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Яблочный сок | Описание: Свежевыжатый яблочный сок | Цена: 150')
    with open('files/8dbf5ae4fdff321c612627522b4efba2.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Ананасовый сок | Описание: Свежевыжатый Ананасовый сок | Цена: 250')
    with open('files/Сок-ананасовый-свежевыжатый.jpg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Название: Томатный сок | Описание: Свежевыжатый Томатный сок | Цена: 120')
    with open('files/tomatnyy-sok.jpeg', 'rb') as img:
        await message.answer_photo(img)
    await message.answer(text='Выберите продукт для покупки:', reply_markup=kb_3)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


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
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_)


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)