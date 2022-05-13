from math import sqrt

def quad(a,b,c):
    '''Returns the solution of an equation of the form: a*x**2 + b*x + c = 0
    '''
    x1 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    return x1, x2

# Solving 2 * x**2 + 7*x - 15 = 0
print(
    "\nSolving a quadratic equation: ax^2+bx+c=0\n"
)


a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
c = int(input("Enter 'c': "))
right_side = int(input("Right side of the equation: "))

x = quad(a,b,c) # returns tuple of (x1,x2)
print(f"\nx = {quad(a,b,c)}")
for i in x:
    equation_0 = 2 * i**2 + 7 * i - 15
    n=x.index(i)
    print(
        f'\nx{n+1}={i}'
        f'\npluging x{n+1} to: 2x^2 + 7x - 15 shall = {right_side}.' 
        f'\nOur equation is: 2*{i}**2 + 7*{i} - 15 = {equation_0}'
    )