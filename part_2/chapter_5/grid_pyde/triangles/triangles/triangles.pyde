# def setup():
#     size(900,900)
#     rectMode(CENTER)
    
# t = 0

# def draw():
#     global t
#     translate(width/2,height/2)
#     rotate(radians(t))
#     triangle(0,0,100,100,200,-200)
#     t += 0.5


# def setup():
#     size(900,900)
#     background(7,8,9,)
#     rectMode(CENTER)
    
    
# t = 0

# def draw():
#     # background(0)
#     global t
    
#     translate(width/2,height/2)
#     rotate(radians(t))
#     tri(400)
#     t += 0.175
    
# def tri(length):
#     '''Draws an equilateral triangle around the center of triangle'''
#     fill(14,15,16)
#     triangle(
#              0,-length,
#              -length*sqrt(3)/2,length/2,
#              length*sqrt(3)/2,length/2 ,
#              )
    

def setup():
    size(900,900)
    # background(20,24,26)
    rectMode(CENTER)
    
t = 0

def draw():
    global t
    background(255)
    translate(width/2,height/2)
    colorMode(HSB)

    for i in range(90):
        # space the triangles evenly
        # around the circle
        rotate(radians(360/90))
        # Spin each triangle
        # rotate(radians(360/90))
        pushMatrix() # Save the orientation
        # Go to circumference of circle
        translate(200,0)
        # Spin each triangle
        rotate(radians(t+2*i*360/90))
        # MAke a variable for length size
        d = dist(width/2,height/2,mouseX,mouseY)
        # Draw the triangle
        tri(d)
        stroke(360/90*i,255,255)
        # Return to saved orientation
        popMatrix()
    t += 0.75
    
def tri(length):

    noFill() # Makes the triangle transparent
    triangle(
             0,-length,
             -length*sqrt(3)/2,length/2,
             length*sqrt(3)/2,length/2 ,
             )


    
