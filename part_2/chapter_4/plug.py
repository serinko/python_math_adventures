# Solving mathematical equation by brute force:

def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def plug():
    x = -100 # start at -100
    while x < 100: # go up to 100
        if g(x) == 0: # if it makes the equation true
            print("x =",x) # print it out
        x += 1 # make x go up b 1 to test the next number

plug()

