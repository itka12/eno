#ball
x = 100 #ball's x position
y = 100
xdir = 5 #ball’s direction
ydir = 5
diam = 30 #ball’s diameter
ballColor = color(255, 255, 255)

#pad
padColor = color(64, 206, 255)
padX = 0
padY = 0
padHeight = 10
padWidth = 2

#brick
bColNo = 10
bWidth = 0
bHeight = 0
#bricks = [True for i in range(10)]
bricks = [True] * 10

def setup():
    size(1000, 700)
    global x, y, xdir, ydir, diam, ballColor
    global padY, padHeight, padWidth, padX, padColor
    global bColNo, bWidth, bHeight
    
    x = width/2
    y = height/2
    diam = 30
    xdir = 5
    ydir = 5
    ballColor = color(255, 255, 255)
    
    padX = width/2
    padY = height - padHeight
    padWidth = 200
    padColor = color(64, 206, 255)
    
    bColNo = 10
    bWidth = width / bColNo
    bHeight = 30

def draw():
    global x, y, xdir, ydir, diam, ballColor
    global padY, padHeight, padWidth, padX, padColor
    global bColNo, bWidth, bHeight
    background(200)
    
    #drawing ball
    fill(ballColor)
    ellipse(x, y, diam, diam)
    x = x + xdir
    y += ydir
    
    #drawing brick
    fill(0xff3BB28D)
    for i,brick in enumerate(bricks):
        if brick:
            rect(i*bWidth, 0, bWidth, bHeight)
    
    #ball bouncing
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
        
    #brick and ball collision with a pad
    if y  < bHeight + diam/2 and x < bWidth:
        if bricks[x // bWidth]:
            ydir *= -1
            bricks[x // bWidth] = False
            
    #draw racket
    fill(padColor)
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth/2, padHeight)
    
    #collision with a ball
    if x > padX -diam/2 and x + diam/2 < padX + padWidth and y > padY - diam/2:
        ydir = ydir * -1
        pallColor = color(255, 255, 0)
        fill(padColor)
