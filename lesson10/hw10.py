from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def show_all(self):
        print(self.data)


class Record:
    def __init__(self, name, phones):
        self.name = name
        self.phone = [number for number in phones]


class Field:
    name = ''
    phone = []


class Name(Field):
    pass


class Phone(Field):
    pass
