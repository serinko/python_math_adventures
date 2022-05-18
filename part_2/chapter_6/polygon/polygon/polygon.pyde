def setup():
    size(600,600)
    
    
def draw(n=6,r=200):
    translate(width/2,height/2)
    beginShape()
    for i in range(n):
        vertex(r*cos(radians(360/n*i)),r*sin(radians(360/n*i)))
    endShape(CLOSE)
