import numpy
import math


# This function implements an infinite series formula for e, 1/n!
def calculate_e(terms):
    array = numpy.arange(terms)  # Create a numpy array automatically filled with the terms
    e = 0
    for term in array:
        e += 1/math.factorial(term)

    return e


num_terms = 20
for num in range(num_terms):
    estimate = calculate_e(num)
    error = math.e - estimate  # Using the math.e constant
    print("Terms: {} \t\t Estimate: {} \t\t Error: {}".format(num, estimate, error))
