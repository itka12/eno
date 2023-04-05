#ball
x = 100 #ball's x position
y = 100
xdir = 5 #ball’s direction
ydir = 5
diam = 30 #ball’s diameter

#pad
ballColor = color(255, 255, 255)
padColor = color(255, 255, 255)
padX = 0
padY = 0
padHeight = 0
padWidth = 0

#brick
bColNo = 10
bWidth = 0
bHeight = 0
#bricks = [True for i in range(10)]
bricks = [True] * 10

def setup():
    global x, y, xdir, ydir, diam, ballColor
    global padY, padHeight, padWidth, padX, padColor
    global bColNo, bWidth, bHeight
    
    size(900, 700)
    
    x = width/2
    y = height/2
    diam = 30
    xdir = 5
    ydir = 5
    ballcolor = color(255, 255, 0)
    
    padX = width/2
    padY = height - padHeight
    padWidth = 200
    #rect(0, 500, 200, 500)

def draw():
    global x, y, xdir, ydir, diam, ballColor
    global padY, padHeight, padWidth, padX, padColor
    global bColNo, bWidth, bHeight
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
