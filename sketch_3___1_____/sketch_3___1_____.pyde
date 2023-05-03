a = 90
diam = 50
xdir = 5
ydir = 5
#r = 255
y = 90
def setup():
    size(900, 600)
    a = 90
    
def draw():
    global a, diam, xdir
    global r, y, ydir
    background(190)
    ellipse(a, y, diam, diam)
    #fill(r, 255, 0)
    # if diam < 100:
    #     diam += 1
    # if diam == 100:
    #     fill(250, 250, 0)
    # if a > 300:
    #     fill(255, 0 , 0)
    
    a += xdir #a = a + 1
    y += ydir
    
    if a + diam/2 > width:
        xdir *= -1
        fill(255, 255, 0)
        #r /= 2
    if a - diam/2 < 0:
        xdir *= -1
        #r *= 2
        fill(255, 0, 0)

        
    if y + diam/2 > height:
        ydir *= -1
        #r /= 2
        
    if y - diam/2 < 0:
        ydir *= -1
        #r *= 2
    
