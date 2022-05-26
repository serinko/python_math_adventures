# Creating Oscillations with Trigonometry

- *Trigonometry* - The study of triangles, the right triangles and the ratio between the angles of the sides
- Functions *sine* and *cosine* are used for oscillating waves
- *sin* wave oscillating between 1 and -1 and the period of the wave is 2\pi

**Right Triangle Sides:**

- **Adjacsent** - the longer leg of the righ angle (b side)
- **Opposite** - the shorter leg of the right angle (a side)
- **Hypotenuse** - the longest side without (c side)

**Trigonometry Functions**


| **function** | **ratio**             |
| -------------- | ----------------------- |
| *sin A*      | opposite/ hypotenuse  |
| *cos A*      | adjacsent/ hypotenuse |
| *tan A*      | opposite/ adjacsent   |

```python
def f(x):
    return sin(x)
```

- Trig functions can be used to generate polygons with any number of sides as well as stars with any (odd) number of prongs.

## Using Trigonometry for Rotations and Oscillations

if:

*sin A = a/c*

then:

*a = c Sin A*

Yherefore the y-coordinate of a point ca be expressed as the distance from the origin times the sine of the angle the point makes with the  horizontal.

## Writing Functions to Draw Polygons

- Vertices are points rotating around center. This understanding make crating polygons very easy.
- Regular polygon is made by connecting certain number of points equally spaced around a circle.
- Proccessing functions `beginShape()` and `endShape()` define any shape we want
- the `vertex()` function is to define any points to build the shape

```python
def setup():
    size(600,600)
  
def draw():
    beginShape()
    vertex(100,100)
    vertex(100,200)
    vertex(200,200)
    vertex(200,100)
    vertex(150,50)
    endShape(CLOSE)

```

## Drawing a Hexagon with Loops

- The function draw could look like this:

```python
def draw():
    translate(width/2,height/2)
    beginShape()
    for i in range(6):
        vertex(100,100)
        rotate(radians(360/6))
    endShape(CLOSE)
```

- Problem is that rotate cannot be used with shape definition as it rotates the entire coordinate system.
- Solution is sine and cosine notation.

**The expresion:**

$$
(r*cos(360/6*i), r*sin(360/6*i))

$$

creates each vertex of a hexagon. When i = 0 the angle in () will be 0, when i = 1, the angle will be 60 etc.

- create variable `r`
- create variable `n` for the number of vertices
- general expression than looks like this:

```
for i in range(n):
        vertex(r*cos(radians(360/n*i)),r*sin(radians(360/n*i)))
```

The entire code to draw any polygon, looks like this:

```python
def setup():
    size(900,900)
  
  
def draw(n=3,r=400):
    translate(width/2,height/2)
    polygon(3,100) # Defines the sides, vertices and its distance from the center
  
def polygon(sides,sz):
    '''draws a polygon given the number of sides and length from the center'''
   
    beginShape()
    step = radians(360/sides)
    for i in range(sides):
        vertex(
               sz * cos(i * step),
               sz * sin(i * step)
               )
    endShape(CLOSE)
```

With this code, making a regular polygon with any number of sides shall be fairly easy.

**Adding Randomization to the Animation:**

- Processing draws object in a constant loop.
- add few random elements to the code:

```python
import random as r

def setup():
    size(900,900)
  
  
def draw():
    translate(width/2,height/2)
    x = r.randrange(3,30)
    y = r.randrange(40,400)
    z = r.randrange(0,255)
    polygon(x,y) # Defines the sides, vertices and its distance from the center
    fill(z)

# --snip--
```

## Making Sine Waves

Here is a Processing code to visualize Sine waves. The code includes Python function `enumerate()` for simplification of counting.

```python
r1 = 200 # radius of a big circle
r2 = 20 # radius of a small circle
t = 0 # time variable
circleList = []

def setup():
    size(960,960)
  
def draw():
    global t, circleList
    background(200)
    noFill()
    stroke(0)
    # move to the lef of the screen
    translate(width/4,height/2,)
    ellipse(0,0,2*r1,2*r1)
  
    # circling the ellipse:
    fill(255,0,0) #red
    y = r1*sin(t)
    x = r1*cos(t)
    ellipse(x,y,r2,r2)
    # make a trail
    # circleList.insert(0,y) and slice to prevent endless computing
    circleList = [y] + circleList[:399]
  
    # Drawing a green line and ellipse
    stroke(0,255,0) #green color
    line(x,y,400,y)
    fill(0,255,0)
    ellipse(400,y,10,10)
  
  
  
    # Loop over circleList to make a trail, using enumerate
    for idx,vl in enumerate(circleList):
        # small circle for trail:
        ellipse(400+idx,vl,5,5)
          
  
    t += 0.05
```
## Creating a Spirograph Program

*Spirograph* is a toy made up of two overlapping circular gears that slide against each other.
The gears have holes to put pencil in to draw curvy designs. We use sine and cosine to program one.

