import simplify

# contains functions for building each step of the BDD


def simplify_all(string):

    # 10 simplifications just in case
    for i in range(10):
        string = simplify.replace_complement(string)
        string = simplify.same_var_and(string)
        string = simplify.same_var_or(string)

        string = simplify.simplify_complement_or(string)
        string = simplify.same_var_and(string)
        string = simplify.same_var_or(string)

        string = simplify.simplify_complement_and(string)
        string = simplify.same_var_and(string)
        string = simplify.same_var_or(string)

        string = simplify.simplify_0(string)
        string = simplify.simplify_1(string)
        string = simplify.same_var_and(string)
        string = simplify.same_var_or(string)

    return string


def put_0(string, var):

    variable = str(var)

    string = string.replace(variable, "0")
    string = string.replace(variable.upper(), "1")

    return string


def put_1(string, var):

    variable = str(var)

    string = string.replace(variable, "1")
    string = string.replace(variable.upper(), "0")

    return string


# use these two for each loop in the sequence list
def build_0(string, var):

    string = put_0(string, var)

    string = simplify_all(string)

    return string


def build_1(string, var):

    string = put_1(string, var)

    string = simplify_all(string)

    return string
