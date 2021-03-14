from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):

    def add_record(self, record):
        if record.key.value in self.data:
            self.data[record.key.value].update(record.data_dict)
        else:
            self.data[record.key.value] = record.data_dict

    def __str__(self):
        return f'Records in AddressBook: {self.data}'


class Record:

    def __init__(self, name, value, *data):
        self.data_dict = {}
        self.key = Name(name)
        self.value = value
        if value == 'birthday':
            # print(*data)
            self.contact_data = Birthday(data)
        else:
            self.contact_data = Phone(list(data))

        if self.key not in self.data_dict:
            self.data_dict[self.value] = self.contact_data.value

    def add_data(self, field, *data):
        if field in self.data_dict and field != 'birthday':
            for data_element in data:
                self.data_dict[field].append(data_element)
        else:
            if field == 'birthday':
                self.data_dict[field] = Birthday(data).value
            else:
                self.data_dict[field] = list(data)

    def delete_data_in_field(self, field):
        for key, value in self.data_dict.items():
            if key == field:
                value.clear()


    def days_to_birthday(self):
        date_with_current_year = self.data_dict['birthday'].replace(year=datetime.now().year)
        if date_with_current_year > datetime.now():
            print((date_with_current_year - datetime.now()).days)
        else:
            year_delta = timedelta(days=365)
            dif = (date_with_current_year + year_delta) - datetime.now()
            print(dif.days)

    def __str__(self):
        return f'{self.data_dict}'


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Birthday(Field):

    def __init__(self, data):
        self.value = datetime(*data)

    def __str__(self):
        return f'Birthday date is {self.value.date()}'


kirill = Record('Kirill', 'birthday', 1983, 7, 12)


a = AddressBook()
a.add_record(kirill)
# print(a)
kirill.add_data('phones', 1, 5, 44)

kirill.days_to_birthday()

print(a)

