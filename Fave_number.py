import json


def store_number(file_name):
    fave_num = input('Please enter your favorite number: ')

    with open(file_name, 'w') as file:
        json.dump(fave_num, file)
        print(f'We will remember your favorite number, {fave_num}')


def get_number(file_name):
    try:
        with open(file_name) as file:
            fave_num = json.load(file)
            fave_num = int(fave_num)
    except FileNotFoundError:
        store_number(file_name)
    else:
        print(f'Your favorite number is {fave_num}')


get_number('fave_number.json')
