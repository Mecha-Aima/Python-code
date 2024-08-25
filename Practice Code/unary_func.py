# import modules from the Python standard library
# The math module provides mathematical functions including unary functions
# Unary functions take one argument

from math import exp, log, log10, sqrt
from math import ceil, fabs, floor, modf

num = 10
num2 = 40

# UNARY FUNCTIONS
print("abs", num,":", abs(num))  # abs returns the absolute value
# exp function returns e to the power of the input
print("exp", num,":", round(exp(num).real, 2))
print("fabs", num,":", fabs(num))    
print("ceil", num,":", ceil(num))   # Ceil returns the smallest integer greater than or equal to the input
print("floor", num,":", floor(num))  # floor returns the largest integer less than or equal to the input
# log and log10 return the natural and common logarithms of the input
print("natural log", num,":", log(num))
print("common log", num,":", log10(num))
# modf returns the fractional and integer parts of the input
print("modf", num,":", modf(num))
print("round[2]", num,":", round(num, 2))   # Rounds a float to given decimal places
print("sqrt", num,":", sqrt(num).real)

