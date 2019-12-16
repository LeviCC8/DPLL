import numpy as np
from sklearn import tree
from sklearn.tree._tree import TREE_UNDEFINED
from functions_DIMACS_CNF import write_DIMACS_CNF

patients = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_header=3)
RULES_NUMBER = 6

patients_input = patients[:, :-1]
patients_output = patients[:, -1]

LITERALS_NUMBER = len(patients_input[0])


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
        if leaf_label == 1:
            rules += [rule]

def rules_to_clauses(rules, clauses=[]):
    if clauses == []:
        clauses += [rules[0]]
        return rules_to_clauses(rules[1:], clauses)
    if rules == []:
        new_clauses = []
        for clause in clauses:
            add_clause = True
            for n in clause:
                if n*-1 in clause:
                    add_clause = False
                    break
            if add_clause:
                new_clauses += [set(clause)]
        return new_clauses
    if rules != []:
        new_clauses = []
        for clause in clauses:
            for n in rules[0]:
                new_clauses += [clause + [n]]
        return rules_to_clauses(rules[1:], new_clauses)


def generate_clauses(x, y, rules_number):
    dt = tree.DecisionTreeClassifier(max_leaf_nodes=rules_number)
    dt.fit(x, y)
    rules = []
    find_rules(0, dt, rules)
    clauses = rules_to_clauses(rules)
    return clauses


clauses = generate_clauses(patients_input, patients_output, RULES_NUMBER)
write_DIMACS_CNF(LITERALS_NUMBER, clauses, f'RULES_NUMBER = {RULES_NUMBER}', 'rules')