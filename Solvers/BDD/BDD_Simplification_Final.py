class BDDSimplification:

    def __init__(self):
        pass

    def double_variable_simplification(self, function_list):  # receives a list, returns a string of new function

        function_length = len(function_list)

        for i in range(function_length):  # for each term
            temp = set(function_list[i])  # make the term a set, removing double elements
            function_list[i] = "".join(temp)  # recreate the term as a string

        return function_list  # return the corrected list

    def same_var_or(self, function):

        function_length = len(function)
        seen = {}
        new_list = [seen.setdefault(x, x) for x in function if x not in seen and x != '0' and x != '1']

        return new_list

    def same_var_and(self, function):

        function_length = len(function)
        for i in range(function_length):
            temp = set(function[i])
            if function_length !=1:
                function[i] = "".join(temp)

        return function

    def and_simplification(self, function):
        #  this code part simplifies expressions like xx' and x'zx, which always return 0
        function_length = len(function)

        if function_length != 1:
            snext = ''
            snow = ''
            for i in range(function_length):
                term_length = len(function[i])
                for j in range(term_length):
                    if j == term_length - 1:
                        snext = function[i][j]
                        snow = function[i][j]
                        # if snow == '0':
                            # function[i] = ""
                    else:
                        snext = function[i][j + 1]
                        snow = function[i][j]
                        if snow.isupper():  # or snow.isnumeric():
                            if snext.upper() == snow:  # or snow == '0':
                                function[i] = ""
                                break
                            else:
                                continue
                        elif snow.islower():  # or snow.isnumeric():
                            if snext.lower() == snow:  # or snow == '0':
                                function[i] = ""
                                break
                            else:
                                continue

            while "" in function:
                function.remove("")
        return function

    def term_with_1(self,function):
        function_length = len(function)
        for i in range(function_length):
            if '1' in function[i] and len(function[i]) != 1:
                function[i] = function[i].replace('1', '')
            elif function[i] == "1":
                function = ['1']
                break
        return function

    # this code removes any 0, i need to make not to remove 0 standalone
    def remove_0_terms(self,function_list):
        for i in range(len(function_list)):
            if function_list != ['0']:
                if '0' in function_list[i] and function_list[i] != ['0']:
                    function_list[i] = ""
                else:
                    continue
            else:
                continue
        while "" in function_list:
            function_list.remove("")
        return function_list



