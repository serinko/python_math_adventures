from math import sqrt

def quad(a,b,c):
    '''Returns the solution of an equation of the form: a*x**2 + b*x + c = 0
    '''
    x1 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    return x1, x2

# Solving 2 * x**2 + 7*x - 15 = 0
print(
    "Testing our solution by pluging back to the equation:"
)

x = quad(2,7,-15) # returns tuple of (x1,x2)
right_side = int(input("What is the right side of the equation?"))
for i in x:
    equation_0 = 2 * i**2 + 7 * i - 15
    n=x.index(i)
    print(
        f'\nx{n+1}={i}'
        f'\npluging x{n+1} to: 2x^2 + 7x - 15 shall = {right_side}.' 
        f'\nOur equation is: 2*{i}**2 + 7*{i} - 15 = {equation_0}'
    )