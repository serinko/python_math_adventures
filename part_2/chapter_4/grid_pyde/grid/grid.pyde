# set tje range of x-values
xmin = -10
xmax = 10

# range of y-values
ymin = -10
ymax = 10

# Calculate the range
rangex = xmax - xmin
rangey= ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl, yscl
    background(255) #white)
    translate(width/2,height/2) # moves x,y origin to the middle of the screen
    grid(xscl,yscl) # draw grid
    
def f(x):
    return x**2    
    
def grid(xscl,yscl):
    #Draws grid for graphing  
    # setting cyan lines (1=the thinnest)
    strokeWeight(1)
    
    stroke(0,255,255) #collor of lines (rgb)
    
    # create lines in for loop
    # from xmin to xmax including xmax
    for i in range(xmin,xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        
    # same for y    
    for i in range(ymin,ymax + 1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
        
    # Create axis
    stroke(0) # black color
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
    # # Test with a circle
    # fill(0)
    # ellipse(3*xscl,6*yscl,10,10)
    
    
