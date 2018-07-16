import test_simplify

# string is function
# seq is a list of variables sequence
# creates the functions of each BDD node and gives the final binaries of each unsimplified BDD node


def build(seq, string):

    # write sequence to .txt file
    text = ""
    for i in range(len(seq)):
        var = str(seq[i]) + "\n"
        text += var
    f = open('sequence.txt', 'w')

    f.write(text)
    f.close()

    function_collection = list()

    func_list = list()

    # first element that cannot be edited in loop
    function_collection.append(string)

    branch = 1

    for i in range(1, len(seq) + 1):

        branch *= 2

        for j in range(branch):

            if branch == 2:
                if j == 0:
                    func_list.append(test_simplify.build_0(function_collection[0], seq[i-1]))
                elif j == 1:
                    func_list.append(test_simplify.build_1(function_collection[0], seq[i-1]))
            else:
                index = int(j/2)
                if j % 2 == 0:
                    func_list.append(test_simplify.build_0(function_collection[i-1][index], seq[i-1]))
                elif j % 2 != 0:
                    func_list.append(test_simplify.build_1(function_collection[i-1][index], seq[i-1]))

        function_collection.append(func_list)
        func_list = []

    return function_collection


# returns only the final results (0s and 1s) of each branch
# NOT SIMPLIFIED
def get_func_results(func_col):

    final_result = func_col[len(func_col) - 1]

    text = ""
    f = open('binary_results.txt', 'w')

    for i in range(len(final_result)):
        text += str(final_result[i]) + "\n"

    f.write(text)
    f.close()

    return final_result
