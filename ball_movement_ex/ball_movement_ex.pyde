import random
bs = 20
balls = []
for i in range(10):
    x = random.randint(0, 500)
    y = random.randint(0, 100)
    ydir = random.uniform(1, 7)
    balls.append([x, y, ydir])
    
def setup():
    size(500, 500)
    
def draw():
    global bs
    background(200)
    
    for ball in  balls:
        x, y, ydir = ball
        y += ydir
        if y > 500 - bs or y < 0:
            ydir *= -1
        
        ball[1] = y
        ball[2] = ydir
        
    for ball in balls:
        x, y, b = ball
        ellipse(x, y, bs, bs)
