# A is in clausal form
# Example of A (DIMACS CNF): [{1, -3}, {2, 3, -1}, {1}] (list of clauses, that is set of literals)

from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution

def DPPL(clauses):
    return DPPL_rec(clauses, set())

def DPPL_rec(clauses, interpretation):
    clauses, interpretation2 = unit_propagation(clauses, set())
    interpretation = interpretation.union(interpretation2)
    if set() in clauses:
        return False
    if clauses == []:
        return interpretation
    literal = get_literal(clauses)
    print(literal)
    clauses1 = clauses + [{literal}]
    clauses2 = clauses + [{-1*literal}]
    answer = DPPL_rec(clauses1, interpretation)
    if answer != False:
        return answer
    return DPPL_rec(clauses2, interpretation)


def get_literal(clauses):
    indexs = []
    minLength = 2**1024
    for i in range(len(clauses)):
        if len(clauses[i]) < minLength:
            indexs = [i]
            minLength = len(clauses[i])
        elif len(clauses[i]) == minLength:
            indexs += [i]
    literals = clauses[indexs[0]]
    for j in indexs[1:]:
        if literals.intersection(clauses[j]) != set():
            literals = literals.intersection(clauses[j])
    return literals.pop()

def unit_propagation(clauses, interpretation):
    for i in range(len(clauses)):
        if len(clauses[i]) == 1:
            unitLiteral = list(clauses[i])[0]
            interpretation = interpretation.union({(unitLiteral, False)}) if unitLiteral < 0 else interpretation.union({(unitLiteral, True)})
            A = []
            for clause in clauses:
                if unitLiteral not in clause:
                    clause.discard(-1*unitLiteral)
                    A += [clause]
            return unit_propagation(A, interpretation)
    return clauses, interpretation

A, numberAtomics = read_DIMACS_CNF('example.txt')
answer = DPPL(A)
write_solution(answer, numberAtomics)