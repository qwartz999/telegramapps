from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("8065680595:AAEGU1tZW9NKfq6_Q6Y4gQKffJ3M1aid2WQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://qwartz999.github.io/telegramapps/apptg.html')))
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(dp)