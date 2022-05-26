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
