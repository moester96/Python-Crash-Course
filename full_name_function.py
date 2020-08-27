def format_name(full_name, middle_name=''):
    if middle_name:
        full_name = f'{full_name[0]} {middle_name} {full_name[1]}'
    else:
        full_name = f'{full_name[0]} {full_name[1]}'

    return full_name.title()


def get_name():
    print('Enter q or Q at any time to quit')

    while True:
        first_name = input('Please enter first name: ')
        if first_name == 'q' or first_name == 'Q':
            break
        last_name = input('Please enter last name: ')
        if last_name == 'q' or last_name == 'Q':
            break

        # formatted_name = format_name((first_name, last_name))
        print(f'Formatted name: {format_name((first_name, last_name))}\n')
