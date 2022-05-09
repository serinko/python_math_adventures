# TODO
# 1. Define the factors Function, which takes a number as an argument
# 2. Create an empty factors list to fill factors.
# 3. Loop over all the numbers from 1 to the given number
# 4. If any of these numbers divides evenly, add it to the factors list.
# 5. Return the list of factors at the end.

def factors(num):
    '''Returns a list of the factors of num'''
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors



def greatest_common_factors(num1, num2):
    '''Returns the greatest common factor (GCF) of two given numbers'''
    factors_1 = []
    factors_2 = []
    common_factors = []
    for i in range(1,num1+1):
        if num1 % i == 0:
            factors_1.append(i)
    for i in range(1,num2+1):
        if num2 % i == 0:
            factors_2.append(i)
    for i in factors_1:
        if i in factors_2:
            common_factors.append(i)
    return common_factors[-1]
