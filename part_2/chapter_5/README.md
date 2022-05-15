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



