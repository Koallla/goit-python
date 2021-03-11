from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, name, *phone):
        self.data.update(Record(name, phone).data_dict)

    def show_all(self):
        print(self.data)


class Record:
    data_dict = {}

    def __init__(self, name, phone):
        self.key = Name(name)
        # self.name = Name(name)
        self.phones = Phone(set(phone))

        if self.key not in self.data_dict:
            self.data_dict[self.key.name] = self.phones.phones

    def add_number(self, name, number):
        self.data_dict[name].add(number)

    def delete_all_number(self, name):
        self.data_dict[name].clear()


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phones = phone


a = AddressBook()
a.add_record('Kirill', 1111111, 2222222, 55555555)
a.add_record('Liza', 1, 2, 55)
