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
## Specifying Location Using Coordinates

- In traditional math graphs 0,0 (x,y) is in the center
- In computer graphics 0,0 is in the top left and increasing down and left
- Such setup makes it easier as everything on the screen is in positive numbers
- It is slightly more difficult to draw center oriented shapes

