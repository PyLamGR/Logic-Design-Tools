import copy

from Solvers.BDD.BDD_Simplification_Final import BDDSimplification


class BDD:

    def __init__(self):

        self.num = None
        self.order = None
        self.function = None

        self.result = {}

    def main(self):

        self.order = self.order.replace(" ", "")
        self.order = self.order.lower()
        self.order_list = self.order_generator(self.order)
        self.validity_number_checker = self.check_number_of_vars(len(self.order_list), self.num)


        self.function = self.function.replace(" ", "")
        self.function = self.function.lower()
        self.function_list = self.list_generator(self.function)
        self.validity_checker = self.check_vars(self.order_list, self.function_list)


        for i in range(len(self.function_list)):
            print(self.function_list[i])
            self.function_list[i] = self.generate_reversals(self.function_list[i])

        """ from down here code is just for debugging"""
        print(self.function_list)
        print(self.order_list)
        self.function = self.generate_func_from_list(self.function_list)

        # code part admitted by Aris Karabelas Timotijevic
        simplificator = BDDSimplification()
        # checking the function with the additional checks
        # 1. removing double characters in the same term
        self.function = simplificator.double_variable_simplification(self.function_list)
        self.function_list = simplificator.same_var_or(self.function_list)
        self.function_list = simplificator.same_var_and(self.function_list)
        self.function_list = simplificator.and_simplification(self.function_list)
        self.function_list = simplificator.remove_0_terms(self.function_list)
        self.function_list = simplificator.term_with_1(self.function_list)
        self.function = self.generate_func_from_list(self.function_list)
        self.result = self.bdd_simplification(self.function, self.order_list, self.function_list)

    def list_generator(self, string):
        alist = []
        if len(string) != 1:
            pos = 0
            j = 0
            for i in range(len(string)):
                if ord(string[i]) == 43:
                    pos = i
                    alist.append(string[j:pos])
                    j = i+1
            alist.append(string[pos+1:])
            if len(alist) == 1:
                alist[0] = string[0] + alist[0]
        else:
            alist.append(string)
        return alist

    def order_generator(self, string):
        alist = []
        pos = 0
        j = 0
        flag = True
        for i in range(len(string)):
            if ord(string[i]) == 60 or ord(string[i]) == 62:
                if ord(string[i]) == 62:
                    flag = False
                pos = i
                alist.append(string[j:pos])
                j = i+1
        alist.append(string[pos+1:])
        if flag is False:
            alist.reverse()
        return alist

    def check_vars(self, olist, flist):  # checking the variable , according to order etc.
                                        # x<y<z so f must be of form f(x,y,z)
        flag = False
        '''counter = 0

         for i in range(len(olist)):
            for j in range(len(flist)):

                if olist[i] in flist[j]:
                    counter += 1
                


        if counter < 100:
            flag = True'''

        return True



    def check_number_of_vars(self, num1, num2):  # checking the number of variables
                                                # in order to match the one of the order
        flag = True
        if num1 != num2:
            flag = False
        return flag

    def generate_reversals(self, string):
        result = ''
        snext = ''
        snow = ''
        for i in range(len(string)):
            if i == len(string)-1:
                snext = string[i]
                snow = string[i]
            else:
                snext = string[i+1]
                snow = string[i]
            if ord(snow) == 39:
                continue
            elif ord(snext) == 39:
                result += str(snow).upper()
            else:
                result += str(snow)
            result.replace("'", '')
        return result

    def generate_func_from_list(self, flist):
        if len(flist) != 1:
            result = "+".join(flist)
        else:
            result = flist[0]
        return result

        # and now the main code for BDD simplification

    def bdd_simplification(self, function, order_list, function_list):
        simplificator = BDDSimplification()
        function_for_0 = function_list
        function_for_1 = function_list
        func_collection = list()
        func_collection.append(function)
        tmp_list = list()
        tmp_list.append(function)
        phases = dict()
        phases["Initial Function"] = func_collection[0]  # the first element of the phases
        order_length = len(order_list)
        function_length = len(function_list)
        for i in range(order_length):  # for each variable which appears in the function
            # print("order: " + order_list[i])
            # print(tmp_list)
            for_loops = copy.copy(func_collection)
            tmp_list.clear()
            for j in range(len(for_loops)):  # for each function from the previous step
                safe_function = for_loops[j]
                # print("safe function: ")
                # print(safe_function)
                if order_list[i] in for_loops[j] or order_list[i].upper() in for_loops[j]:
                    # print("Function: "+str(for_loops[j]))

                    function_for_0 = for_loops[j].replace(order_list[i], '0')
                    function_for_0 = function_for_0.replace(order_list[i].upper(), '1')

                    temp_function = self.list_generator(function_for_0)

                    temp_function = simplificator.and_simplification(temp_function)
                    temp_function = simplificator.remove_0_terms(temp_function)
                    temp_function = simplificator.term_with_1(temp_function)
                    temp_function = simplificator.same_var_and(temp_function)
                    function_for_0 = self.generate_func_from_list(temp_function)

                    function_for_1 = for_loops[j].replace(order_list[i], '1')
                    function_for_1 = function_for_1.replace(order_list[i].upper(), '0')

                    temp_function = self.list_generator(function_for_1)

                    temp_function = simplificator.and_simplification(temp_function)
                    temp_function = simplificator.remove_0_terms(temp_function)
                    temp_function = simplificator.term_with_1(temp_function)
                    try:
                        temp_function = simplificator.same_var_and(temp_function)
                    except:
                        print("End Value [1]")

                    function_for_1 = self.generate_func_from_list(temp_function)
                    # print("function for zero: "+str(function_for_0))
                    # print("function for one: "+str(function_for_1))
                    tmp_list.append(function_for_0)
                    tmp_list.append(function_for_1)
                    func_collection = copy.copy(tmp_list)
                    for k in range(len(func_collection)):
                        if func_collection[k] == '':
                            func_collection[k] = '0'
                        for n in range(len(func_collection[k])):
                            if func_collection[k][n] == '':
                                func_collection[k][n] = '0'
                    phases[order_list[i]] = func_collection
                else:
                # elif order_list[i] not in func_collection[j] or order_list[i].upper() not in func_collection[j]:
                    function_for_0 = safe_function
                    function_for_1 = safe_function
                    tmp_list.append(function_for_0)
                    tmp_list.append(function_for_1)
                    func_collection = copy.copy(tmp_list)
                    phases[order_list[i]] = func_collection
                    continue
        # print("=============END===============")
        # print(tmp_list)
        # print(phases)
        return phases



    def validityForNumbers(self, order):
        self.order = order
        self.order = self.order.replace(" ", "")
        self.order = self.order.lower()
        self.order_list = self.order_generator(self.order)
        self.validity_number_checker = self.check_number_of_vars(len(self.order_list), self.num)
        return self.validity_number_checker





    def validityChecker(self, function):

        self.function = function
        self.function = self.function.replace(" ", "")
        self.function = self.function.lower()
        function_list = self.list_generator(self.function)

        self.validity_checker = self.check_vars(self.order_list, function_list)
        return self.validity_checker






if __name__ == '__main__':
    b = BDD()
    
    x = int(input("vars: "))
    y = input("order: ")
    z = input("function: ")

    b.num = x
    b.order = y
    b.function = z

    b.main()
    print(b.result)





