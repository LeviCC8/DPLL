def read_DIMACS_CNF(file_name):
    DIMACS_CNF = open(file_name, 'r')
    lines = DIMACS_CNF.readlines()
    DIMACS_CNF.close()
    A = [x.split() for x in lines[2:]]
    B = []
    for x in A:
        C = set()
        for y in x[:-1]:
            C.add(int(y))
        B += [C]
    return B


def write_DIMACS_CNF(literals_number, clauses, comment, file_name):
    file = open(file_name, 'w')
    file.write(f'c {comment}\n')
    file.write(f'p cnf {literals_number} {len(clauses)}\n')
    for clause in clauses:
        for literal in clause:
            file.write(f'{literal} ')
        file.write('0\n')
    file.close()


def append_clauses(file_name, clauses, new_comment, new_file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    lines[0] = f'c {new_comment}\n'
    literals_number = lines[1].split()[-2]
    old_clauses_number = int(lines[1].split()[-1])
    new_clauses_number = old_clauses_number + len(clauses)
    lines[1] = f'p cnf {literals_number} {new_clauses_number}\n'
    for clause in clauses:
        line = ''
        for literal in clause:
            line += f'{literal} '
        line += '0\n'
        lines += [line]
    new_file = open(new_file_name, 'w')
    new_file.writelines(lines)
    new_file.close()


def write_solution(answer, file_name, my_method):
    file = open(file_name, 'w')
    if answer is False:
        file.write('UNSATISFIABLE')
    else:
        if my_method:
            for i in answer:
                file.write(str(i[0]) + ' ') if i[1] is True else file.write(str(-1 * i[0]) + ' ')
        else:
            for i in answer:
                file.write(str(i) + ' ')
        file.write('0')
    file.close()
