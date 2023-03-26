
x = 100 #ball's x position
y = 100
xdir = 5 #ball’s direction
ydir = 5
diam = 30 #ball’s diameter

ballColor = color(255, 255, 255)
padColor = color(255, 255, 255)
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
    global ballColor
    global padY, padHeight, padWidth
    global padX, padColor
    background(200)
    
    ellipse(x, y, diam, diam)
    x = x + xdir
    y += ydir
    if x + diam/2  > width:
        xdir = xdir * -1
        ballColor = color(255, 0, 0)
        fill(ballColor)
  
    if x - diam/2 < 0:
        ballColor = color(0, 255, 0)
        fill(ballColor)
        xdir = xdir * -1
        
    if y - diam/2 < 0:
        ballColor = color(0, 0, 255)
        fill(ballColor)
        ydir = ydir * -1

    if y + diam/2 > height:
        ballcolor = color(0, 255, 255)
        fill(ballColor)
        ydir = ydir * -1
    
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth, padHeight)
    
    if x > padX and x < padX + padWidth and y + diam/2 > padY:
        ydir = ydir * -1
        pallColor = color(255, 255, 0)
        fill(padColor)
# Mission: change ball color
