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





button1 = KeyboardButton('«Своих не бросаем!')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1)
button11 = KeyboardButton('Киевская Область')
button12 = KeyboardButton('Харьковская Область')
button13 = KeyboardButton('Херсонская Область')
button14 = KeyboardButton('Сумская Область')
button15 = KeyboardButton('Донецкая область')
button16 = KeyboardButton('Луганская Область')
button17 = KeyboardButton('Черниговская Область')
button18 = KeyboardButton('Житомирская область')
button19 = KeyboardButton('Одесская область')
button20 = KeyboardButton('Закарпатская область')
button21 = KeyboardButton('Волынская область')
button22 = KeyboardButton('Днепропетровская область')
button23 = KeyboardButton(' Полтавская область')
button24 = KeyboardButton('Ровенская область')
button25 = KeyboardButton('Львовская область')
button26 = KeyboardButton('Тернопольская область')
button27 = KeyboardButton('Винницкая область')
button28 = KeyboardButton('Ивано-Франковская область')
button29 = KeyboardButton('Хмельницкая область')
button30 = KeyboardButton('Черкасская область')
button31 = KeyboardButton('Черновицкая область')
button32 = KeyboardButton('Кировоградская область')

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

button2 = KeyboardButton('Отправить Информацию', request_contact=True)
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button2)
button3 = KeyboardButton('Start', )
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button3)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, "*Активисты группы «Багратион Z» совместно с Министерством обороны Российской Федерации приветствуем Вас!* \n Этот ресурс создан для помощи нашим военным, которые принимают участие в проведении специальной военной операции на Украине. \n Наши военные нуждаются в следующей информации: \n 1.Место и время обнаружения сил противника; \n 2.Количественный состав техники противника и её тип; \n 3.Количество личного состава боевиков ВСУ; \n 4.Информация о националистически настроенных лицах. \n Военные аналитики группы «Багратион Z» получают эти сведения от Вас и немедленно передают в Штаб Специальной военной операции. \n Поможем нашим братьям, освободим от националистической власти, изменим мир к лучшему!  ",reply_markup=keyboard1, parse_mode= "Markdown")
    await bot.send_message(message.chat.id, 'Для начала пользования ботом нажмите: «Своих не бросаем!', reply_markup=keyboard1)



@dp.message_handler(lambda message: message.text == "«Своих не бросаем!")
async def kb_answer(message: types.Message):
    try:
        await message.answer('В какой области был замечен противник?):',reply_markup=keyboard11)
        await Test.Q1.set()
    except Exception as e:
        print(e)

@dp.message_handler(state=Test.Q1)
async def answer_for_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q1'] = message.text
    await message.answer('Укажите город, населенный пункт, а также название улицы или какой-либо ориентир (по возможности укажите геометку')
    await Test.next()



@dp.message_handler(state=Test.Q2)
async def answer_for_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = message.text
    await Test.next()

    await message.answer("Опишите замеченные силы противника (количество и вид техники; личный состав противника).\n В случае с *движущимися силами противника* указывайте вероятное направление движения и обращайте внимание на количество бензозаправщиков. *Пример*: Город «А», колона 4 бензовоза, 2 БМП, 3 БТР. Движутся в направлении города «Б» по улице Победы. Личный состав 30 человек. В случае со *стационарными силами противника* указывайте тип (блокпост, склад, воинская часть, казарма), адрес и ориентир. *Пример*: Город «А», в здании по адресу: ул. Победы, 1 расположена казарма. Во дворе техника: 2 БМП, 3 БТР. Личный состав 200 человек.", parse_mode= "Markdown")



@dp.message_handler(state=Test.Q3)
async def answer_for_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = data.get("Q2")
    answer3 = message.text
    await Test.next()
    await message.answer('Если у вас есть фото- или видеоматериалы сил и средств противника, Вы можете дополнительно прикрепить их к сообщению.\n Для передачи данных нашим военным аналитикам нажмите: «Отправить информацию»', reply_markup=keyboard2)

@dp.message_handler(content_types=['contact'], state=Test.Q4)
async def test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("Q1")
    answer2 = data.get("Q2")
    answer3 = data.get("Q3")
    answer4 = message.contact.phone_number
    await state.finish()
    full_q = 'Питання 1: {0}\bПитання 2: {1}\nПитання 3: {2}\nНомер телефону: {3}'.format(

        answer1, answer2, answer3, answer4)
    await bot.send_message('-653478073', full_q)
    await bot.send_message(message.chat.id, "*Активисты группы «Багратион Z» совместно с Министерством обороны Российской Федерации приветствуем Вас!* \n Этот ресурс создан для помощи нашим военным, которые принимают участие в проведении специальной военной операции на Украине. \n Наши военные нуждаются в следующей информации: \n 1.Место и время обнаружения сил противника; \n 2.Количественный состав техники противника и её тип; \n 3.Количество личного состава боевиков ВСУ; \n 4.Информация о националистически настроенных лицах. \n Военные аналитики группы «Багратион Z» получают эти сведения от Вас и немедленно передают в Штаб Специальной военной операции. \n Поможем нашим братьям, освободим от националистической власти, изменим мир к лучшему!  ", reply_markup=keyboard1, parse_mode="Markdown")
    await bot.send_message(message.chat.id, 'Для начала пользования ботом нажмите: «Своих не бросаем!',reply_markup=keyboard1)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
