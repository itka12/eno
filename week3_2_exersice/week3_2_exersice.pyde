def setup():
    size(800, 800)
    

def draw():    
    background(150)
    if mouseX < width/2 and mouseY > height/2:
        rect(0, 0, width/2, height/2)
