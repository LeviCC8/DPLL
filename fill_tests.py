import numpy as np
from functions_DIMACS_CNF import append_clauses

test = np.genfromtxt('data/column_bin_test.csv', delimiter=',', skip_header=3)
test_input = test[:, :-1]

n = 0

for patient in test_input:
    n += 1
    new_clauses = [[x+1] if patient[x] == 1 else [(x+1)*-1] for x in range(len(patient))]
    append_clauses('rules.txt', new_clauses, f'Patient {n}', f'tests/patient_{n}.txt')