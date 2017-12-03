import json

filename = '../files/txt/lovely_number.json'


def get_stored_number():
    """Возвращает сохраненное любимое число"""
    try:
        with open(filename) as f_obj:
            item = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return item


def get_new_number():
    """ Запрашивает новое любимое число"""
    item = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(item, f_obj)
    return item


def get_number():
    """Показывает любимое число или, если нет файла его хранящего, просит ввести"""
    l_number = get_stored_number()
    if l_number:
        print('Your favorite number is ' + l_number)
    else:
        l_number = get_new_number()


get_number()
