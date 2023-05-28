import re
from enum import Enum
import logging

URL = 'https://portal.omgups.ru/extranet/raspisanie/semester2_2022-2023/raspisanie_iatit/40.htm'
API_TOKEN = '5998384248:AAGa4_UX5grl7dEHz-BjzzNwEAqaWboGSqc'
days_dict = {
    0: 'Пнд',
    1: 'Втр',
    2: 'Срд',
    3: 'Чтв',
    4: 'Птн',
    5: 'Сбт',
    6: 'Вск'
}
reg = r"а\..{5}"
logging.basicConfig(level=logging.INFO)

def schedule_print(today: str, day_info: list[str]):
    return f"""День недели- {today}
Первая пара
Пара: {day_info[1][:len(day_info[1]) - 11]}
Время: 08:00-09:30
Аудитория: {str(re.findall(reg, day_info[1])[0] if len(re.findall(reg, day_info[1])) > 0 else '-')}

Вторая пара 
Пара: {day_info[2][:len(day_info[2]) - 11]}
Время: 09:45-11:15
Аудитория: {str(re.findall(reg, day_info[2])[0] if len(re.findall(reg, day_info[2])) > 0 else '-')}

Третья пара 
Пара: {day_info[3][:len(day_info[3]) - 11]}
Время: 11:30-13:00
Аудитория: {str(re.findall(reg, day_info[3])[0] if len(re.findall(reg, day_info[3])) > 0 else '-')}

Четвертая пара
Пара: {day_info[4][:len(day_info[4]) - 11]}
Время: 13:55-15:25
Аудитория: {str(re.findall(reg, day_info[4])[0] if len(re.findall(reg, day_info[4])) > 0 else '-')}

Пятая пара
Пара: {day_info[5][:len(day_info[5]) - 11]}
Время: 15:40-17:10
Аудитория: {str(re.findall(reg, day_info[5])[0] if len(re.findall(reg, day_info[5])) > 0 else '-')}
"""
