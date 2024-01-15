
phonebook = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except IndexError:
            return "Contact not found"
    return wrapper


def hello():
    return "How can I help you?"


@input_error
def add_phone(name: str, number: str):
    if name in phonebook:
        raise ValueError(f'Contact {name} already exist.')
    else:
        phonebook[name] = number
        return f'Contact {name} with phone {number} added.'


@input_error
def change_phone(name: str, number: str):
    if name in phonebook:
        phonebook[name] = number
        return f'Phone number of contact {name} changed to {number}.'
    else:
        raise IndexError


@input_error
def show_phone(name: str):
    if name in phonebook:
        return f'{name}: {phonebook[name]}'
    else:
        raise IndexError


def show_all():
    if not phonebook:
        return 'Phonebook is empty.'
    phonebook_str = '|{:^16}|{:^16}|'.format('Name', 'Phone number') + '\n'
    for name, number in phonebook.items():
        phonebook_str += '|{:<16}|{:>16}|'.format(name, number) + '\n'

    return phonebook_str


def bye():
    return "Good bye!"


def main():
    while True:
        try:
            input_str = input('Enter command>>').strip()
            if not input_str:
                raise ValueError("Empty command. Please try again.")
            command, *parameter = input_str.split(' ')
            command = command.lower()
            if command == 'hello':
                print(hello())
            elif command == 'add':
                if len(parameter) != 2:
                    raise ValueError('Invalid parameters. Try again. Use "add <contact name> <phone number>"')
                else:
                    print(add_phone(*parameter))
            elif command == 'change':
                if len(parameter) != 2:
                    raise ValueError('Invalid parameters. Try again. Use "change <contact name> <phone number>"')
                else:
                    print(change_phone(*parameter))
            elif command == 'phone':
                if not parameter:
                    raise ValueError('Invalid parameter. Try again. Use "phone <contact name>"')
                print(show_phone(parameter[0]))
            elif command == 'show':
                if not parameter or not parameter[0] == 'all':
                    raise ValueError('Invalid command. Try again. Use "show all"')
                print(show_all())
            elif command == 'good':
                if not parameter or not parameter[0] == 'by':
                    raise ValueError('Invalid command. Try again. Use "good by"')
                print(bye())
                break
            elif (command == 'close' or
                  command == 'exit'):
                print(bye())
                break
            else:
                raise ValueError("Invalid command. Please try again.")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
