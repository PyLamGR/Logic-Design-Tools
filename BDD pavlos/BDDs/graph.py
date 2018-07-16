import matplotlib.pyplot as plt
import networkx as nx
import bdd_seq_logic as bdd


# NEED TO TWEAK THE POSITIONING X ALGORITHM SO THAT THE NODES DO NOT FALL ONTO EACHOTHER

# generates a list of final binaries
def create_final_bin_list(seq, string):

    graph_list = list()

    graph_list.append(([seq[0]]))
    for i in range(1, len(seq)):
        graph_list.append([seq[i], seq[i]])

    graph_list.append(bdd.get_func_results(bdd.build(seq, string)))

    results = graph_list[len(graph_list) - 1]

    # if you were to create a full tuple list for edges if the BDD was simplified
    # final_graph_list = list()
    # create list without final binaries
    # branch = 1
    # for i in range(len(seq) - 1):
    #
    #    branch *= 2
    #
    #    for j in range(branch):
    #        final_graph_list.append(tuple([seq[i], seq[i + 1]]))

    # add final binaries to final_graph_list
    # for i in range(len(results)):
    #     final_graph_list.append(tuple([seq[len(seq) - 1], results[i]]))
    # NEED TO ADD NUMBERS TO EACH VARIABLE WITH str(variable) + str(number)
    # SO THAT THE GRAPH RECOGNISES IT
    # final_graph_list is the final list with tuples to represent the edges of the graph

    return results


# not simplified
# used for graph
def create_new_seq(seq):

    # create new seq list that gives indexes to variables( [a, b, c] would be [a, b1, b2, c1, c2, c3, c4])
    new_seq = list()
    new_seq.append(seq[0])

    branch = 1
    for i in range(1, len(seq)):
        branch *= 2
        for j in range(branch):
            new_seq.append(seq[i] + str(j + 1))

    # new_seq is used as nodes list for nx graph
    return new_seq


# create edges tuples
# need to modify generate_graph to work with new_seq
def create_edges(seq, new_seq, string):
    # make it check indexes and variable names to avoid confusion
    # matches all variables with indexes from new_seq to final binaries in initial seq
    # branches is the number that represents how many variables with the same name(but different index) exist
    # that helps with matching the binaries
    branches = 1
    for i in range(len(new_seq)-1, 1, -1):

        if str(new_seq[i][0]) != str(new_seq[i-1][0]):
            break
        else:
            branches += 1

    # 'c1', 'c2', 'c3', 'c4' --> '0', '1', '0', '1', '0', '1', '1', '1'
    # need to create a new_results list of tuples to create the new edges
    results = create_final_bin_list(seq, string)

    # this loop creates the list of tuples that will be used as edges
    edge_list = list()

    for i in range(len(new_seq) - branches):
        for j in range(2*i + 1, 2*i + 3):
            edge_list.append(tuple([new_seq[i], new_seq[j]]))

    # need to add binaries to final (branches(number of tuples)) variables
    for i in range(len(new_seq) - branches, len(new_seq)):
        for j in range(2*(i-branches) + 1, 2*(i-branches) + 3):
            edge_list.append(tuple([new_seq[i], results[j]]))

    return edge_list


# print("\n")
# print(create_edges(["a", "b", "c", "d"], create_new_seq(["a", "b", "c", "d"]), "ab + c + d"))


def create_positioning(seq):

    new_seq = create_new_seq(seq)
    pos = {}

    list_x = list()
    list_y = list()

    # for list y
    y = 100
    dec_y = 100/3
    list_y.append(y)
    for i in range(len(seq) - 1):
        y -= dec_y
        list_y.append(y)

    # for list x
    list_x.append(100)
    branch = 1
    temp = list()
    list_x.append([list_x[0] - (list_x[0]/2), list_x[0] + (list_x[0]/2)])

    # middle nodes are placed onto each other
    for i in range(1, len(seq)):
        branch *= 2
        for j in range(branch):
            temp.append(list_x[i][j] - 10)
            temp.append(list_x[i][j] + 10)

        list_x.append(temp)
        temp = []

    # pos.update({...: ...}) appends to dictionary
    # create pos
    pos.update({str(new_seq[0]): tuple([str(list_x[0]), str(list_y[0])])})

    branch = 1
    coord = [(int(100), int(100))]
    for i in range(1, len(seq)):
        y = list_y[i]

        branch *= 2
        for j in range(branch):

            x = list_x[i][j]

            coord.append(tuple([x, y]))

    for i in range(1, len(new_seq)):
        pos.update({str(new_seq[i]): coord[i]})

    # need to add binaries positions
    pos.update({"0": (95, list_y[len(list_y)-1] - 100),
                "1": (105, list_y[len(list_y)-1] - 100)
                })

    pos["a"] = (100, 100)

    return pos


def create_labels(edge_list):

    labels = dict()

    for i in range(len(edge_list)):
        if i % 2 == 0:
            labels.update({edge_list[i]: '0'})
        elif i % 2 != 0:
            labels.update({edge_list[i]: '1'})

    return labels


# GUI NEEDS TO CALL ONLY THIS FUNCTION AFTER IMPORTING JUST THIS MODULE

# seq is a list of the variables sequence
# string is the function
# both parameters are given by the user
def generate_graph(seq, string):

    g = nx.DiGraph()

    new_seq = create_new_seq(seq)
    g.add_nodes_from(new_seq)

    pos = create_positioning(seq)

    edges_list = create_edges(seq, new_seq, string)

    labels = create_labels(edges_list)

    # save data to file
    file = open('data.txt', 'w')
    text1 = str(new_seq)
    text2 = str(pos)
    text3 = str(edges_list)
    text4 = str(labels)
    line_feed = "\n"
    file.write("new_seq")
    file.write(text1)
    file.write(line_feed)
    file.write("pos")
    file.write(text2)
    file.write(line_feed)
    file.write("edges_list")
    file.write(text3)
    file.write(line_feed)
    file.write("labels")
    file.write(text4)
    file.write(line_feed)

    file.close()

    # make graph
    g.add_edges_from(edges_list)

    edge_labels = nx.draw_networkx_edge_labels(g, pos, labels)
    #  DOES NOT WORK BECAUSE OF MODULE ERROR
    nx.draw(g, pos, with_labels=True)
    #  DOESN'T WORK WITH THIS POS....gives ERROR from the module not my program
    # nx.draw_circular(g, with_labels=True)
    plt.savefig('bdd_graph.png')
    # plt.show()
    # does not save as .jpg


generate_graph(["a", "b", "c", "d"], "ab + c + d")

