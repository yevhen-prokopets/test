# -*- coding: utf8 -*-
import logging
# -*- coding: cp1251 -*-
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

bot = Bot(token='5360966327:AAElcL-Cf6iSPC08Mur9QDgmktcfW_Ks6Co')
dp = Dispatcher(bot, storage=MemoryStorage())
class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()





button1 = KeyboardButton('вперед')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1)
button11 = KeyboardButton('заглушка')
button12 = KeyboardButton('заглушка')
button13 = KeyboardButton('заглушка')
button14 = KeyboardButton('заглушка')
button15 = KeyboardButton('заглушка')
button16 = KeyboardButton('заглушка')
button17 = KeyboardButton('заглушка')
button18 = KeyboardButton('заглушка')
button19 = KeyboardButton('заглушка')
button20 = KeyboardButton('заглушка')
button21 = KeyboardButton('заглушка')
button22 = KeyboardButton('заглушка')
button23 = KeyboardButton(' заглушка')
button24 = KeyboardButton('заглушка')
button25 = KeyboardButton('заглушка')
button26 = KeyboardButton('заглушка')
button27 = KeyboardButton('заглушка')
button28 = KeyboardButton('заглушка')
button29 = KeyboardButton('заглушка')
button30 = KeyboardButton('заглушка')
button31 = KeyboardButton('заглушка')
button32 = KeyboardButton('заглушка')

keyboard11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard11.row(button11, button12)
keyboard11.row(button16, button15)
keyboard11.row(button18, button17)
keyboard11.row(button14, button13)
keyboard11.row(button19, button20)
keyboard11.row(button21, button22)
keyboard11.row(button23, button24)
keyboard11.row(button25, button26)
keyboard11.row(button27, button28)
keyboard11.row(button29, button30)
keyboard11.row(button31, button32)

button2 = KeyboardButton('заглушка', request_contact=True)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button2)
button3 = KeyboardButton('Start', )
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button3)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, "заглушка ",reply_markup=keyboard1, parse_mode= "Markdown")
    await bot.send_message(message.chat.id, 'заглушка', reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '«заглушка':
        await message.answer('заглушка):',reply_markup=keyboard11)
        await Test.Q1.set()



@dp.message_handler(state=Test.Q1)
async def answer_for_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q1'] = message.text
    await message.answer('заглушка')
    await Test.next()



@dp.message_handler(state=Test.Q2)
async def answer_for_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = message.text
    await Test.next()

    await message.answer("заглушка.", parse_mode= "Markdown")



@dp.message_handler(state=Test.Q3)
async def answer_for_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = data.get("Q2")
    answer3 = message.text
    await Test.next()
    await message.answer('заглушка', reply_markup=keyboard2)

@dp.message_handler(content_types=['contact'], state=Test.Q4)
async def test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = data.get("Q2")
    answer3 = data.get("Q3")
    answer4 = message.contact.phone_number

    full_q = 'Питання 1: {0}\bПитання 2: {1}\nПитання 3: {2}\nНомер телефону: {3}'.format(

        answer1, answer2, answer3, answer4)
    await bot.send_message('-653478073', full_q)
    await welcome(message)



if __name__ == "__main__":

    try:

        executor.start_polling(dp, skip_updates=True)

    except Exception as e:

        print(e)
