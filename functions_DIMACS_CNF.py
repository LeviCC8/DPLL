def read_DIMACS_CNF(file):
    DIMACS_CNF = open(file, 'r')
    lines = DIMACS_CNF.readlines()
    DIMACS_CNF.close()
    A = [x.split() for x in lines[2:]]
    B = []
    for x in A:
        C = set()
        for y in x[:-1]:
            C.add(int(y))
        B += [C]
    atomics_number = int(lines[1].split()[2])
    return B, atomics_number


def write_DIMACS_CNF(literals_number, rules, comment):
    file = open('DIMASC_CNF.txt', 'w')
    file.write(f'c {comment}\n')
    file.write(f'p cnf {literals_number} {len(rules)}\n')
    for rule in rules:
        for literal in rule:
            file.write(f'{literal} ')
        file.write('0\n')
    file.close()


def write_solution(answer, atomics_number):
    file = open('answer.txt', 'w')
    atomics = list(range(1, atomics_number + 1))
    if answer is False:
        file.write('UNSATISFIABLE')
    else:
        for i in answer:
            atomics.remove(abs(i[0]))
            file.write(str(i[0]) + ' ') if i[1] is True else file.write(str(-1 * i[0]) + ' ')
        for j in atomics:
            file.write(str(j) + ' ')
        file.write('0')
    file.close()
