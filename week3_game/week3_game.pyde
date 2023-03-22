padX = 0 
padY = 0
padWidth = 100
padHeight = 10

r = 250
g = 250
b = 250
ballColor = color(r, g, b)
padColor = color(250, 250, 0)
xdir = 5
ydir = 5
x = 30
y = 30
diam = 30

def setup():
    global padY, padHeight, x, y
    size(900, 600)
    padY = height - padHeight
    ellipse(x, y, diam, diam)
    
def draw():
    
    global x, y, diam, xdir, ydir, ballColor, r, g, b
    global padX, pady, padWeight, padHeight
    background(190)
    fill(ballColor)
    ellipse(x, y, diam, diam)
    
    #ball
    x += xdir #a = a + 1
    y += ydir

    if x + diam/2 > width:
        xdir *= -1
        

    if x - diam/2 < 0:
        xdir *= -1

        
    if y + diam/2 > height:
        ydir *= -1

        
    if y - diam/2 < 0:
        ydir *= -1
    
    
    #pad
    padX = mouseX - padWidth/2
    if padX < 0:
        padX = 0
    elif padX + padWidth == 900:
        padX = 800
    fill(padColor)
    rect(padX, padY, padWidth, padHeight)
