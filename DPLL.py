# A is in clausal form
# Example of A (DIMACS CNF): [{1, -3}, {2, 3, -1}, {1}] (list of clauses, that is set of literals)

from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution
from functools import reduce

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
    clauses1 = clauses + [{literal}]
    clauses2 = clauses + [{-1*literal}]
    answer = DPPL_rec(clauses1, interpretation.copy())
    if answer != False:
        return answer
    return DPPL_rec(clauses2, interpretation.copy())


def get_literal(clauses):
    # heuristic: branch on a literal whose atom occurs most often in a clause of shortest length
    minLength = len(reduce(lambda x, y: x if len(x) < len(y) else y, clauses))
    indexes = list(filter(lambda x: len(clauses[x]) == minLength, range(len(clauses))))
    literals = reduce(lambda x, y: x.union(y) , clauses)
    literal = reduce(lambda a, b: a if sum([1 if a in clauses[x] else 0 for x in indexes]) > sum([1 if b in clauses[x] else 0 for x in indexes]) else b, literals)
    return literal

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