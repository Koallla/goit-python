from datetime import datetime, timedelta


d1 = datetime(year=1983, month=1, day=7)

users = {
    'Bill': datetime(year=1983, month=2, day=13),
    'John': datetime(year=1991, month=2, day=14),
    'Carl': datetime(year=2012, month=2, day=23),
    'Carlito': datetime(year=1985, month=2, day=19),
    'Carlos': datetime(year=2002, month=2, day=20),
    'Carl2': datetime(year=1988, month=2, day=27),
    'Liza': datetime(year=2014, month=7, day=23),
    'Kirill': datetime(year=2020, month=2, day=14),
    'Bart': datetime(year=2021, month=2, day=14)
}



current_datetime = datetime.now()
change_current_date = current_datetime

seven_days_delta = timedelta(days=7)
time_start = None
friday = 4
users_birthdays = {}

for user, date in users.items():
    # Заменяем год на текущий, чтобы сравнивать объекты datetime
    date_with_current_year = date.replace(year=current_datetime.year)

    # Создаем день отсчета пятницу
    time_start = current_datetime + timedelta(days = friday - current_datetime.weekday())

    if time_start <= date_with_current_year <= time_start + seven_days_delta:
        users_birthdays[user] = date


print(users_birthdays)