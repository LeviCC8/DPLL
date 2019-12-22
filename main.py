import numpy as np
from problem_modeling import generate_model
from utilities_tests import fill_tests, performance

patients = np.genfromtxt('data/column_bin.csv', delimiter=',', skip_header=3)
patients_input = patients[:, :-1]
patients_output = patients[:, -1]

test = np.genfromtxt('data/column_bin_test.csv', delimiter=',', skip_header=3)
test_input = test[:, :-1]
test_output = test[:, -1]

RULES_NUMBER = 3  # It's necessary at least 2

generate_model(patients_input, patients_output, RULES_NUMBER, 'model.txt')
fill_tests('model.txt', test_input)

hit_rate, mean_run_time = performance(test_output, my_method=True)
print(f'### My method ###\nHit rate = {hit_rate}\nMean Run time = {mean_run_time} miliseconds')

hit_rate, mean_run_time = performance(test_output, my_method=False)
print(f'### Glucose3 ###\nHit rate = {hit_rate}\nMean Run time = {mean_run_time} miliseconds')