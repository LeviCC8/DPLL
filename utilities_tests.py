from DPLL import DPPL
from utilities_DIMACS_CNF import append_clauses, read_DIMACS_CNF, write_solution


def fill_tests(model_name, input):
    n = 0
    for x in input:
        n += 1
        new_clauses = [[a + 1] if x[a] == 1 else [(a + 1) * -1] for a in range(len(x))]
        append_clauses(model_name, new_clauses, f'Test {n}', f'tests/test_{n}.txt')


def accuracy(output):
    test_predict = []
    for i in range(1, 156):
        A, atomics_number = read_DIMACS_CNF(f'tests/test_{i}.txt')
        answer = DPPL(A)
        write_solution(answer, f'tests/test_{i}_solution.txt')
        test_predict += [0] if answer is False else [1]
    hit_rate = [x == y for x, y in zip(output, test_predict)].count(True) / len(output)
    print(hit_rate)  # 0.8709677419354839