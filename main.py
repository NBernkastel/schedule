import datetime
import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
from utuls import URL, API_TOKEN, days_dict, schedule_print

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['get'])
async def send_welcome(message: types.Message):
    time = datetime.datetime.now()
    day_of_week = time.weekday()
    week_number = time.isocalendar()[1]
    today = days_dict[day_of_week]
    week = True if week_number % 2 else False
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabl = soup.find_all('tr')
    day_info = []
    del tabl[0]
    del tabl[0]
    if week:
        del tabl[6:]
    for days in tabl:
        day_content = days.find_all('p')
        if day_content[0].text == today:
            for p in day_content:
                day_info.append(p.text)
    if day_of_week < 6:
        out = schedule_print(today, day_info)
    else:
        out = 'Чел спи'
    await message.answer(out)


@dp.message_handler(commands=['nex'])
async def send_welcome(message: types.Message):
    time = datetime.datetime.now()
    day_of_week = time.weekday()
    day_of_week = day_of_week + 1 if day_of_week < 6 else 0
    print(day_of_week)
    week_number = time.isocalendar()[1]
    today = days_dict[day_of_week]
    week = True if week_number % 2 else False
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabl = soup.find_all('tr')
    day_info = []
    del tabl[0]
    del tabl[0]
    if week:
        del tabl[6:]
    for days in tabl:
        day_content = days.find_all('p')
        if day_content[0].text == today:
            for p in day_content:
                day_info.append(p.text)
    if day_of_week < 6:
        out = schedule_print(today, day_info)
    else:
        out = 'Чел спи'
    await message.answer(out)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
