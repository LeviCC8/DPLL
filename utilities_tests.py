from DPLL import DPPL
from utilities_DIMACS_CNF import append_clauses, read_DIMACS_CNF, write_solution
import time
from pysat.solvers import Glucose3


def fill_tests(model_name, input):
    n = 0
    for x in input:
        n += 1
        new_clauses = [[a + 1] if x[a] == 1 else [(a + 1) * -1] for a in range(len(x))]
        append_clauses(model_name, new_clauses, f'Test {n}', f'tests/test_{n}.txt')


def performance(output, my_method):
    test_predict = []
    run_time = []
    for i in range(1, 156):
        A = read_DIMACS_CNF(f'tests/test_{i}.txt')
        if my_method:
            start = time.time()
            answer = DPPL(A)
            end = time.time()
            write_solution(answer, f'tests/test_{i}_my_solution.txt', my_method)
        else:
            glucose = Glucose3()
            for clause in A:
                glucose.add_clause(list(clause))
            start = time.time()
            answer = glucose.solve()
            end = time.time()
            answer = answer if answer is False else glucose.get_model()
            write_solution(answer, f'tests/test_{i}_glucose3_solution.txt', my_method)
        test_predict += [0] if answer is False else [1]
        run_time.append((end - start) * 1000.0)
    hit_rate = [x == y for x, y in zip(output, test_predict)].count(True) / len(output)
    mean_run_time = sum(run_time) / len(run_time)
    return hit_rate, mean_run_time
