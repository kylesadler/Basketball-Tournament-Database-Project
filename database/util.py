# from .errors import *
# from tabulate import tabulate

import json
from datetime import datetime, timedelta, date

""" random util functions. May be useful """


# def get_user_input(message):
#     """ promts users for input. throws InputIsEmptyError on empty input """
#     user_input = input(message)
#     if not isinstance(user_input, str) or len(user_input) <= 0:
#         raise EmptyInputError()
#     return user_input

def get_option_from_user(message, options):
    """ get_option_from_user() prompts the user with message, reads an input string,
        and returns the option the user wants to select.
        options is a list of strings. The user can select based on index
        or name.

        raises EmptyInputError or InvalidInputError on error
    """
    user_input = get_user_input(message).lower().strip()

    try: # parse as integer index
        index = int(user_input) - 1
        assert index >= 0
        return options[index]
    except (ValueError, AssertionError, IndexError):
        # parse as string command
        if user_input in options:
            return user_input
        else:
            selected_options = [opt for opt in options if opt.lower().startswith(user_input)]
            if len(selected_options) != 1:
                raise InvalidInputError()
            return selected_options[0]

# def confirm(question, default):
#     """ asks a yes/no question to the user and converts their answer to a boolean """
#     assert default.lower() in ['y', 'n']
#     confirm = input(question) or default
#     return confirm.lower() in ['yes', 'y']

# def print_error(message):
#     """ prints an error message """
#     print(f"ERROR: {message}")

# def print_options(a_list):
#     """ prints a nicely formatted numbered list of strings """
#     space = ' '*3
#     formatted_options = [
#         f'{space}{i+1}) {thing.title()}' for i, thing in enumerate(a_list)
#         ]
#     print('\n' + '\n'.join(formatted_options) + '\n')

# def print_table(headers, rows):
#     print(f'{tabulate(rows, headers=headers)}\n')


def clean_input(query):
    """ cleans user input to be ready for DB query. uppercases everything """
    INVALID_CHARACTERS = ".'\";()!=-"

    for c in INVALID_CHARACTERS:
        query = query.replace(c, "")

    return query.upper()





NON_SERIALIZABLE_CLASSES = [ datetime, timedelta, date ]

def is_non_serializable(object_):
    """ returns True if object_ cannot be serialized in json """
    return any([isinstance(object_, class_) for class_ in NON_SERIALIZABLE_CLASSES])

def remove_non_serializable_fields(obj):
    if is_non_serializable(obj):
        obj = str(obj)
    elif isinstance(obj, list):
        obj = [remove_non_serializable_fields(x) for x in obj]
    elif isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = remove_non_serializable_fields(value)

    return obj

def to_json(d):
    """ formats dicts to json strings """
    return json.dumps(
        remove_non_serializable_fields(d)
    )

def send(object):
    print(to_json({"return": object}))
