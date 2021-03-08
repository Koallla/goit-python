from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def show_all(self):
        print(self.data)


class Record:
    def __init__(self, name, phones, emails):
        self.name = name
        self.phone = [number for number in phones]
        self.email = [email for email in emails]

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
