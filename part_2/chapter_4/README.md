# Transforming and Storing Numbers with Algebra

## Solving First Degree Equations

Say we have an equation to solve:

```latex
$2x+5=13$
```

**Using Brute Force**

```python
# Solving mathematical equation by brute force:

def plug():
    x = -100 # start at -100
    while x < 100: # go up to 100
        if 2*x + 5 == 13: # if it makes the equation true
            print("x = ", x) # print it out
        x += 1 # make x go up b 1 to test the next number
    
plug()
```

### Finding Formula for First-Degree Equations

```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}
\begin{align*}

	ax+b &= cx+d
	ax-cx &= d-b
	x(a-c) &= d-b
	x &= \frac{d-b}{a-c}

\end{align*}
\end{document}
```

### Writing the Equation() function
Since we know that ax + b = cx + d can be described as x = (d-b)/(a-c), 
a function for x can be written like this:

```python
def equation(a,b,c,d):
    '''
    Solves the equation of the form: ax + b = cx + d 
    '''
    return (d - b)/(a - c)
```

## Solving Higher Degree Equations

### 2nd Degree - Quadratic Equations

General term for a quadratic equation 

```latex
$$
ax^2 + bx + c = 0
$$
```
The quadratic formula to isolate x is:
```latex
$$
x = \frac{-b \pm \sqrt{xb^2-4ac}}{2a}
$$
```

A Python function would look like this:
```python
from math import sqrt

def quad(a,b,c):
    '''Returns the solution of an equation of the form: a*x**2 + b*x + c = 0
    '''
    x1 = (-b + sqrt(b**2 - 4 * a * c))/(2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c))/(2 * a)
    return x1, x2
```
### 3rd Degree - Cubic Equation

Example of a cubic equation:
6x**3 + 31x**2 + 3x - 10 = 0

Can be solved by a brute force plug program:
```python
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
```
## Solving Equations Graphically w Processing

Using Processing to graph higher degree equations.

- Examples can be seen here: [processing.org/examples/](https://processing.org/examples/)
- Scetches in proccessing will contain setup() and draw() functions
- setup() runce once with hitting the play button
- draw() runs as as infinnite loop until stop button
- Reference can be seen here: [processing.org/reference/](https://processing.org/reference/)

### Creating Your Own Graphing Tool

- default screen size is 600x600 pixels
- size() function changes the dimension
- draw line in Processing by declaring four numbers:
  - the x- and y-coordinates of the begining
  - and the endpoints of the line

**Code in Processing To Create a Grid With Axis in the Middle (600x600 screen)
```python
# set tje range of x-values
xmin = -10
xmax = 10

# range of y-values
ymin = -10
ymax = 10

# Calculate the range
rangex = xmax - xmin
rangey= ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
      
    background(255) #white)
    translate(width/2,height/2) # moves x,y origin to the middle of the screen
    # setting cyan lines (1=the thinnest)
    strokeWeight(1)
    
    stroke(0,255,255) #collor of lines (rgb)
    
    # create lines in for loop
    # from xmin to xmax including xmax
    for i in range(xmin,xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        
    # same for y    
    for i in range(ymin,ymax + 1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
        
    # Create axis
    stroke(0) # black color
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
```

**Adding a point (tiny ellipse)**
```python
# --snip--

# Test with a circle
    fill(0)
    ellipse(3*xscl,6*yscl,10,10)
```

### Graphing an Equation
```python
def f(x):
    return x**2    
```
This is function f(x), when Python returns the output of the function.
In this case to square a number, but any equation can be added. 
f(x) is a math commonly used name, but if needed any description is possible.


**Drawing the function**
```python
def graphFunction():
    x = xmin
    while x<=xmax:
        fill(0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x+=0.1    
```

6*x**3 + 31*x**2 + 3*x - 10 = 0






























