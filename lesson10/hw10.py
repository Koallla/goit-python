from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def show_all(self):
        print(self.data)


a = AddressBook()


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.phone = [number for number in phones]



class Field:
    name = ''
    phone = None


class Name(Field):
    pass


class Phone(Field):
    pass

