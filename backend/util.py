# from .errors import *
# from tabulate import tabulate

""" random util functions. May be useful """


def get_user_input(message):
    """ promts users for input. throws InputIsEmptyError on empty input """
    user_input = input(message)
    if not isinstance(user_input, str) or len(user_input) <= 0:
        raise EmptyInputError()
    return user_input

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

def confirm(question, default):
    """ asks a yes/no question to the user and converts their answer to a boolean """
    assert default.lower() in ['y', 'n']
    confirm = input(question) or default
    return confirm.lower() in ['yes', 'y']

def print_error(message):
    """ prints an error message """
    print(f"ERROR: {message}")

def print_options(a_list):
    """ prints a nicely formatted numbered list of strings """
    space = ' '*3
    formatted_options = [
        f'{space}{i+1}) {thing.title()}' for i, thing in enumerate(a_list)
        ]
    print('\n' + '\n'.join(formatted_options) + '\n')

def print_table(headers, rows):
    print(f'{tabulate(rows, headers=headers)}\n')


def clean_input(query):
    """ cleans user input to be ready for DB query. uppercases everything """
    INVALID_CHARACTERS = ".'\";()!=-"

    for c in INVALID_CHARACTERS:
        query = query.replace(c, "")

    return query.upper()
