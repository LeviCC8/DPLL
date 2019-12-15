import numpy as np
from sklearn import tree
from sklearn.tree._tree import TREE_UNDEFINED
from DPLL import DPPL
from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution

pacients = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_header=2)

pacients_input = pacients[1:, :-1]
pacients_output = pacients[1:, -1]
#thresholds = pacients[0, :-1]

#attributes = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_footer=157, dtype=str)

test = np.genfromtxt('data/column_bin_test.csv', delimiter=',', skip_header=2)
test_input = test[1:, :-1]
test_output = test[1:, -1]

M = 6

def find_rules(tree):
    dt = tree.tree_
    rules = []
    return rules + [find_rules(0, 1, dt)]

def find_rules(node, depth, dt, rules):
    if dt.feature[node] != TREE_UNDEFINED:
        return find_rules(dt.children_left[node], depth + 1, dt) , find_rules(dt.children_right[node], depth + 1, dt)
    else:
        pass



def generate_rules(x, y, M): # M is the number of rules
    decision_tree = tree.DecisionTreeClassifier(max_leaf_nodes=M)
    decision_tree.fit(x, y)
    print(decision_tree.tree_.feature)
    print(TREE_UNDEFINED)
    print(decision_tree.tree_.threshold)
    rules = []
    '''
    for rule in range(M):
        for attribute_number in range(7):
                
        rules += [attributes]
    '''

generate_rules(pacients_input, pacients_output, M)
'''
clauses, atomicsNumber = read_DIMACS_CNF('rules.txt')
answer = DPPL(clauses)
write_solution(clauses, atomicsNumber)
'''