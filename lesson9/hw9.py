import json


# Будем сохранять контакты в файл .json

def input_error(func):
    def inner(*data):
        try:
            return func(*data)
        except KeyError:
            return print('Please, enter correct command...')
        except ValueError:
            return print("Name or number is empty")
        except NameError:
            return print("Name is not found")
        except FileNotFoundError:
            return print("No contacts")

    return inner


# Получение имени и номера из введеной команды
def get_name_and_number(command):
    command = command.split(' ')
    if len(command) == 3:
        command.pop(0)
        name, number = command[0], command[1]
        if name and number:
            new_dict = {}
            new_dict[name] = number
            return new_dict, name
        else:
            return False
    else:
        return False


def func_hello(message=True):
    print('How can I help you?')


@input_error
def func_add(command):
    print('Working command add...')
    if get_name_and_number(command):
        new_dict, name = get_name_and_number(command)
        dict_json = json.dumps(new_dict)
        try:
            with open('contacts.json', 'r') as fh:
                file = fh.read()
                current_dict = json.loads(file)
                current_dict.update(new_dict)

                with open('contacts.json', 'w') as fh:
                    fh.write(json.dumps(current_dict))
                    print(f'phone number of {name} was saved!')
        except FileNotFoundError:
            with open('contacts.json', 'a') as fh:
                fh.write(dict_json)
                print(f'phone number of {name} was saved!')

    else:
        raise ValueError


@input_error
def func_change(command):
    print('Working command change...')
    if get_name_and_number(command):
        with open('contacts.json', 'r') as fh:
            file = fh.read()
            current_dict = json.loads(file)
            new_dict, name = get_name_and_number(command)
            if current_dict.get(name):
                current_dict.update(new_dict)
                with open('contacts.json', 'w') as fh:
                    fh.write(json.dumps(current_dict))
                    print(f'phone number of {name} was changed!')


            else:
                raise NameError
    else:
        raise ValueError


@input_error
def func_phone(command):
    print('Working command phone...')
    command = command.split(' ')
    if len(command) == 2:
        name = command[1]
        with open('contacts.json', 'r') as fh:
            file = fh.read()
            current_dict = json.loads(file)
            for key, value in current_dict.items():
                if key == name:
                    print(f'phone number of {name} is {value}')
                    return
            raise NameError
    else:
        raise ValueError


@input_error
def func_show_all(message=True):
    print('Working command show all...')

    with open('contacts.json', 'r') as fh:
        file = fh.read()
        current_dict = json.loads(file)
        format_str = ''
        max_len_name = 0
        max_len_number = 0
        for key, value in current_dict.items():
            if len(key) > max_len_name:
                max_len_name = len(key)
            if len(value) > max_len_number:
                max_len_number = len(value)
        for key, value in current_dict.items():
            s = "| {:^{width_name}} | {:^{width_number}} |".format(key, value, width_name=max_len_name,
                                                                   width_number=max_len_number)
            format_str += (s + '\n')

        print(format_str)


def func_good_bye(message=True):
    print('Goodbye!')


COMANDS = {
    'hello': func_hello,
    'add': func_add,
    'change': func_change,
    'phone': func_phone,
    'show all': func_show_all,
    'good bye': func_good_bye,
    'close': func_good_bye,
    'exit': func_good_bye,
}


def main():
    while True:

        command = input("Please, enter command: ")

        @input_error
        def get_handler(command):
            command = command.lower()
            command_in_list = command.split(' ')
            # Первые два слова из введенной строки
            if len(command_in_list) > 1:
                first_two_word = f'{command_in_list[0]} {command_in_list[1]}'
                # Если есть ключ, который состоит из двух слов, берем его значение, нет - берем ключ по первому слову
                # из введеной строки
                return COMANDS[first_two_word] if COMANDS.get(first_two_word) else COMANDS[command_in_list[0]]
            else:
                return COMANDS[command]

        heandler = get_handler(command)

        if heandler:
            heandler(command)

        if command in ('good bye', 'exit', 'close'):
            break


main()
