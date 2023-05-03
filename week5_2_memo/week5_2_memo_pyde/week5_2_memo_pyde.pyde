#16t toog heregledeg 0-9 a=10 b=11 c=12 d=13 e=15 f=16 

# bricks = [True, True, True, True, True, True, True, True, True, True]

# bricks = [true] * 10

# # list append method
# bricks = []
# bricks.append(1) listed nemegdeh
# bricks.append(100) nemegdeh listed
# print(bricks)


#exaple12_2
#bricks = [True for i in range(10)]
bricks  = [True] * 20

def setup():
    size(600,600)
    noStroke()
def draw():
    background(0xffffffff)
    
    for i, h in enumerate(bricks):
        if h:
            fill(0xff00ff00)
        
        else:
            fill(0xffffffff)
        rect(i*60, 0, 60, 60)
        
        rect(i*60, 60, 60, 60)
            
def mousePressed():
    if mouseY < 60:
        if bricks[mouseX/60]:
            bricks[mouseX/60] = False
        
        else:
            bricks[mouseX/60] = True  
    elif mouseY > 60 and mouseY < 120:
        if bricks[mouseX/60]:
            bricks[mouseX/60] = False
        else:
            bricks[mouseX/60] = True
