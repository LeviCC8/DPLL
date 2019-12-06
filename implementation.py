import numpy as np
from DPLL import DPPL
from functions_DIMACS_CNF import read_DIMACS_CNF, write_solution

pacients = np.genfromtxt('column_2C.dat', delimiter=',')

def generate_rules(pacients, m): # m is the number of rules
    pass

'''
clauses, atomicsNumber = read_DIMACS_CNF('rules.txt')
answer = DPPL(clauses)
write_solution(clauses, atomicsNumber)
'''