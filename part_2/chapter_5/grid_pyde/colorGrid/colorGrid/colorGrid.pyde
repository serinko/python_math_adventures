def setup():
    size(600,600)
    
def draw():
    #set background white
    background(255)
    
    for x in range(20):
        for y in range(20):
            rect(30*x,30*y,25,25)
