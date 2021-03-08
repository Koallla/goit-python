from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def show_all(self):
        print(self.data)


class Record:
    def __init__(self, name, *phone):
        self.name = name
        self.phone = list(phone)

    def add_number(self, number):
        self.phone.append(number)

    def delete_number(self, number):
        self.phone.remove(number)




class Field:
    name = ''
    phone = []
    email = []


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    pass