# Transforming Shapes With Geometry

## Drawing a Circle (Processing)

1. Define the size of the sketchbook - *coordinate plane*

```python
def setup():
    size(width,height)
```

2. Create the circle with `draw()` and `ellipse()`

```python
def draw():
	ellipse(x-coor,y-coor,width,height)
```

- the x,y-coordinates are the center of the ellipse

## Specifying Location Using Coordinates

- In traditional math graphs 0,0 (x,y) is in the center
- In computer graphics 0,0 is in the top left and increasing down and left
- Such setup makes it easier as everything on the screen is in positive numbers
- It is slightly more difficult to draw center oriented shapes

## Transformation Functions

### Translating Objects with translate()

To *translate* means move an object on the grid so that all the points of the object move the same direction and same distance.
The object does not change the shape even a tiny bit.

- In math each point must be translated one by one
- Processing instead moves the grid under

```python
def draw():
    rect(20,40,50,30)
```

- the drawing rect() function again reffers to x,y and the width and height.
- the x,y-coordinates are of the top left corner

**translate()**

- two parameters:
  1. tell Python how far to move the grid on the horizontal (x) axis,
  2. tell Python how far to move the grid on the vertical (y) axis.

To move the canvas to the middle, use the width and height as variables:

```python
def draw():
    translate(width/2,height/2)
```

- width and height refer to the parameters defined in `setup(width, height)` function

### Rotating Objects with rotate()

- *Rotation* is a transformation moving object around a center point.
- The `rotate()` function in Processing rotates the grid around (0,0)
- units for rotation are radians.
  - In degrees a full rotation = 360
  - In radians = 2pi * radians
- The `radians()` function converts degrees to radians

Example:

```python
def draw():
    rotate(radians(20))
    rect(50,100,100,60)
```

We can first move the grid and then rotate:

```python
def draw():
    translate(200,200)
    rotate(radians(20))
    rect(50,100,100,60)
```

1. Translate where you want the center of the circle to be (the top left corner of the grid)
2. Rotate and put the objects along the circumference of the circle

### Drawing a Circle of Circles

- Rember the circle has 360 degrees
- The centers of the circles need to be placed as 360/number of circles degrees of rotation

In Processing:

```python
def setup():
    size(600,600)
  
  
def draw():
    translate(width/2,height/2)
    for i in range(12):
        ellipse(200,0,50,50)
        rotate(radians(360/12))
```

- note that we use `radians(# degress)` to convert to radians

### Drawing a Circle of Squares

```python
def draw():
    translate(width/2,height/2)
    for i in range(12):
        rect(200,0,50,50)
        rotate(radians(360/12))
```

## Animating Objects

Normally rotation happens instantlly so we only see the result. Let's use the time variable `t` and initialize it:

- `t = 0`

```python
t=0
  
def setup():
    size(600,600)
  
  
def draw():
    global t
    background(0)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
        ellipse(200,0,50,50)
        rotate(radians(360/12))
    t += 1  
```

### Rotating the Individual Squares

Change the code inside the draw() function:

```python
t=0

def setup():
    size(600,600)
  
def draw():
    global t
    background(0)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
  
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        rotate(radians(360/12))
    t += 1  
```

This creates a bit of a strange behaviour. PErhaps nice but unexpected. Our code shall be always behaving in a way we intended so.
This behaviour is due to changing the center and orientation of the grid so much.
After translating the location we need to rotate back to the center of the circle before translating the next square.
We could use another translate() to undo the last one, but this would bring more complex problems.

**pushMatrix()** and **popMatrix()** are build in methods in Processing to save and return the orientation of the grid.

```python
# --snip--

def draw():
    global t
    background(0)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix() # save this orientation
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        popMatrix() # return the saved orientation
        rotate(radians(360/12))
    t += 1  
```

- The `pushMatrix()` function saves the position of the coordinate system at the center of the circle of squares
- the `popMatrix()` function instantly return to the center if the circle of the squares and repeat for all 12 circles

**Rotating Squares Around the Center**

The squares rotate around the upper left corner. To make them rotate around their center, add this line:
```
rectMode(CENTER)
```
To make the squares rotate faster, speed up the `t` time:
```
rotate(radians(5*t))
```
## Creating an Interactive Rainbow Grid

### Drawing a Grid of Objects
We will make a 12x12 grid we can re-use later in cellural automata.

```python
def setup():
    size(600,600)
    
def draw():
    #set background white
    background(255)
    
    for x in range(20):
        for y in range(20):
            rect(30*x,30*y,25,25)
```

### Adding the Rainbow Color
- Processing `colorMode()` adds cool colour to sketches.
- Switches between RGB and HSB mode
  - RGB - Red,Blue,Green
  - HSB - hue, saturation, brightness

```
d = dist(30*x,30*y,mouseX,mouseY)
```
- this function find a distance between two places - in this case between the square and the mouse.

```python
def setup():
    size(900,900)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    #set background white
    background(0)
    translate(15,15)
    
    for x in range(30):
        for y in range(30):
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)
            
```

