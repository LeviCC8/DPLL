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
    atomicsNumber = int(lines[1].split()[2])
    return B, atomicsNumber

def write_solution(answer, atomicsNumber):
    file = open('answer.txt', 'w')
    atomics = list(range(1, atomicsNumber+1))
    if answer == False:
        file.write('UNSATISFIABLE')
    else:
        for i in answer:
            atomics.remove(abs(i[0]))
            file.write(str(i[0]) + ' ') if i[1] == True else file.write(str(-1*i[0]) + ' ')
        for j in atomics:
            file.write(str(j) + ' ')
        file.write('0')
    file.close()