import copy
import string


class QuineMcV3:


    def __init__(self, array_of_min_terms, array_of_dc_terms):
        self.complete_array_of_min_terms = (array_of_min_terms + array_of_dc_terms)
        self.array_of_min_terms = array_of_min_terms

        self.table_dict = {}
        self.next_table = {}
        self.tmplist = {}
        self.final_list = []
        self.mega_table = []
        self.bin_array_of_min_terms = []
        self.translated_version = []


        self.number_of_ones = 0
        self.temporery_list = []

        templist = [int(x) for x in self.complete_array_of_min_terms]
        self.max_number_of_digits = len(list(bin(max(templist))[2:]))


    def sort_first_list(self):
        for i in range(len(self.complete_array_of_min_terms)):
            self.number_of_ones = bin(int(self.complete_array_of_min_terms[i])).count("1")

            templist = self.table_dict.get(self.number_of_ones, [])

            templist.append(bin(int(self.complete_array_of_min_terms[i]))[2:].zfill(self.max_number_of_digits))

            self.table_dict[self.number_of_ones] = templist

            self.table_dict.get(self.number_of_ones).sort()

            self.number_of_ones = 0

        # print(self.table_dict)
        # print(len(self.table_dict))

        for i in list(self.array_of_min_terms):
            self.bin_array_of_min_terms.append(bin(int(i))[2:].zfill(self.max_number_of_digits))
        self.bin_array_of_min_terms.sort()
        print(self.bin_array_of_min_terms)

        for h in range(self.max_number_of_digits-1):

            self.create_temp_list()

            self.get_last_list()

        self.final_list = copy.deepcopy(self.temporery_list)

        # print("final table: " + str(self.final_list))

    def count_differences(self, input1, input2):
        count = 0
        position = 0
        final_position = 0

        for number_x, number_y in zip(input1, input2):
            if str(number_x) != str(number_y):
                count += 1
                final_position = position
            position += 1

        return (count, final_position)

    def create_temp_list(self):
        for i in list(self.table_dict.values()):
            for j in range(len(i)):
                self.temporery_list.append(i[j])

    def get_last_list(self):
        loop_range = (len(self.table_dict) - 1)
        if '0' not in self.complete_array_of_min_terms:
            loop_range += 1

        for i in range(loop_range):
            # print("i: " + str(self.table_dict.get(i)))
            # print("i+1: " + str(self.table_dict.get(i + 1)))

            if self.table_dict.get(i) is None:
                # print("The First one was empty")
                continue

            else:
                for x in self.table_dict.get(i):
                    for y in self.table_dict.get(i + 1):

                        count, final_position = self.count_differences(x, y)

                        if count == 1:

                            if x in self.temporery_list:
                                self.temporery_list.remove(x)

                            if y in self.temporery_list:
                                self.temporery_list.remove(y)

                            y = list(y)
                            y[final_position] = '-'
                            y = ''.join(y)

                            self.tmplist = self.next_table.get(i, [])

                            if y not in self.tmplist:
                                self.tmplist.append(y)

                            # print(self.tmplist)

                            self.next_table[i] = (self.tmplist)

                            # print("next table: " + str(self.next_table))

        self.mega_table.append(self.table_dict)

        self.table_dict = copy.deepcopy(self.next_table)

        self.next_table.clear()

    def final_step(self):
        self.letters = self.generate_letters()

        self.final_char_min_terms = self.generate_char_min_terms(self.final_list, self.letters)

        self.starting_char_min_terms = self.generate_char_min_terms(self.bin_array_of_min_terms, self.letters)

        self.final_table_of_min_terms = self.compare_chars(self.starting_char_min_terms, self.final_char_min_terms)

        self.shortened_version = self.create_shortened_version(self.final_table_of_min_terms)

        self.translated_version = self.translate_result(self.shortened_version)

        print(self.mega_table)
        print(self.final_list)

        print(self.final_char_min_terms)
        print(self.final_table_of_min_terms)

        print(self.shortened_version)



    def generate_letters(self):
        letters = []
        for i in range(self.max_number_of_digits):
            letters.append(string.ascii_lowercase[i])
        return letters

    def generate_char_min_terms(self, list, letters):
        char_minterms = []
        for i in list:
            term = ''
            letter_pos = -1
            for j in i:
                letter_pos += 1
                if j == '0':
                    term += str(letters[letter_pos]).upper()
                    # term += "'"
                elif j == '1':
                    term += str(letters[letter_pos])
                elif j == '-':
                    continue
            char_minterms.append(term)
        return char_minterms

    def compare_chars(self, starting_min_terms, final_min_terms):
        temp_list_of_min_terms = [['#', starting_min_terms[0]], [final_min_terms[0]]]

        for h in range(len(final_min_terms)):
            if h != 0:
                temp_list_of_min_terms.append([])
                temp_list_of_min_terms[h+1].append(final_min_terms[h])
            else:
                continue

        for w in range(len(starting_min_terms)):
            if w != 0:
                temp_list_of_min_terms[0].append(starting_min_terms[w])
            else:
                continue

        for x in range(1, len(temp_list_of_min_terms)):
            for y in range(1, len(temp_list_of_min_terms[0])):
                count = 0
                for h in list(temp_list_of_min_terms[x][0]):
                    for j in list(list(temp_list_of_min_terms[0][y])):
                        if h == j:
                            count += 1
                if count == len(temp_list_of_min_terms[x][0]):
                    temp_list_of_min_terms[x].insert(y, 'x')
                else:
                    temp_list_of_min_terms[x].insert(y, '-')


        return temp_list_of_min_terms

    def create_shortened_version(self, final_table_of_min_terms):
        temp_list_of_min_terms = final_table_of_min_terms
        temp_list_of_min_terms.append(['#'])
        shortened_version = []

        for x in range(1, len(temp_list_of_min_terms[0])):
            temp_list_of_min_terms[len(temp_list_of_min_terms) - 1].append('*')

        while '*' in temp_list_of_min_terms[len(temp_list_of_min_terms) - 1]:
            for x in range(1, len(temp_list_of_min_terms[0])):
                count = 0
                position = 0
                max_count = 2
                for y in range(1, len(temp_list_of_min_terms)):

                    if temp_list_of_min_terms[y][x] == 'x':
                        count += 1
                        position = y

                if count > max_count:
                    max_count = count

                if count == 1:
                    shortened_version += self.add_shortened_minterm(temp_list_of_min_terms, position)

                elif count == max_count:
                    shortened_version += self.add_shortened_minterm(temp_list_of_min_terms, position)

            shortened_version = list(set(shortened_version))

        return shortened_version

    def add_shortened_minterm(self,list, position):
        self.temp_shortened_version = []
        for i in range(1, len(list[position])):
            if list[position][i] == 'x':
                list[len(list) - 1][i] = '+'
        if list[position][0] not in self.temp_shortened_version:
            self.temp_shortened_version.append(list[position][0])

        return self.temp_shortened_version

    def translate_result(self, shortened_version):
        for i in range(len(shortened_version)):
            shortened_version[i] = list(shortened_version[i])
            for y in range(len(shortened_version[i])):
                if shortened_version[i][y].isupper():
                    shortened_version[i][y] = shortened_version[i][y].lower() + "'"
            shortened_version[i] = "".join(shortened_version[i])
        shortened_version = "+".join(shortened_version)


        return shortened_version