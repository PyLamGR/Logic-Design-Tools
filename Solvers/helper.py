def language(text):
    return {
        'Error.Base': 'You are trying to use an incorrect base'
    }.get(text, 'N/A')


def check_base(number, base):
    """
    Checks if a number belongs to that base
    :param number: String of number we are checking
    :param base: Integer that represents what base we are in
    :return: True if the number belongs to the base, False otherwise
    """
    assert 2 <= base <= 36, language('Error.Base')
    if base <= 10:
        max_allowed_n = base - 1
    elif base <= 36:
        max_allowed_n = 54 + base

    number = str(number).upper()  # Covert number to Uppercase ( Max base: 36 )

    for letter in number:
        if letter.isnumeric() and int(letter) <= max_allowed_n:
            continue
        elif letter <= chr(max_allowed_n):
            continue
        else:
            return False
    return True
