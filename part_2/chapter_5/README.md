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
