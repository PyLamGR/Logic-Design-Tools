from .BaseConverter import *

from Solvers.helper import check_base


class ArithmeticExpression:

    @classmethod
    def get_expression(cls, number, base_from, base_to=-1):
        """
        Get the expression of a numer at a give base.
        :param number:
        :param base_from:
        :param base_to:
        :return:
        """
        base_to = base_from if base_to is -1 else base_to  # Ternary Operator

        assert 2 <= base_from <= 36, 'Invalid base'
        assert 2 <= base_to <= 36, 'Invalid base'
        assert check_base(number, base_from), 'Invalid number'

        if not check_base(number, base_from):
            return None

        tmp = list(BaseConverter.any_to_any(number, base_from, base_to))
        
        result_str = ''
        expression = []

        length = len(tmp)
        for i in range(length):
            expression.append('{0}*{1}^{2}'.format(tmp[i], base_to, length-i-1))
            result_str = result_str + "+" + expression[i]

        tmp = list(result_str)
        del tmp[0]
        result_str = ''.join(tmp)  # List to String
        return result_str

