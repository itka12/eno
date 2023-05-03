x = 100 #ball's x position
y = 100
xdir = 0 #ball’s direction
ydir = 0
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
    stroke(150)
    x = width/2
    y = height/2
    diam = 30
    xdir = 7
    ydir = 7
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
    background(230)
    
    #drawing ball
    fill(ballColor)
    ellipse(x, y, diam, diam)

    if mousePressed:
        x = x - xdir
        y -= ydir
        textSize(20)
        om = color(230)
        fill(om)
        text("please clock mouse", 400, 300)
    else:
        textSize(20)
        mo = color(0xFFFF0000)
        fill(mo)
        text("please click mouse", 400, 300)
    
    #drawing brick
    fill(0xff7C2A2A)
    for i,brick in enumerate(bricks):
        if brick:
            rect(i*bWidth, 0, bWidth, bHeight, 5)
    
    #ball bouncing
    if x + diam/2  > width:
        xdir = xdir * -1
        ballColor = color(255, 255, 0, 150)
        fill(ballColor)
  
    if x - diam/2 < 0:
        ballColor = color(0, 255, 0, 150)
        fill(ballColor)
        xdir = xdir * -1
        
    if y - diam/2 < 0:
        ballColor = color(0, 0, 255, 150)
        fill(ballColor)
        ydir = ydir * -1
        
    # if ball out of height
    if y + diam/2 > height:
        ballColor = color(255, 255, 255)
        fill(ballColor)
        y = 200
        x = 500
        
        #if ball is out text "game over"
        textSize(50)
        GameOverColor = color(0xFFFF1008)
        fill(GameOverColor)
        text("Game over", 400, 350)
        textSize(10)
        tryAgain = color(0xFF000000)
        fill(tryAgain)
        text("if u wanna try again press the mouse", 440, 370)
        noLoop()
        
    #Score
    score = 0
    scoreColor = color(0xFFFFFFFF)
    fill(scoreColor)
    textSize(20)
    text("score:", 50, 100)
         
    #brick and ball collision with a pad
    if y  < bHeight + diam/2:
        if bricks[x // bWidth]:
            ydir *= -1
            bricks[x // bWidth] = False
            score += 1
            
            
    #draw racket
    fill(padColor)
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth/2, padHeight)
    
    #collision with a ball
    if x > padX -diam/2 and x + diam/2 < padX + padWidth and y > padY - diam/2:
        ydir = ydir * -1
        pallColor = color(255, 255, 0)
        fill(padColor)
# if game is over and press mouse it will continuing
def mousePressed():
    loop()
