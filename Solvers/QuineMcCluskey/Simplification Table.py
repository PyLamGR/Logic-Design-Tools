import string


class Simplification_table:
    def __init__(self):  # inputs will come in here
        pass

        # taking the users input, making it list so i can compare the numbers
        # to the dictionary keys, the string will come in by reading the table

        # Not ready

    # the table maker below wont do , i ll think of sth else , i ll have to do separate lists

    def table_of_minterms_maker(self, string, list_of_str_len, mint):
        table_list_horizontal_up = []
        table_list_horizontal_up.append('')
        for i in range(list_of_str_len):
            table_list_horizontal_up.append(string[i])
        table_list_horizontal_up = ['m' + i for i in table_list_horizontal_up]  # decoration of minterms , adding m
        table_list_horizontal_up[0] = None

        table_list_vertical = []
        table_list_vertical.append(None)
        for i in range(len(mint)):
            table_list_vertical.append(mint[i])

        table_x = []
        table_ticks = []
        for i in range(len(table_list_horizontal_up)):
            if i == 0 :
                continue
            else:
                table_ticks.append('')
            for j in range(len(table_list_vertical)):
                if i == 0 or j == 0:
                    continue
                else:
                    table_x.append('')

        # for debugging
        print(table_list_horizontal_up)
        print(table_list_vertical)
        self.table_results_x_printer(table_x)
        print(table_ticks)
        return


# generating letters according to length of binary strings etc. 001-0 --> a-e letters

    def generate_letters(self, dictionary):
        values_list = list(dict(dictionary).values())
        num_to_gen = len(values_list[0])
        letters = []
        for i in range(num_to_gen):
            letters.append(string.ascii_lowercase[i])
        return letters

# generating minterms by using letters etc 0-11 --> a'cd , skipping b cause its '-'

    def generate_minterms(self, dictionary, letters):
        values_list = list(dict(dictionary).values())
        minterms = []
        term = ''
        for i in range(len(values_list)):
            letter_pos = -1
            for j in values_list[i]:
                letter_pos += 1
                if j == '0':
                    term += str(letters[letter_pos])
                    term += "'"
                elif j == '1':
                    term += str(letters[letter_pos])
                elif j == '-':
                    continue
            minterms.append(term)
        return minterms

    def table_results_x_printer(self, table):
        j = 0
        if len(table) % 2 == 0:
            j = len(table)//2
        else:
            j = len(table)//2 - 1
        print(table[:j])
        print(table[j:])
        return

    def generate_x_in_table(self, table_x, binterms_dic, vtable):
        list_of_keys = dict(binterms_dic).keys()
        list_of_keys = list(list_of_keys)
        list_of_terms = dict(binterms_dic).values()
        list_of_terms = list(list_of_terms)
        # i need to check the format of strings if they are like "'a','b'" or 'ab'
        # so i need to make to functions to reanable them

        # for i in range(len(list_of_terms)):
        #     binary_num = bin(int(list_of_terms[i]))
        #     del list_of_terms[i]
        #     list_of_terms[i] = binary_num

        list_of_terms_in_letters = self.generate_letters(binterms_dic)
        return

    def generate_binaries_from_strings(self, list_of_terms):
        temp = 0
        for i in range(len(list_of_terms)):
            try:
                temp = int(list_of_terms[i])
                return temp
            except ValueError:
                return False
        return

# debug code , will be deleted


def line():
    print('----------------------------------------')

example = Simplification_table()
etc = ['0', '1', '2', '3', '4', '5', '15']
minterms = {'4 , 8, 15 , 12, 30': '010--0010',
            '15, 25, 35, 60': '010---010'}
example.table_of_minterms_maker(etc, len(etc),
                                example.generate_minterms(minterms,
                                example.generate_letters(minterms)))
line()

