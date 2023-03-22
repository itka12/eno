Pshape = ellipse(mouseX, mouseY, 100 ,100)

def setup():
    size(800, 600)
    
def draw():
    background(200)
    global a
    
    if mouseX > width/2:
        fill(255, 255, 0)
        #shape(circle) X
        a = circle(mouseX, mouseY, 100)
    else:
        fill(255, 0 , 0)
        #shape(rect) X
        a = rect(mouseX, mouseY, 200, 100)
