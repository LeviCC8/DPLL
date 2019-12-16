import numpy as np
from DPLL import DPPL
from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution

test = np.genfromtxt('data/column_bin_test.csv', delimiter=',', skip_header=3)
test_output = test[:, -1]

test_predict = []

for i in range(1, 156):
    A, atomics_number = read_DIMACS_CNF(f'tests/patient_{i}.txt')
    answer = DPPL(A)
    write_solution(answer, f'tests/patient_{i}_diagnostic.txt')
    test_predict += [0] if answer is False else [1]

hit_rate = [x==y for x, y in zip(test_output, test_predict)].count(True)/len(test_output)
print(hit_rate) # 0.8709677419354839