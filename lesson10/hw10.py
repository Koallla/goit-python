from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, name, *phone):
        self.data.update(Record(name, phone).data_dict)

    def show_all(self):
        print(self.data)


class Record:
    data_dict = {}

    def __init__(self, name, phone):
        self.key = Name(name).name
        # self.name = Name(name).
        self.phone = Phone(list(phone))

        if self.key not in self.data_dict:
            self.data_dict[self.key] = self.phone.phone


    # def add_number(self, number):
    #     self.phone.append(number)
    #
    # def delete_number(self, number):
    #     self.phone.remove(number)


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name



class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


a = AddressBook()
a.add_record('Kirill', 1111111, 2222222, 55555555)
a.show_all()
