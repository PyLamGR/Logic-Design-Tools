from Solvers.helper import check_base


class BaseConverter:
    @classmethod
    def any_to_dec(cls, number, base):
        """
        Convert a number from any base to Decimal
        :param number:
        :param base:
        :return: The Decimal result if successful, None otherwise
        """
        assert 2 <= base <= 36, 'Wrong base'
        assert check_base(number, base), 'Invalid number'
        if not check_base(number, base):
            return None

        temp = list(str(number).upper())  # Split a string to its characters
        length = len(temp)
        result = 0
        temp.reverse()
        # The if for the basis from 2 to 10!
        if 2 <= base <= 10:
            temp = list(map(int, temp))
            for i in range(length):
                result += temp[i] * (base ** i)
        if 10 < base <= 36:
            for i in range(length):
                if 65 <= ord(temp[i]) <= 90:  # Check if temp[i] is letter between A-Z
                    letter_value = (ord(temp[i]) - 55)
                    result += letter_value * (base ** i)
                elif temp[i].isnumeric():
                    result += int(temp[i]) * (base ** i)
        return result

    @classmethod
    def dec_to_any(cls, number, base):
        """
        Convert a number from decimal to any base
        :param number:
        :param base:
        :return: The decimal number as a number from base X
        """
        assert 2 <= base <= 36, 'Wrong base'
        assert isinstance(number, int) or number.isnumeric(), 'Parameter 1 must be an int or a value of int'
        result_str = ''
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if number == 0:
            return '0'
        while number != 0:
                remainder = number % base
                number = number // base

                if 10 <= remainder <= 36:  # if remainders value is a letter
                    result_str = alphabet[remainder-10] + result_str  # DO NOT ATTEMPT to use +=. It creates a bug
                else:
                    result_str = str(remainder) + result_str  # DO NOT ATTEMPT to use +=. It creates a bug
        return result_str

    @classmethod
    def any_to_any(cls, number_from, base_from, base_to):
        """
        Convert a number from a base to another base
        :param number_from:
        :param base_from:
        :param base_to:
        :return:
        """
        return cls.dec_to_any(cls.any_to_dec(number_from, base_from), base_to)
