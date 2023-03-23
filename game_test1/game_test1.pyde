# def setup():
#     size(900, 700)
    
# def draw():
#     background(160)
#     ellipse(450, 350, 30, 30)
#     fill(160, 150, 0)

x = 100 #ball's x position
y = 100
xdir = 4 #ball’s direction
ydir = 4
diam = 50 #ball’s diameter

padX = 0
padY = 0
padHeight = 20
padWidth = 100
def setup():
    global padY, padHeight
    size(900, 700)
    padY = height - padHeight
    #rect(0, 500, 200, 500)

def draw():
    global x, y, xdir, ydir, diam
    global padY, padHeight, padWidth, padX
    background(200)
    
    ellipse(x, y, diam, diam)
    x = x + xdir
    y += ydir
    if x + diam/2  > width:
        xdir = xdir * -1
        fill(255, 0, 0)
  
    if x - diam/2 < 0:
        xdir = xdir * -1
        fill(0, 255, 255)
        
    if y - diam/2 < 0:
        ydir = ydir * -1
        fill(255, 255, 0)

    if y + diam/2 > height:
        ydir = ydir * -1
        fill(0, 0, 255)
    
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth, padHeight)
    
    if x > padX and x < padX + padWidth and y + diam/2 > padY:
        ydir = ydir * -1

# Mission: change ball color
