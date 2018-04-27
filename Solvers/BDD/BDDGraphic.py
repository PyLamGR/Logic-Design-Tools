from graphviz import Digraph
from graphviz import Graph
import functools
import pydot
import os
import copy

class BDDGraph:

    def __init__(self, result):
        self.result = copy.copy(result)

    def bdd_graph(self):
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'  # must be in every program
        path = 'C:/Users/Aris/Desktop/BDDs/example.gv'
        test_diagram = copy.copy(self.result)
        keys = list(test_diagram)
        functions = []
        #now I must separate the values
        for i in range(len(test_diagram)):
            functions.append(test_diagram[keys[i]])
        del test_diagram['Initial Function']
        bddG = Digraph(comment='Binary Decision Diagram', format='png')
        # I need a list of keys
        keys = list(test_diagram)
        bddG.node('0', shape='square')  # fixed nodes
        bddG.node('1', shape='square')  # fixed nodes)
        # I will try removing the double functions from the function lists
        i = 1
        for j in functions[1:]:
            functions[i] = list(sorted(set(j)))
            i += 1
        safe = '0'
        count = 2
        sp_index_list = {}
        for i in range(len(keys)):
            for j in range(len(functions[i])):
                if keys[i] in functions[i][j] or keys[i].upper() in functions[i][j]:
                    if safe != functions[i]:
                        count += 1
                        print(functions[i])
                        sp_index_list[str(count)] = keys[i]
                        bddG.node(str(count), keys[i], shape='circle')
            safe = functions[i]

        print(sp_index_list)
        print(count)

        # the elements of sp_index_list refer to the nodes that will be used
        # now I must make a code part where nodes, keys and functions can manage to communicate and connect together
        # initially, I must choose the dominant loop. Is the creation of the bdd based on functions, keys or nodes?
        # basically, we can say that the bdd's design is based in number of nodes, but the connections is based in the functions
        # so...
        functions_for_0 = list()
        functions_for_1 = list()
        for i in range(len(functions)):
            if i == 0:
                continue
            for j in range(len(functions[j])):
                if j % 2 == 0:
                    functions_for_0.append(functions[i][j])
                elif j % 2 != 0:
                    functions_for_1.append(functions[i][j])
        flag = True
        i = 1
        j = 0
        k = 1
        while flag:
            if keys[i] in functions_for_0[j]:
                bddG.edge(list(sp_index_list)[k-1],list(sp_index_list)[k])

            if keys[i] in functions_for_1[j]:
                bddG.edge(list(sp_index_list)[k-1],list(sp_index_list)[k])
                print("l")

            j += 1
            if j == len(functions_for_0):
                flag = False




        bddG.render(view=True)

# driver code

result = {'Initial Function': 'Xy+z', 'x': ['y+z', 'z'], 'y': ['z', '1', 'z', 'z'], 'z': ['0', '1', '1', '1', '0', '1', '0', '1']}
graph = BDDGraph(result)
graph.bdd_graph()



