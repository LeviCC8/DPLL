import numpy as np
from sklearn import tree
from sklearn.tree._tree import TREE_UNDEFINED
from DPLL import DPPL
from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution, write_DIMACS_CNF

patients = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_header=2)
RULES_NUMBER = 6

patients_input = patients[1:, :-1]
patients_output = patients[1:, -1]
#thresholds = patients[0, :-1]
literals_number = len(patients_input[0])
#attributes = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_footer=157, dtype=str)

test = np.genfromtxt('data/column_bin_test.csv', delimiter=',', skip_header=2)
test_input = test[1:, :-1]
test_output = test[1:, -1]

#rule = [[False, False]]*literals_number
#rules = [rule]*RULES_NUMBER
# rules[n] means the nth rule
# rules[n][m] means the attributes of mth literal in the nth rule
# rules[n][m][0] == True means that literal happens truly in the nth rule
# rules[n][m][1] == True means that literal happens falsely in the nth rule
# Note that rules[n][m][0] == not rules[n][m][1] or rules[n][m][0] == rules[n][m][1] == False

'''
def find_rules(features, rules=[], branch=[], last_bifurcation=0):
    feature = features[0]
    if feature == TREE_UNDEFINED:
        branch += [feature+1]
        rules += [branch]
    else:
        last_bifurcation = feature
        find_rules(features[1:], rules, branch, last_bifurcation)
'''

def find_rules(node, dt, rules, rule=[]):
    feature = dt.tree_.feature[node]
    if feature != TREE_UNDEFINED:
        rule_left = rule.copy()
        rule_right = rule.copy()
        rule_left += [(1+feature)*-1]
        rule_right += [1+feature]
        find_rules(dt.tree_.children_left[node], dt, rules, rule_left)
        find_rules(dt.tree_.children_right[node], dt, rules, rule_right)
    else:
        leaf_label = dt.classes_[np.argmax(dt.tree_.value[node])]
        #rules += [rule]
        if leaf_label == 1:
            rules += [rule]
            # [[-33], [33, -19, -27], [33, -19, 27, -21, -10], [33, -19, 27, -21, 10], [33, -19, 27, 21], [33, 19]] len=6
        else:
            rules += [x*-1 for x in rule]
            # [[-33], [-33], [19], [27], [33, -19, 27, -21, -10], [-33], [19], [-27], [21], [-10], [33, -19, 27, 21], [33, 19]] len=12


def generate_clauses(x, y, rules_number):
    dt = tree.DecisionTreeClassifier(max_leaf_nodes=rules_number)
    dt.fit(x, y)
    # print(dt.score(test_input, test_output)) 0.8709677419354839
    rules = []
    # [[-33], [33, -19, -27], [33, -19, 27], [33, -19, -21, -10], [33, -19, -21, 10], [33, -19, 21]] ????? tá certo?
    find_rules(0, dt, rules)
    print(rules)
    print(len(rules))
    return rules


clauses = generate_clauses(patients_input, patients_output, RULES_NUMBER)
'''
clauses, atomicsNumber = read_DIMACS_CNF('rules.txt')
answer = DPPL(clauses)
write_solution(clauses, atomicsNumber)
[x==y for x, y in zip(a, b)].count(True)/len(a)
'''