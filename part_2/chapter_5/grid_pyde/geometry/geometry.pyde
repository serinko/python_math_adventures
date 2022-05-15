t=0
    
def setup():
    size(600,600)
    
    
def draw():
    global t
    background(0)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix() # save this orientation
        translate(200,0)
        rotate(radians(t))
        fill(100,80,255)
        rect(0,0,50,50)
        popMatrix() # return the saved orientation
        rotate(radians(360/12))
    t += 1       
