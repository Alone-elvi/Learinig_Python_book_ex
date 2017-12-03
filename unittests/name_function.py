# -*- coding: utf-8 -*-

# def get_formatted_name(first, last):
#     """Строит отформатированное полное имя."""
#     full_name = first + ' ' + last
#     return full_name.title()


def get_formatted_name(first, last, middle=''):
    """Строит отформатированное полное имя."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()
