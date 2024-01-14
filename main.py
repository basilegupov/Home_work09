
phonebook = {}


def parse_command(input_str):
    input_str = input_str.lower().split()

    command_str = ' '.join(input_str)
    return command_str


def command_handler(command_str):
    result = ''
    return result


def main():
    while True:
        user_input = input('Enter >>')
        command = parse_command(user_input)
        result = command_handler(command)
        print(result)


if __name__ == '__main__':
    main()
