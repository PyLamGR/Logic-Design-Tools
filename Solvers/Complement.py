from Solvers.helper import *


class Complement:
    def __init__(self, base):
        assert 1 < base <= 10, language('Error.Base')
        self.base = base



    def base_compliment(self, number):
        """
        Returns the complement of a number in a given base
        :param number:
        :return: Base complement
        """
        assert check_base(number, self.base), 'Number doesn\'t belong in base'
        number = self.reduced_base_compliment(number) + 1
        return number

    def reduced_base_compliment(self, number):
        """
        Returns the reduced base complement of a number in a base
        :param number:
        :return: Reduced base complement
        """
        assert check_base(number, self.base), "Number doesn't belong in base"
        digits = len(str(number))
        if self.base == 10:
            final_base = self.base ** digits
        else:
            final_base = str(str(self.base - 1) * digits)

        number = int(final_base) - number
        return number
