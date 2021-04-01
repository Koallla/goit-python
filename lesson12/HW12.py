from collections import UserDict
from datetime import datetime, timedelta
import pickle

from helpers import check_birthday_date, WrongDateFormat, check_phone_number, WrongPhoneNumberFormat


class AddressBook(UserDict):
    field_names = ['user', 'data']

    def add_record(self, record):
        self.data[record.name] = record

    def iterator(self, record_count):
        result = ''

        if record_count > len(self.data):
            print(f'Max count item {len(self.data)}')
        elif record_count == len(self.data):
            print(self.__str__())
        else:
            for key, value in self.data.items():
                if record_count:
                    result += f'{key}: {value} \n'
                    record_count -= 1
                else:
                    print(result)
                    break

    def save_data(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self.data, file)

    def load_data(self, path):
        with open(path, 'rb') as file:
            self.data = pickle.load(file)

    def get_user_list(self, input_data=None):
        user_list = []
        input_data = str(input_data).lower()
        for name, value in self.data.items():
            try:
                if str(name).lower().find(input_data) >= 0:
                    user_list.append([name, str(value)])
                for phone in value.phones:
                    if input_data in str(phone):
                        user_list.append([name, str(value)])
            except AttributeError:
                continue

        if user_list:
            print(user_list)
        else:
            print('User was not found')

    def __str__(self):
        result = ''
        for key, value in self.data.items():
            result += f'{key}: {value} \n'
        return result


class Record:
    def __init__(self, name, value, *phone, birthday=None):
        self.value = value
        self.name = name
        if phone:
            self.phones = Phone(phone).value
        if birthday:
            self.birthday = Birthday(birthday).value

    def add_data(self, field, *data):
        if field == 'birthday':
            b = Birthday(str(*data))
            self.birthday = b.value
        else:
            p = Phone(data)
            p.value = data
            if len(p.value) == 1:
                self.phones.append(p.value[0])
            else:
                for item in p.value:
                    self.phones.append(item)

    def delete_data_in_field(self, field):
        if field == 'birthday':
            self.birthday = None
        else:
            self.phones.clear()

    def days_to_birthday(self):
        date_with_current_year = self.birthday.replace(year=datetime.now().year)
        if date_with_current_year > datetime.now():
            dif = date_with_current_year - datetime.now()
            print(f'{dif.days} days')
        else:
            year_delta = timedelta(days=365)
            dif = (date_with_current_year + year_delta) - datetime.now()
            print(f'{dif.days} days')

    def __str__(self):
        try:
            return f'{self.value}: {self.phones}, birthday: {self.birthday.date()}'
        except AttributeError:
            return f'{self.value} {self.phones}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.__value = []
        self.value = value

    def __getitem__(self, key=None):
        return self.__value

    def __setitem__(self, key, value):
        if type(value) != int:
            raise Exception('Only one number and integer')
        try:
            check_phone_number(value)
            if len(self.__value) and key < (len(self.__value)):
                self.__value.pop(key)
                self.__value.insert(key, value)
            elif key > (len(self.__value)):
                raise IndexError
            else:
                self.__value.append(value)
        except WrongPhoneNumberFormat:
            print('Please, enter number in format 380_________')
        except IndexError:
            print(f'Max index {len(self.__value)}')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, number):
        try:
            if type(number) == int:
                check_phone_number(number)
                self.__value.append(number)
            else:
                for item in number:
                    check_phone_number(item)
                    self.__value.append(item)
        except WrongPhoneNumberFormat:
            print('Please, enter number in format 380_________')

    def __str__(self):
        return f'Phone: {self.__value}'


class Birthday(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __getitem__(self, key=None):
        return self.__value

    def __setitem__(self, key, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        try:
            check_birthday_date(data)
            self.__value = (datetime.strptime(data, '%d %m %Y'))
        except WrongDateFormat:
            print('Please, input birthday date in format "%d %m %Y" ')

    # def __str__(self):
    #     return f'Birthday: {self.__value}'


# Для проверки

Kirill = Record('Kirill', 'phone', 380951111111, 380502222222)
Ola = Record('Ola', 'phone', 380953333333, 380504444444, birthday='23 07 2014')
Liza = Record('Liza', 'phone', 380955555555, 380506666666, birthday='12 01 1983')
Koala = Record('Koala', 'phone', 380953128882, 380509999999, birthday='22 07 1983')

a = AddressBook()
a.add_record(Kirill)
a.add_record(Ola)
a.add_record(Liza)
a.add_record(Koala)
#
# a.save_data('test.bin')
# a.load_data('test.bin')
#
a.get_user_list('z')
a.get_user_list(3333)