## Drawing Complex Patterns Using Triangles
```python
def setup():
    size(900,900)
    rectMode(CENTER)
    
t = 0

def draw():
    global t
    translate(width/2,height/2)
    rotate(radians(t))
    triangle(0,0,100,100,200,-200)
    t += 0.5
```
Such triangle rotate arounds one of its verticles, or points.
It is not an equilateral triangle but a right triangle.


 
- Equilateral triangle is made of three equal parts.
- Three descending lines going from the center, meeting at 120 degrees

**Triangle in Processing** 

- `triangle(x-coor,y-coor, of all three verticles)`

### A 30-60-90 Triangle
- A 30-60-90 triangle can be made by cutting the bottom triangle of inner equilateral triangle in half.
- The ratio between the sides can be expressed:
  - 30degrees: x*\sqrt(3) [longer leg] :90 degrees: x [smaller leg] :60 degrees: 2*x [hypotenuse]:30 degrees 
  - Pythagorean Theoren: c2=a2+b2

### Equilateral Triangle
- based on the counting from 30-60-90 and the ratios, we can point calculate the position of the points
- read from the code:
```python
def setup():
    size(900,900)
    rectMode(CENTER)
    
t = 0

def draw():
    global t
    translate(width/2,height/2)
    rotate(radians(t))
    tri(200)
    t += 0.5
    
def tri(length):
    '''Draws an equilateral triangle around the center of triangle'''
    triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )
```
- tri function takes the variable length
  - that is the hypotenuse of special 30-60-90 triangle, we cut the equilateral into
- Find three vertices to draw our triangle inside the call to triangle function
- Specify the location of all three by each having its x and y-coordinates
  - `triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )`
- 

**Final rotating Equilateral Triangle:**

```python

def setup():
    size(900,900)
    background(7,8,9,)
    rectMode(CENTER)
    
    
t = 0

def draw():
    # background(0)
    global t
    
    translate(width/2,height/2)
    rotate(radians(t))
    tri(400)
    t += 0.175
    
def tri(length):
    '''Draws an equilateral triangle around the center of triangle'''
    fill(14,15,16)
    triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )
```

### Multiple Rotating Triangles

```python
def setup():
    size(900,900)
    # background(20,24,26)
    rectMode(CENTER)
    
    
t = 0

def draw():
    
    global t
    background(255)
    translate(width/2,height/2)
    for i in range(90):
        # space the triangles evenly
        # around the circle
        rotate(radians(360/90))
        # Spin each triangle
        rotate(radians(360/90))
        pushMatrix() # Save the orientation
        # Go to circumference of circle
        translate(200,0)
        # Spin each triangle
        rotate(radians(t))
        # Draw the triangle
        tri(150)
        # Return to saved orientation
        popMatrix()
    t += 0.5
    
def tri(length):

    noFill() # Makes the triangle transparent

    triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )
```
- `noFill()` function make the triangles transparent
- play changing the length argument in tri(length) - will change the pattern

### Phase-Shifting The Rotation
- *phase-shift* means to change the pattern in which the triangles rotate
- each will be a little bit behind the next - giving the effect of a wave or cascade
- as each is asighned to `i` number, we can add `i` to:
```
rotate(radians(t+i))
```
- for playfulness - make again variable d:
```
# Make a variable measuring distance of the mouse from the middle
d = dist(width/2,height/2,mouseX,mouseY)
# Draw the triangle
tri(d)
```
- to obfuscate the break in the patter on the right side of the screen
- to have an even smooth patter, change the `rotate` function to:
```
rotate(radians(t+i*360/90))
```
- if we add one more function of rotate like in the upper code, we can see that in the place of each triangle is two triangles, creating star.
- if we remove that and change the second rotate function into:
```
rotate(radians(t+2*i*360/90))
```
- Changing the phase by multiplying will change the pattern

### Finalizing the Design
- To add a nice rainbow, inside the for loop function, add: -
  - colorMode(hue) to setup and
  - stroke() function
```
stroke(360/90*i,255,255)
```

The final code looks like this:
```python
def setup():
    size(900,900)
    # background(20,24,26)
    rectMode(CENTER)
    
t = 0

def draw():
    global t
    background(255)
    translate(width/2,height/2)
    colorMode(HSB)

    for i in range(90):
        # space the triangles evenly
        # around the circle
        rotate(radians(360/90))
        # Spin each triangle
        # rotate(radians(360/90))
        pushMatrix() # Save the orientation
        # Go to circumference of circle
        translate(200,0)
        # Spin each triangle
        rotate(radians(t+2*i*360/90))
        # MAke a variable for length size
        d = dist(width/2,height/2,mouseX,mouseY)
        # Draw the triangle
        tri(d)
        stroke(360/90*i,255,255)
        # Return to saved orientation
        popMatrix()
    t += 0.75
    
def tri(length):

    noFill() # Makes the triangle transparent
    triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )
```
