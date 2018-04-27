def go_right(lst, i, j):
    try: return i, j+1, lst[i][j+1]
    except IndexError: return i, 0, lst[i][0]


def go_left(lst, i, j):
    return i, (j-1 if j != 0 else len(lst[i])-1), lst[i][j-1]


def go_up(lst, i, j):
    return (i-1 if i != 0 else len(lst)-1), j, lst[i-1][j]


def go_down(lst, i, j):
    try: return i+1, j, lst[i+1][j]
    except IndexError: return 0, j, lst[0][j]


def is_subset(lsa, lsb):  # Is lsb subset of lsa? Alternate: not set.isdisjoint()
    for b in lsb:
        if b in lsa: continue
        else: return False
    return True