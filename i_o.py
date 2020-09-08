import os
from converter import roman_to_decimal


def read_from_file():
    file_name = input("Enter the name of the file to convert: ")
    if os.path.isfile(file_name):
        converted_numbers = []
        with open(file_name) as number_reader:
            for number in number_reader:
                converted_numbers.append(f'{number.strip()} = {roman_to_decimal(number.strip())}\n')
        with open(f'converted_{file_name}', 'w') as number_writer:
            for number in converted_numbers:
                number_writer.write(number)
        print('Numbers to convert detected\n')
        for number in converted_numbers:
            print(number)
        print(f'all numbers saved to converted_{file_name}')
    else:
        print(f'File {file_name} not detected')
    return 0


def read_from_console():
    number = 'meow'
    while number:
        number = input('Please enter a number to convert: ')
        converted = roman_to_decimal(number)
        if isinstance(converted, str):
            print(f'{number} is {converted}')
        else:
            print(f'{number} = {converted}')