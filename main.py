import datetime
import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
import re

API_TOKEN = '5291964444:AAGXq6himZqCQdqYu0b-dKAAKogMlRD_tY8'
today = datetime.datetime.now()
day_of_week = today.weekday()
week_number = today.isocalendar()[1]
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
days_dict = {
    0: 'Пнд',
    1: 'Втр',
    2: 'Срд',
    3: 'Чтв',
    4: 'Птн',
    5: 'Сбт',
    6: 'Вск'
}
TODAY = days_dict[day_of_week]
WEEK = True if week_number % 2 else False
reg = r"(?<=а\.)[^.]+"


@dp.message_handler(commands=['get'])
async def send_welcome(message: types.Message):
    url = 'https://portal.omgups.ru/extranet/raspisanie/semester2_2022-2023/raspisanie_iatit/40.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabl = soup.find_all('tr')
    day_info = []
    del tabl[0]
    del tabl[0]
    if WEEK:
        del tabl[6:]
    for days in tabl:
        day_content = days.find_all('p')
        if day_content[0].text == TODAY:
            for p in day_content:
                day_info.append(p.text)
    if day_of_week < 6:
        out = f"""День недели- {TODAY}
Первая пара
Пара: {day_info[1][:len(day_info[1])-11]}
Время: 08:00-09:30
Аудитория: {str(re.findall(reg, day_info[1])[0] if len(re.findall(reg, day_info[1])) > 0 else '-')}

Вторая пара 
Пара: {day_info[2][:len(day_info[2])-11]}
Время: 09:45-11:15
Аудитория: {str(re.findall(reg, day_info[2])[0] if len(re.findall(reg, day_info[2])) > 0 else '-')}

Третья пара 
Пара: {day_info[3][:len(day_info[3])-11]}
Время: 11:30-13:00
Аудитория: {str(re.findall(reg, day_info[3])[0] if len(re.findall(reg, day_info[3])) > 0 else '-')}

Четвертая пара
Пара: {day_info[4][:len(day_info[4])-11]}
Время: 13:55-15:25
Аудитория: {str(re.findall(reg, day_info[4])[0] if len(re.findall(reg, day_info[4])) > 0 else '-')}

Пятая пара
Пара: {day_info[5][:len(day_info[5])-11]}
Время: 15:40-17:10
Аудитория: {str(re.findall(reg, day_info[5])[0] if len(re.findall(reg, day_info[5])) > 0 else '-')}
"""
    else:
        out = 'Чел спи'
    await message.answer(out)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    gg = []
    gg.get(0)
