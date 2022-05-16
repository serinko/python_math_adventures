def setup():
    size(900,900)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    #set background white
    background(0)
    translate(15,15)
    
    for x in range(30):
        for y in range(30):
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)
            
