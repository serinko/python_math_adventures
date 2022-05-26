r1 = 300.0 #radius of big circle
r2 = 175.0 #radius of circle 2
r3 = 5.0 #radius of drawing "dot"

#location of big circle
x1 = 0
y1 = 0
prop = 0.9 #proportion variable
t = 0 #time variable
points = [] #empty list to put points in

def setup():
    size(900,900)
    
def draw():
    global r1,r2,x1,y1,prop,t
    translate(width/2,height/2)
    background(255)
    noFill()
    
    #big circle
    stroke(0)
    ellipse(x1,y1,2*r1,2*r1)
    
    #circle 2
    x2 = (r1-r2)*cos(t)
    y2 = (r1-r2)*sin(t)
    ellipse(x2,y2,2*r2,2*r2)
    
    #drawing dot
    x3 = x2 + prop * (r2-r3) * cos(t)
    y3 = y2 + prop * (r2-r3) * sin(t)
    fill(255,0,0)
    ellipse(x3,y3,2*r3,2*r3)
    
    t += 0.05
