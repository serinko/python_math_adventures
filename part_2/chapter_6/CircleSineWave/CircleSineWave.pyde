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
    # circleList.insert(0,y)
    circleList = [y] + circleList[:399]
    
    # Drawing a green line and ellipse
    stroke(0,255,0) #green color
    line(x,y,400,y)
    fill(0,255,0)
    ellipse(400,y,10,10)
    
    
    
    # Loop over circleList to make a trail
    for idx, vl in enumerate(circleList):
        # small circle for trail:
        ellipse(400+idx,vl,5,5)
            
    
    t += 0.05
    
