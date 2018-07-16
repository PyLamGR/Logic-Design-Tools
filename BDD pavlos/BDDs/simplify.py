# functions for basic simplification of a boolean function


def simplify_0(string):

    string = string.replace(' + ', '_')
    s = string.split('_')

    for i in range(len(s)):
        if '0' in s[i]:

            # changed it from remove the element(s.remove(s[i])) to replacing it with 0
            s[i] = "0"

    for i in range(len(s)):
        s[i] += " + "

    index = len(s) - 1
    s[index] = s[index].replace(" + ", "")

    string = "".join(s)

    return string


def simplify_1(string):

    s = string.split(' + ')

    for i in range(len(s)):
        if s[i] == "1":
            string = "1"
            return string

    for i in range(len(s)):
        s[i] = s[i].replace('1', '')

    for i in range(len(s)):
        s[i] += " + "

    index = len(s) - 1
    s[index] = s[index].replace(" + ", "")
    string = "".join(s)

    return string


def replace_complement(string):
    s = string.split(' + ')

    for i in range(len(s)):
        if "'" in s[i]:
            hold = list(s[i])

            for j in range(len(hold)):
                if hold[j] == "'":
                    hold[j] = ""
                    hold[j - 1] = hold[j - 1].upper()

            s[i] = "".join(hold)

    for i in range(len(s) - 1):
        if i != len(s):
            s[i] += " + "

    string = "".join(s)

    return string


def same_var_or(string):

    s = string.split(' + ')

    for i in range(len(s) - 1):
        count = s.count(s[i])
        if count > 1:
            s.remove(s[i])

    for i in range(len(s)):
        if i != len(s) - 1:
            s[i] += " + "
    string = "".join(s)

    return string


def same_var_and(string):

    s = string.split(' + ')

    for i in range(len(s)):
        length = len(s[i])
        sub_string = s[i]
        count_same = 0
        # check for same chars
        for j in range(length):
            for k in range(length):
                if j == k:
                    continue
                else:
                    if sub_string[k] is sub_string[j]:
                        count_same += 1

        if count_same > 0:
            hold = list(s[i])

            for j in range(len(hold) - 1):
                count = hold.count(hold[j])
                if count > 1:
                    hold.remove(hold[j])

            s[i] = "".join(hold)

    for i in range(len(s)):
        if i != len(s) - 1:
            s[i] += " + "

    string = "".join(s)

    return string


def simplify_complement_or(string):
    string = replace_complement(string)

    s = string.split(" + ")

    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            else:
                if len(s[i]) > 1:
                    continue
                else:
                    s[i] = s[i].upper()

                    if s[j] == s[i]:
                        s[j] = ""
                        s[i] = "1"
                    else:
                        s[i] = s[i].lower()

    new_s = []

    for i in range(len(s)):
        if s[i] == "":
            continue
        else:
            new_s.append(s[i])

    for i in range(len(new_s)):
        if i != len(new_s) - 1:
            new_s[i] += " + "

    string = "".join(new_s)

    return string


def simplify_complement_and(string):
    string = replace_complement(string)

    s = string.split(" + ")

    for i in range(len(s)):

        hold = list(s[i])

        for j in range(len(hold)):
            for k in range(len(hold)):
                if j == k:
                    continue
                else:
                    hold[j] = hold[j].upper()

                    if hold[k] == hold[j]:
                        hold[k] = ""
                        hold[j] = "0"
                    else:
                        hold[j] = hold[j].lower()
        new_hold = []

        for j in range(len(hold)):
            if hold[j] == "":
                continue
            else:
                new_hold.append(hold[j])

        s[i] = "".join(new_hold)

    for i in range(len(s) - 1):
        if i != len(s) - 1:
            s[i] += " + "

    string = "".join(s)

    return string
