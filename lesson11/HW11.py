from collections import UserDict
from datetime import datetime, timedelta
from helpers import check_birthday_date, WrongDateFormat, check_phone_number, WrongPhoneNumberFormat


class AddressBook(UserDict):
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
            p = Phone()
            p.value = phone
            self.phones = p.value
        if birthday:
            b = Birthday()
            b.value = birthday
            self.birthday = b.value

    def add_data(self, field, *data):
        if field == 'birthday':
            b = Birthday()
            b.value = str(*data)
            self.birthday = b.value
        else:
            p = Phone()
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
        return f'{self.value} {self.phones} {self.birthday}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self):
        self.__value = []

    def __getitem__(self, key=None):
        return self.__value

    def __setitem__(self, key, value):
        self.value = value

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


class Birthday(Field):

    def __init__(self):
        self.__value = None

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

    def __str__(self):
        return f'Birthday: {self.__value}'






#
# user = Record('user', 'phone', 380953128882, 380506042357, birthday='11 07 1983')
# print(user)
# user1 = Record('user1', 'phone', 380953128882, 380506042357, birthday='23 07 2014')
# user2 = Record('user2', 'phone', 380953128882, 380506042357, birthday='12 01 1983')
# user3 = Record('user3', 'phone', 380953128882, 380506042357, birthday='12 01 1983')
# user.add_data('phone', 380991245367, 380995555555)
# print(user)
# user.add_data('birthday', '12 01 1983')
# print(user)
# user.delete_data_in_field('birthday')
# print(user)
# user.add_data('birthday', '14 04 2011')
# print(user)
# user.days_to_birthday()
#
# a = AddressBook()
# a.add_record(user)
# a.add_record(user1)
# a.add_record(user2)
# a.add_record(user3)
#
# a.iterator(3)
# print(a)
