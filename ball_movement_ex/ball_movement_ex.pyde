import random 
x = 0
y = 0
bs = 20
balls = []
for i in range(10):
    x = random.randint(0, 500)
    y = random.randint(5, 100)
    ydir = random.uniform(2, 10)
    balls. append([x, y, ydir])

def setup():
    size(500, 500)
    
def draw():
    global bs
    background(200)
    for ball in balls:
        x, y, ydir = ball
        y += ydir
        if y > height or y < 0:
            ydir *= -1
        
        ball[1] = y
        ball[2] = ydir
        
    for ball in balls:
        x, y, g = ball
        ellipse(x, y, bs,bs)
        
        
    
    
