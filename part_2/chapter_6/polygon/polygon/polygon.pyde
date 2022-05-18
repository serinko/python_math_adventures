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
