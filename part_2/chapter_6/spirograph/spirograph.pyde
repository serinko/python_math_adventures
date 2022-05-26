r1 = 300.0 #radius of big circle
r2 = 175.0 #radius of circle 2
r3 = 5.0 #radius of drawing "dot"

#location of big circle
x1 = 0
y1 = 0
t = 0 #time variable
points = [] #empty list to put points in

def setup():
    size(900,900)
    
def draw():
    global r1,r2,x1,y1,t
    translate(width/2,height/2)
    background(255)
    noFill()
    #big circle
    stroke(0)
    ellipse(x1,y1,2*r1,2*r1)
    
