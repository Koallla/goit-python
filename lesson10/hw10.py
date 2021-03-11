from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record.phone

    def show_all(self):
        print(self.data)


class Record:
    phone = []

    def __init__(self, name, phone):

        self.name = name
        self.phone.append(phone.value)

    def add_number(self, number):
        self.phone.append(number)

    def delete_number(self, number):
        self.phone.remove(number)


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


