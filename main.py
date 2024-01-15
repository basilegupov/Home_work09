""""hello", відповідає у консоль "How can I help you?" "add ...". За цією командою бот зберігає у пам'яті (у словнику
наприклад) новий контакт. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл. "change
..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... користувач вводить
ім'я та номер телефону, обов'язково через пробіл. "phone ...." За цією командою бот виводить у консоль номер телефону
для зазначеного контакту. Замість ... користувач вводить ім'я контакту, чий номер треба показати. "show all". За цією
командою бот виводить всі збереженні контакти з номерами телефонів у консоль. "good bye", "close", "exit" по
будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!"."""


phonebook = {}
LIST_COMMANDS = ['hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', 'exit', '.']


def parse_command(input_str):
    input_str = input_str.lower().split()

    command_str = ' '.join(input_str)
    print(command_str)
    return command_str


def hello():
    return "How can I help you?"


def add_phone(name: str, number: str):
    # rec = phonebook.get(name, '')
    phonebook[name] = number


def change_phone(name: str, number: str):
    phonebook[name] = number


def show_phone(name: str):
    return phonebook[name]


def show_all():
    for name, number in phonebook:
        print(f'Name: {name} phone:{number}')


def bye():
    return "Good bye!"


def command_handler(command_str):
    if command_str in LIST_COMMANDS:

    result = ''
    return result


def main(user_input):
    while True:
        # user_input = input('Enter >>')
        command = parse_command(user_input)
        print(command)
        result = command_handler(command)
        print(result)
        break


if __name__ == '__main__':
    main('add Basil +380505852071')
    main('add Basil1 +380505852072')
    main('add Basil2 +380505852073')
    main('add Basil3 +380505852074')
    main('add Basil4 +380505852075')
    main('add Basil5 +380505852076')
    main('add Basil6 +380505852077')
    main('add Basil7 +380505852078')
    main('show all')
